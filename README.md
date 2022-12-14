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


## Systemd

If you want the bot to run as a systemd service file, use the repo example in `systemd`, copy it to `/etc/systemd/system` on your system and change the path in the service file to the correct one.
Then you can reload the systemd unit files and start/enable the bot:
```
systemctl daemon-reload
systemctl enable discord-download-bot.service
systemctl start discord-download-bot.service
```

### as non-root

If you want the service to run as non-root, create a system user:
```
useradd -r -s /bin/false discordbot
```
and add these lines in the service file under the `[Service]` tag:
```
User=discordbot
Group=discordbot
```
as well as giving the newly created user ownership of the working directory:
```
chown -R discordbot: /path/to/working/directory
```

Then reload the systemd and restart the service.
