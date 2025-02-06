# App Update Notifier

## Overview

A Python script that monitors App Store applications for version updates and sends notifications via Telegram.

## Features

- Track multiple iOS apps for version updates
- Automatically check for updates every hour
- Send update notifications to a Telegram chat
- Simple command-line interface for adding and checking apps

## Prerequisites

Make sure you have the following installed:
- Python 3.7+
- pip (Python package manager)

## Required Libraries

Install the necessary libraries using pip:

```bash
pip install pyTelegramBotAPI requests
```

## Configuration

1. Create a Telegram Bot:
   - Talk to BotFather on Telegram to create a new bot
   - Obtain your bot token

2. Get your Telegram Chat ID:
   - Use @userinfobot on Telegram or use Swiftgram app to find your Chat ID

3. Update the script with your credentials:
   - Replace `BOT_TOKEN` with your Telegram bot token
   - Replace `CHAT_ID` with your Telegram chat ID

## Usage

### Add an App to Watchlist

```bash
python3 updateNotifier.py add https://apps.apple.com/app/your-app-link
```

### Start Monitoring

```bash
python3 updateNotifier.py check
```

## How It Works

1. The script maintains a JSON file (`updateNotifier-Applist.json`) with tracked apps
2. Checks app versions every 60 minutes
3. Sends a Telegram message when a new version is detected
4. Automatically updates the local version in the watchlist

## Notes

- Ensure stable internet connection
- The script runs continuously when in check mode
- Compatible with macOS, Linux, and Windows
