import requests
from bs4 import BeautifulSoup
import json
import os
import sys
import time
from datetime import datetime, timedelta
import telebot

BOT_TOKEN = 'YOUR_BOT_TOKEN'
CHAT_ID = 'YOUR_CHAT_ID'
bot = telebot.TeleBot(BOT_TOKEN)

def get_version_from_webpage(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Problem fetching the website.")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    version_elem = soup.select('p.whats-new__latest__version')

    if version_elem:
        version_text = version_elem[0].text.strip()
        version = version_text.split("Version ")[1].split(" ")[0]
        return version
    return None

def get_name_from_webpage(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Problem fetching the website.")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    h1_elem = soup.select_one('.product-header__title.app-header__title')

    if not h1_elem:
        return None

    span_elem = h1_elem.find('span')
    if span_elem:
        span_elem.extract()

    app_name = h1_elem.text.strip()
    return app_name

def send_telegram_message(app_name, old_version, new_version, app_link):
    msg = f"Update available for {app_name}!\n\nOld version: {old_version}\nnew version: {new_version}\n\n{app_link}"
    try:
        bot.send_message(CHAT_ID, msg)
    except Exception as e:
        print(f"Failed to send message to Telegram: {e}")

def initialize_json_file():
    if not os.path.exists("appstore_notifier_applist_DONT_DELETE.json"):
        with open("appstore_notifier_applist_DONT_DELETE.json", "w") as file:
            json.dump([], file)

def check_apps_for_updates():
    initialize_json_file()

    with open("appstore_notifier_applist_DONT_DELETE.json", "r") as file:
        apps = json.load(file)

    for app in apps:
        app_name = app['name']
        app_link = app['link']
        old_version = app['version']
        print(f"Checking {app_name} (current version: {old_version})...")
        new_version = get_version_from_webpage(app_link)

        if new_version:
            print(f"Latest version of {app_name}: {new_version}")
            if old_version != new_version:
                print("New version available! Sending message to Telegram channel.")
                send_telegram_message(app_name, old_version, new_version, app_link)
                app['version'] = new_version

    with open("appstore_notifier_applist_DONT_DELETE.json", "w") as file:
        json.dump(apps, file)

def add_app_to_checklist(app_link):
    app_name = get_name_from_webpage(app_link)
    if not app_name:
        print(f"Failed to fetch app name from the link: {app_link}")
        return

    if "https://apps.apple.com/" in app_link:
        parts = app_link.split('/')
        if len(parts) > 4 and parts[3] != "us":
            parts[3] = "us"
            app_link = '/'.join(parts)

    new_version = get_version_from_webpage(app_link)
    if new_version:
        apps = []
        initialize_json_file()

        with open("appstore_notifier_applist_DONT_DELETE.json", "r") as file:
            apps = json.load(file)
        
        # Check if the app is already in the list
        for app in apps:
            if app_name == app["name"]:
                print(f"{app_name} is already in the list with version {app['version']}.")
                return
        
        apps.append({"name": app_name, "link": app_link, "version": new_version})

        with open("appstore_notifier_applist_DONT_DELETE.json", "w") as file:
            json.dump(apps, file)  # Save updated list
        
        print(f"Successfully added {app_name} with version {new_version} to the watchlist.")
    else:
        print(f"Failed to add {app_name}. Could not fetch its version.")

if len(sys.argv) < 2:
    print("Usage: python3 script.py [add/check] [App-Link]")
    sys.exit(1)

action = sys.argv[1]

if action == "check":
    while True:
        check_apps_for_updates()
        next_check_time = datetime.now() + timedelta(minutes=20)
        print(f"Checking again in 20 minutes at {next_check_time.strftime('%H:%M:%S')}")
        time.sleep(1200)  # checks every 20 minutes
elif action == "add":
    if len(sys.argv) != 3:
        print("Usage: python3 script.py add <App-Link>")
        sys.exit(1)
    app_link = sys.argv[2]
    add_app_to_checklist(app_link)
else:
    print("Invalid action. Usage: python3 script.py [add/check] [App-Link]")
