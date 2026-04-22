import os
import re
import requests
import time
import random
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# --- CONFIG FROM GITHUB SECRETS ---
# DO NOT put your real token here. GitHub Actions will handle it securely.
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
DB_PATH = 'seen_cars.csv'
def send_telegram_msg(message):
    if not BOT_TOKEN or not CHAT_ID:
        print("Error: Missing Telegram credentials!")
        return
        
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"})
def scrape_and_snip():
    # 1. Setup Chrome
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    
    try:
        # 2. Load Page & Scroll
        url = 'https://sylndr.com/en/buy-used-cars/egypt/sylndr-market?kilometers=125000&price=300000,600000&transmission=automatic'
        driver.get(url)
        time.sleep(15)
        for _ in range(5):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(random.uniform(4, 6))
        # 3. Scrape Data
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        cards = soup.find_all(lambda tag: tag.name in ['div', 'a'] and 'EGP' in tag.get_text())
        results = []
        seen_texts = set()
        for card in cards:
            text = card.get_text(separator=' ', strip=True)
            if (text.startswith('Market') or text.startswith('Certified')) and text not in seen_texts:
                seen_texts.add(text)
                
                try:
                    match = re.search(r'(Market|Certified)\s+(.*?)\s+(\d{4})\s+.*?\s+([\dK]+)\s+KM.*?([\d,]+)\s+EGP', text)
                    if match:
                        # Try to find the href in the card or parent element
                        link = '#'
                        if card.name == 'a' and card.get('href'):
                            link = card.get('href')
                        elif card.find_parent('a'):
                            link = card.find_parent('a').get('href', '#')
                        
                        results.append({
                            'Car': match.group(2),
                            'Year': match.group(3),
                            'Mileage': match.group(4),
                            'Price_EGP': match.group(5),
                            'Fingerprint': f"{match.group(2)}_{match.group(5)}_{match.group(4)}",
                            'URL': link
                        })
                except Exception:
                    continue
        
        df_new = pd.DataFrame(results).drop_duplicates()
        
        if df_new.empty:
            print("No cars found. Check if the site structure changed.")
            return
        # 4. Compare with History (The "Sniper" logic)
        seen_fingerprints = pd.read_csv(DB_PATH)['Fingerprint'].tolist() if os.path.exists(DB_PATH) else []
        new_entries = df_new[~df_new['Fingerprint'].isin(seen_fingerprints)]
        
        # 5. Send Alerts & Save
        if not new_entries.empty:
            print(f"🔥 Found {len(new_entries)} new cars!")
            for _, row in new_entries.iterrows():
                # Handle relative URLs
                car_url = row['URL']
                if car_url.startswith('/'):
                    car_url = 'https://sylndr.com' + car_url
                
                msg = (f"🚀 *New Car Found!*\n"
                       f"🚗 *Model:* {row['Car']} ({row['Year']})\n"
                       f"💰 *Price:* {row['Price_EGP']} EGP\n"
                       f"🛣️ *Mileage:* {row['Mileage']} KM\n"
                       f"🔗 [View on Sylndr]({car_url})")
                send_telegram_msg(msg)
            
            # Save the new list so it can be committed back to GitHub
            updated_db = pd.concat([pd.DataFrame({'Fingerprint': seen_fingerprints}), new_entries[['Fingerprint']]])
            updated_db.to_csv(DB_PATH, index=False)
        else:
            print("No new ads found this run.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Always close the browser
        driver.quit()
if __name__ == "__main__":
    scrape_and_snip()
