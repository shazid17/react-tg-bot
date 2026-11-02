# Telegram Reaction Bot — GitHub + Render

## GitHub-এ আপলোড
1. GitHub-এ নতুন repository তৈরি করো।
2. এই ফোল্ডারের react-bot.py, requirements.txt, render.yaml আপলোড করো।
3. Repository Public করলেও Bot Token ফাইলে নেই—Token কখনো কোডে লিখবে না।

## Render-এ চালানো
1. https://render.com এ লগইন করো।
2. New + → Blueprint নির্বাচন করো।
3. GitHub repository connect করো।
4. Render render.yaml শনাক্ত করে Worker তৈরি করার প্রস্তাব দেবে।
5. Environment Variable চাইলে:
   - Key: BOT_TOKEN
   - Value: BotFather থেকে পাওয়া নতুন Token
6. Apply/Deploy করো।
7. Logs-এ Reaction Bot is starting... দেখলে polling শুরু হয়েছে।

## গুরুত্বপূর্ণ
- এটি Background Worker; Web Service নয়।
- Bot Token GitHub-এ commit/push করবে না।
- Telegram-এ গ্রুপে বট যোগ করো; চ্যানেলে পোস্টে রিঅ্যাকশনের জন্য প্রয়োজনীয় Admin permission দাও।
- Render-এর Free plan ও availability পরিবর্তিত হতে পারে; Worker free না থাকলে Render-এর বর্তমান plan অনুযায়ী চালাতে হবে।
- Telegram-এর permission, chat settings ও allowed reactions অনুযায়ী reaction সফল/ব্যর্থ হতে পারে।
- 
