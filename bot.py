from pyrogram import Client
from pyrogram.errors import FloodWait
import os
import time
import random

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION")

GROUP_ID = int(os.getenv("GROUP_ID"))

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

with app:
    print("Userbot started")

    # FORCE TELEGRAM TO CACHE THE CHAT
    dialogs = list(app.get_dialogs())

    found = False

    for dialog in dialogs:
        if dialog.chat.id == GROUP_ID:
            found = True
            print(f"Connected to: {dialog.chat.title}")
            break

    if not found:
        print("Group not found in dialogs")
        raise SystemExit

    while True:
        username = random.choice(USERNAMES)

        try:
            app.set_chat_username(GROUP_ID, username)

            print(f"Changed to @{username}")

        except FloodWait as e:
            print(f"FloodWait: {e.value}s")
            time.sleep(e.value)

        except Exception as e:
            print(f"Telegram says: {e}")

        print(f"Sleeping {ROTATE_EVERY}s")

        time.sleep(ROTATE_EVERY)
