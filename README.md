# 🏎️ Sylndr Sniper

## 🇬🇧 British English Version

### Project Overview
The **Sylndr Sniper** is an automated web scraping tool designed to monitor the **Sylndr** marketplace in Egypt for specific used car deals[cite: 1]. Using Selenium and GitHub Actions, it periodically checks the site for new listings that match your criteria—such as price, mileage, and transmission—and sends an instant notification to your phone via Telegram[cite: 1].

### Key Features
*   **Automated Monitoring**: Runs every 30 minutes using GitHub Actions, making it completely free of charge[cite: 1].
*   **Instant Alerts**: Sends a detailed message to Telegram as soon as a new car is "snipped"[cite: 1].
*   **Smart History**: Uses a CSV database (`seen_cars.csv`) to ensure you never get notified about the same car twice[cite: 1].
*   **Headless Scraping**: Runs in a virtual environment (Ubuntu) without needing a physical browser window open[cite: 1].

### Setup Instructions
1.  **Fork/Clone**: Copy this repository to your private GitHub account[cite: 1].
2.  **Telegram Bot**: Create a bot via `@BotFather` and retrieve your `BOT_TOKEN`[cite: 1].
3.  **Chat ID**: Retrieve your personal ID via `@userinfobot`[cite: 1].
4.  **GitHub Secrets**: Go to `Settings > Secrets and variables > Actions` and add:
    *   `BOT_TOKEN`: Your Telegram bot token[cite: 1].
    *   `CHAT_ID`: Your Telegram chat ID[cite: 1].
5.  **Permissions**: Ensure your Workflow permissions are set to "Read and write" in repository settings so the script can update the history file (`seen_cars.csv`)[cite: 1].

---

## 🇪🇬 Egyptian Arabic Version (بالعامية المصرية)

### نظرة عامة على المشروع
الـ **Sylndr Sniper** هو أداة أوتوماتيكية (Web Scraper) معمولة عشان تراقب موقع **Sylndr** في مصر[cite: 1]. البرنامج ده بيدور على العربيات المستعملة اللي انت محدد مواصفاتها (زي السعر، الكيلومترات، ونوع الفتيس) وأول ما بتنزل عربية جديدة مطابقة لشروطك، بيبعتلك رسالة فوراً على الموبايل عن طريق تليجرام[cite: 1].

### أهم المميزات
*   **شغال لوحده (Automation)**: البرنامج بيشتغل كل نص ساعة أوتوماتيك عن طريق GitHub Actions، يعني مش محتاج تسيب كمبيوترك شغال[cite: 1].
*   **تنبيهات فورية**: أول ما "يصطاد" عربية جديدة، بيبعتلك التفاصيل واللينك على تليجرام في ثواني[cite: 1].
*   **ذاكرة ذكية**: البرنامج بيسجل العربيات اللي شافها قبل كده في ملف CSV عشان ميزعجكش بنفس العربية مرتين[cite: 1].
*   **توفير مجهود**: بدل ما تدخل كل شوية تعمل Refresh للموقع، الـ Sniper بيقوم بالمهمة بدالك[cite: 1].

### ازاي تشغله؟
1.  **اعمل Clone**: خد نسخة من المشروع ده عندك على GitHub (خليه Private عشان بياناتك)[cite: 1].
2.  **بوت تليجرام**: اعمل بوت جديد من `@BotFather` وخد الـ `BOT_TOKEN`[cite: 1].
3.  **رقم الـ ID**: اعرف رقم الـ Chat ID بتاعك من `@userinfobot`[cite: 1].
4.  **أسرار جيت-هاب (GitHub Secrets)**: ادخل على `Settings > Secrets` وضيف الـ `BOT_TOKEN` والـ `CHAT_ID`[cite: 1].
5.  **الصلاحيات**: اتأكد إن الـ Workflow ليه صلاحية الـ "Read and write" من الإعدادات عشان يقدر يحدّث ملف العربيات اللي اتشافت قبل كده[cite: 1].

---

### 🛠️ Tech Stack | التكنولوجيا المستخدمة
*   **Python**: The core logic[cite: 1].
*   **Selenium & BeautifulSoup**: For web automation and parsing[cite: 1].
*   **GitHub Actions**: For 24/7 automation[cite: 1].
*   **Pandas**: For data management[cite: 1].
*   **Telegram Bot API**: For notifications[cite: 1].

---
*Developed for efficient car hunting in the Egyptian market.*
