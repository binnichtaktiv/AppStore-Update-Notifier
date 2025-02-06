import re
import os
import sys
import time
import json
import urllib
import telebot
import requests
from uuid import uuid4
from datetime import datetime, timedelta

BOT_TOKEN = 'abc'
CHAT_ID = 'abc'
REQUEST_CHAT_ID = 'abc'
API_ID = 123
API_HASH = 'abc'

bot = telebot.TeleBot(BOT_TOKEN)

def check():
    with open("updateNotifier-Applist.json", "r") as appsJson:
        appList = json.load(appsJson)

        for app in appList:
            try:
                appName = app["name"]
                listAppVersion = app["version"]
                appLink = app["link"]
                country = app.get("country", "us")
                
                print(f"[*] checking {appName} - current version {listAppVersion}")
                
                if None in (appLink, appName):
                    print(f"[!] Invalid entry for {appName}")
                    continue

                appLink, apiAppVersion, appName = getApp(appLink, country)

                if listAppVersion != apiAppVersion:
                    print(f"[$] new version available! {listAppVersion} -> {apiAppVersion}")
                    msg = f"update available for {appName}\n\nold version: {listAppVersion}\nnew version: {apiAppVersion}\n\n{appLink}"
                    try:
                        bot.send_message(CHAT_ID, msg)
                    except Exception as e:
                        print(f"[!] failed to send message to Telegram: {e}")

                    app["version"] = apiAppVersion

                    with open("updateNotifier-Applist.json", "w") as appsJson:
                        json.dump(appList, appsJson, indent=4)

            except Exception as e:
                print(f"[!] Error checking {app.get('name','unknown app')}: {str(e)}")
                continue

def getApp(appLink, country):

    appID = re.search(r"/id(\d{9,10})", appLink).group(1)

    try:
        with(urllib.request.urlopen(f"https://itunes.apple.com/lookup?id={appID}&country={country}&limit=1&noCache={uuid4()}")) as req:
            resp = json.load(req)

            if resp["resultCount"] == 0:
                bot.send_message(CHAT_ID, f"app seems to be offline!\n{appLink}")
                raise ValueError("app seems to be offline")  
            
            else:
                appName = resp["results"][0]["trackName"]
                apiAppVersion = resp["results"][0]["version"]
                appLink = "https://apps.apple.com/app/id" + appID
                #appLink = resp["results"][0]["trackViewUrl"]
                return appLink, apiAppVersion, appName
        
    except Exception as e:
        print("erorr: ", e)

if len(sys.argv) < 2:
    print("usage: python3 script.py [add/check] [AppStore Link]")
    sys.exit(1)

action = sys.argv[1]

if sys.argv[1] == "check":
    while True:
        check()
        nextCheck = datetime.now() + timedelta(minutes=60)
        print(f"[-] next update check in 60 minutes at {nextCheck.strftime('%H:%M:%S')}")
        time.sleep(1*60*60)

elif sys.argv[1] == "add":
    if len(sys.argv) != 3:
        print("Usage: python3 script.py add <App-Link>")
    appLink = sys.argv[2]
    appLink, apiAppVersion, appName = getApp(appLink)
    if apiAppVersion:
        if not os.path.exists("updateNotifier-Applist.json"):
            data = [{
                "name": appName,
                "version": apiAppVersion,
                "link": appLink
            }]
            with open("updateNotifier-Applist.json", "w") as appsJson:
                    json.dump(data, appsJson, indent=4)
            sys.exit()
            
        with open("updateNotifier-Applist.json", "r") as appsJson:
            appList = json.load(appsJson)

            for app in appList:
                if appName == app["name"]:
                    print(f"[!]{appName} is already in the list with version {app['version']}")
                    sys.exit()
        
            appList.append(
                {
                "name": appName,
                "version": apiAppVersion,
                "link": appLink
                }
            )
            with open("updateNotifier-Applist.json", "w") as appsJson:
                json.dump(appList, appsJson, indent=4)  # Save updated list
            print(f"[*] successfully added {appName} with version {apiAppVersion} to watchlist.")
    else:
        print(f"[!] failed to add {appName}")
