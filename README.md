# discord-attachment-download-bot

This bot is a personal project for a specific workflow i need. Currently the bot downloads attachments in every channel it can read and safes them in `[discord user name]/[file name]`.

## Discord bot setup

Go to https://discord.com/developers/applications and create and Application. Also create a bot for this application, you will need the bots token and id for the `.conf` file. Note that the bot needs the `Privileged Message Content Intent` to work, it cant see attachments of messages otherwise.

## Getting started

Python 3.10 is required. Create a virtual environment:
```
python3.10 -m venv env
```
activate the env:
```
source env/bin/activate
```
install the requirements:
```
pip install -r requirements.txt
```

Copy the `jarvis.conf.template` to `jarvis.conf` and fill in the information. Start the bot:
```
python jarvis.py
```

Invite your Application/Bot to any server you want.
