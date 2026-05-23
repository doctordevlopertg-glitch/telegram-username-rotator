from pyrogram import Client
from pyrogram.errors import (
    FloodWait,
    UsernameOccupied,
    UsernameInvalid
)

import os
import time
import random

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION")

GROUP_ID = os.getenv("GROUP_ID")

ROTATE_EVERY = int(os.getenv("ROTATE_EVERY", 1800))

USERNAMES = os.getenv("USERNAMES").split(",")

app = Client(
    "rotator",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION
)

def change_username(username):
    try:
        app.set_chat_username(GROUP_ID, username)

        print(f"Changed to @{username}")

    except UsernameOccupied:
        print(f"{username} occupied")

    except UsernameInvalid:
        print(f"{username} invalid")

    except FloodWait as e:
        print(f"FloodWait: {e.value}s")

        time.sleep(e.value)

    except Exception as e:
        print(e)

with app:
    while True:
        username = random.choice(USERNAMES)

        change_username(username)

        print(f"Sleeping {ROTATE_EVERY}s")

        time.sleep(ROTATE_EVERY)
