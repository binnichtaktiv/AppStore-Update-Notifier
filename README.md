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
- Set up a new Telegram bot by speaking to the [BotFather](https://t.me/botfather). After creating the bot, you'll receive a token. Replace the `BOT_TOKEN` value in the script with this token.
- To get your chat ID, send `/id` to [Rose](https://t.me/MissRose_bot) on Telegram. Copy your Chat ID and replace the `CHAT_ID` value in the script with this ID.

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
![Bildschirmfoto 2023-09-11 um 19 06 40](https://github.com/binnichtaktiv/AppStore-Update-Notifier/assets/96953964/5b205a32-591f-4701-a468-ba5ab209ff89)  |  ![Bildschirmfoto 2023-09-11 um 19 06 20](https://github.com/binnichtaktiv/AppStore-Update-Notifier/assets/96953964/81e84276-a307-4f59-a394-086064407ef2)
