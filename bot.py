from pyrogram import Client
from pyrogram.errors import FloodWait
import os
import time
import random

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION")

GROUP_ID = os.getenv("GROUP_ID")

ROTATE_EVERY = int(os.getenv("ROTATE_EVERY", 3600))

USERNAMES = [
    u.strip().replace("@", "").lower()
    for u in os.getenv("USERNAMES", "").split(",")
    if u.strip()
]

app = Client(
    "userbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION
)

def change_username(username):
    try:
        app.set_chat_username(
            chat_id=GROUP_ID,
            username=username
        )

        print(f"Changed to @{username}")

    except FloodWait as e:
        print(f"FloodWait: sleeping {e.value}s")
        time.sleep(e.value)

    except Exception as e:
        print(f"Telegram says: {e}")

with app:
    print("Userbot started successfully")

    try:
        chat = app.get_chat(GROUP_ID)
        print(f"Connected to: {chat.title}")

    except Exception as e:
        print(f"Cannot access group: {e}")
        raise SystemExit

    while True:
        username = random.choice(USERNAMES)

        if len(username) < 5 or len(username) > 32:
            print(f"Skipped invalid length: {username}")
            continue

        change_username(username)

        print(f"Sleeping {ROTATE_EVERY}s")

        time.sleep(ROTATE_EVERY)
