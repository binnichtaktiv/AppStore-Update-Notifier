# 📱 AppStore-Update-Notifier

A Python script designed to track updates for specific iOS apps on the App Store and notify you via Telegram whenever a new version is available.

---

## **Features:**
- 🕵️‍♂️ **Automated App Store scraping**: No need for manual checks, let the script do the work.
- 📬 **Telegram Notifications**: Receive instant notifications directly on your Telegram account.
- 📌 **Extendability**: Can easily be extended to track multiple apps.
- 🌍 **Universal OS Support**: The script has been designed to run on any operating system, including Windows.


---

## **Prerequisites:**
1. **Python 3.x**: Ensure Python is properly installed.
2. **Telegram bot token**: Required for sending Telegram notifications.
3. **Telegram chat ID**: So the script knows where to send the notifications.

---

## **Installation:**

### 1. Clone the Repository
```git clone https://github.com/binnichtaktiv/AppStore-Update-Notifier```


```cd AppStoreUpdateNotifier```

### 2. Install the requirements
```pip3 install requests bs4 pyTelegramBotAPI```

### 3. Telegram Bot Setup
- Set up a new Telegram bot by speaking to the [BotFather](https://t.me/botfather). After creating the bot, you'll receive a token.
- To get your chat ID, send `/id` to [Rose](https://t.me/MissRose_bot) on Telegram.

  Enter the bot token and chat ID the first time you run the program

---

## **Usage:**

### 1. To Add an App for Tracking
```python3 updateNotifier.py add [App-Link]```


Replace `[App-Link]` with the link to the iOS app on the App Store.

### 2. To Check for Updates
```python3 updateNotifier.py check```


This command will initiate the checking process. You'll be notified on Telegram if any tracked app has a new version available. The script checks every 20 minutes.

## **Why Scrape Instead of Using API?**:
You might be wondering why the script scrapes the App Store instead of just using Apple's official API. The answer is quite simple:
1. **Speed**: Scraping proves to be several hours faster than fetching data through the API. This ensures that you get the notifications in almost real-time.
2. **Timely Updates**: For reasons best known to Apple, updates reflected via their API often lag behind. Scraping ensures that you get notified of updates the moment they hit the App Store.


Website:                   |  Api:
:-------------------------:|:-------------------------:
<img src="https://github.com/binnichtaktiv/AppStore-Update-Notifier/assets/96953964/d54ad84b-5ab9-4a2f-99fd-76887bbc33e5" alt="Bildschirmfoto 2023-09-12 um 10 05 21" width="400"/>  |  <img src="https://github.com/binnichtaktiv/AppStore-Update-Notifier/assets/96953964/c09d67b6-c2a1-4bea-9267-04b04292ff39" alt="Bildschirmfoto 2023-09-12 um 10 06 19" width="400"/>




With the way this script works, you can get results a few hours earlier than with Apples API


credits to [zxcvbn](https://github.com/asdfzxcvbn) for the idea and the first version (that uses the API)
