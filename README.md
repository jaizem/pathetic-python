#Pathetic Python Bot for Discord

V. 1

Simple bot that provides humor and sarcasm in a Discord text channel.
Hosted through AWS EC2.

#To invite Pathetic Python to your server:
[Pathetic Python](https://discord.com/api/oauth2/authorize?client_id=953411405518868500&permissions=8&scope=bot)

More features coming soon. 

#How to create your own Discord bot: 

1. Create a [Discord](https://discord.com/) account. 
2. Create a Discord server to test bot in. Must have 'Manage Server' permissions to invite bots. 
3. Create an application in [Discord Developer Portal](https://discord.com/developers/applications)
4. Create bot -- the default name will be inherited from the app name, but this can be changed. 
   IMPORTANT! Make sure to copy the token when creating your bot, this is how you will connect your code to Discord.
   You can reset this if you lose it or there are security vulnerabilites. 
5. To invite your bot to a server, find 'OAuth2'
![OAuth2]()
7. Select 'Bot' from scopes, then select permissions necessary. For testing on a personal server, I recommend admin. 
![Generate URL]()
9. Copy link into browser, and invite to server you will be testing on. 


Make sure to install Discord and ENV:
```
python3 -m pip install --user virtualenv
python3 -m pip install -U discord.py
```

