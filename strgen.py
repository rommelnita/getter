#!/usr/bin/env python3
# getter < https://t.me/kastaid >
# Copyright (C) 2022 kastaid
#
# This file is a part of < https://github.com/kastaid/getter/ >
# PLease read the GNU Affero General Public License in
# < https://github.com/kastaid/getter/blob/main/LICENSE/ >.

import sys
from asyncio import sleep
from subprocess import check_call

try:
    import telethon as tl
except ModuleNotFoundError:
    print("Installing Telethon...")
    # python3 -m pip install --no-cache-dir https://github.com/notudope/Telethon/archive/main.zip
    check_call(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "--no-cache-dir",
            "https://github.com/notudope/Telethon/archive/main.zip",
        ]
    )
finally:
    import telethon as tl


usage = """
Please go-to "my.telegram.org" (to get API_ID and API_HASH):
~ Login using your Telegram account.
~ Click on API development tools.
~ Create a new application, by entering the required details.

API_ID is "App api_id"
API_HASH is "App api_hash"

Or use:
- @apiscrapperbot
- @UseTGXBot
...
"""

template = """
**This is your {} based UserBots** `STRING_SESSION`
⚠️ **DO NOT SHARE WITH ANYONE** ⚠️

```{}```

Generated by KASTA <3 @kastaid
"""

generated = """
Generated !! Check your Telegram "Saved Messages" to copy STRING_SESSION or copy from above.

~ Follow our channel https://t.me/kastaid
"""

print(usage)

try:
    API_ID = int(input("Enter your API_ID here: "))
except ValueError:
    print(">>> API_ID must be an integer.\nQuitting...")
    sys.exit(0)
API_HASH = input("Enter your API_HASH here: ")

client = tl.TelegramClient(
    tl.sessions.StringSession(),
    api_id=API_ID,
    api_hash=API_HASH,
)


async def main() -> None:
    try:
        await sleep(1)
        print("Generating Telethon STRING_SESSION...")
        string_session = client.session.save()
        saved_messages = template.format("Telethon", string_session)
        print("\n" + string_session + "\n")
        await client.send_message("me", saved_messages)
        await sleep(1)
        print(generated)
        sys.exit(0)
    except tl.errors.ApiIdInvalidError:
        print(">>> Your API_ID or API_HASH combination is invalid. Kindly recheck.\nQuitting...")
        sys.exit(0)
    except ValueError:
        print(">>> API_HASH must not be empty!\nQuitting...")
        sys.exit(0)
    except tl.errors.PhoneNumberInvalidError:
        print(">>> The phone number is invalid!\nQuitting...")
        sys.exit(0)


with client:
    client.loop.run_until_complete(main())
