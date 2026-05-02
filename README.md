🏎️ Sylndr Sniper
🇬🇧 British English Version
Project Overview
The Sylndr Sniper is an automated web scraping tool designed to monitor the Sylndr marketplace in Egypt for specific used car deals. Using Selenium and GitHub Actions, it periodically checks the site for new listings that match your criteria (price, mileage, transmission) and sends an instant notification to your phone via Telegram.

Key Features
Automated Monitoring: Runs every 30 minutes using GitHub Actions—completely free of charge.

Instant Alerts: Sends a detailed message to Telegram as soon as a new car is "snipped".

Smart History: Uses a CSV database to ensure you never get notified about the same car twice.

Headless Scraping: Runs in a virtual environment without needing a physical browser window open.

Setup Instructions
Fork/Clone: Copy this repository to your private GitHub account.

Telegram Bot: Create a bot via @BotFather and get your BOT_TOKEN.

Chat ID: Get your personal ID via @userinfobot.

GitHub Secrets: Go to Settings > Secrets and variables > Actions and add:

BOT_TOKEN: Your Telegram bot token.

CHAT_ID: Your Telegram chat ID.

Permissions: Ensure your Workflow permissions are set to "Read and write" in repository settings so the script can update the history file.

(بالعامية المصرية)
نظرة عامة على المشروع
الـ Sylndr Sniper هو أداة أوتوماتيكية (Web Scraper) معمولة عشان تراقب موقع Sylndr في مصر. البرنامج ده بيدور على العربيات المستعملة اللي انت محدد مواصفاتها (زي السعر، الكيلومترات، ونوع الفتيس) وأول ما بتنزل عربية جديدة مطابقة لشروطك، بيبعتلك رسالة فوراً على الموبايل عن طريق تليجرام.

أهم المميزات
شغال لوحده (Automation): البرنامج بيشتغل كل نص ساعة أوتوماتيك عن طريق GitHub Actions، يعني مش محتاج تسيب كمبيوترك شغال.

تنبيهات فورية: أول ما "يصطاد" عربية جديدة، بيبعتلك التفاصيل واللينك على تليجرام في ثواني.

ذاكرة ذكية: البرنامج بيسجل العربيات اللي شافها قبل كده في ملف CSV عشان ميزعجكش بنفس العربية مرتين.

توفير مجهود: بدل ما تدخل كل شوية تعمل Refresh للموقع، الـ Sniper بيقوم بالمهمة بدالك.

ازاي تشغله؟
اعمل Clone: خد نسخة من المشروع ده عندك على GitHub (خليه Private عشان بياناتك).

بوت تليجرام: اعمل بوت جديد من @BotFather وخد الـ BOT_TOKEN.

رقم الـ ID: اعرف رقم الـ Chat ID بتاعك من @userinfobot.

أسرار جيت-هاب (GitHub Secrets): ادخل على Settings > Secrets وضيف الـ BOT_TOKEN والـ CHAT_ID.

الصلاحيات: اتأكد إن الـ Workflow ليه صلاحية الـ "Read and write" من الإعدادات عشان يقدر يحدّث ملف العربيات اللي اتشافت قبل كده.

🛠️ Tech Stack | التكنولوجيا المستخدمة
Python: The core logic.

Selenium & BeautifulSoup: For web automation and parsing.

GitHub Actions: For 24/7 automation.

Pandas: For data management.

Telegram Bot API: For notifications.

Developed for efficient car hunting in the Egyptian market.
