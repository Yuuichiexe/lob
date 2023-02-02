<h1 align="center">🎵 SHIKIX MUSIC V0.1 🎵</h1>

### A bot that can stream music on Telegram Groups and Channels Voice Chats
#### POWERED BY [OTAZUKI](https://github.com/Otazuki004) & [The Gtash](https://github.com/Awesome-Gtash)
### Available on telegram as [@ShikiXPro_1Bot](https://t.me/shikixpro_1bot)

<p align="center">
  <img src="https://telegra.ph/file/dd04b1968f1bc1169d162.jpg">
</p>

<h2> Features 💙 </h2>

- Thumbnail Support
- Playlist Support
- Current playback support
- Showing track names when skipping
- Zero downtime, Fully Stable
- Youtube playback support
- Settings panel
- Control with buttons
- Userbot auto join
- Channel Music Play
- Keyboard selection support for youtube play

## 🚀 Deployment

### 💫 Heroku Deploy 💫

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### ⚔ Self-hosting
```sh
# First Upgrade Your Terminal
$ sudo su (if terminal not have root access)
$ cd (if terminal not have root access)
$ apt update && apt upgrade -y
$ apt install python ffmpeg -y
$ curl -fssL https://deb.nodesource.com/setup_17.x | sudo -E bash -
$ apt install nodejs -y
$ pip3 install -U pip
$ npm i -g npm
# Now Do Git Clone
$ git clone https://github.com/Awesome-Gtash/ShikiXmusic
$ cd ShikiXMusic
# Upgrade sources
# Install All Requirements 
$ pip3 install -U -r requirements.txt
# Now Edit example.env and enter your creds
$ cp example.env .env
# Now start the Bot
$ python3 -m ShikiXMusic
```

### Commands for Group 🛠
#### For all in group

- `/play <song name>` - play song you requested
- `/play <reply to audio>` - play replied file
- `/ytplay <song name>`: Directly play song via Youtube Music
- `/playlist` - Show now playing list
- `/current` - Show now playing
- `/song <song name>` - download songs you want quickly
- `/search <query>` - search videos on youtube with details
- `/video <song name>` - download videos you want quickly

#### Admins only.
- `/player` - open music player settings panel
- `/pause` - pause song play
- `/resume` - resume song play
- `/skip` - play next song
- `/end` - stop music play
- `/mute` - mute song play
- `/unmute` - unmute song play
- `/userbotjoin` - invite assistant to your chat
- `/userbotleave` - remove assistant from your chat
- `/admincache` - Refresh admin list
- `/musicplayer [on/off]` - Enable/Disable Music Player

### Commands for Channel Music Play 🛠
For linked group admins only:
- `/cplay <song name>` - play song you requested
- `/cplay <reply to link>` - play replied youtube link
- `/cplay <reply to audio>` - play replied file
- `/cplaylist` - Show now playing list
- `/cccurrent` - Show now playing
- `/cplayer` - open music player settings panel
- `/cpause` - pause song play
- `/cresume` - resume song play
- `/cskip` - play next song
- `/cend` - stop music play
- `/cmute` - mute song play
- `/cunmute` - unmute song play
- `/userbotjoinchannel` - invite assistant to your chat
* channel is also can be used instead of c

If you donlt like to play in linked channel:
 1. Get your channel ID.
 2. Rename your group to: Channel Music: your_channel_id
 3. Add @ShikiXPro_1Bot as Channel admin with full perms
 4. add helper to channel
 5. Simply send commands in your group.

### Commands for Sudo Users ⚔️
- `/userbotleaveall` - remove assistant from all chats
- `/gcast <reply to message>` - globally brodcast replied message to all chats
- `/pmpermit [on/off]` - enable/disable pmpermit message

#### Pmpermit
- `.a` - approove someone to pm you
- `.da` - disapproove someone to pm you
+ Sudo Users can execute any command in any groups


## Contributors
- [The Gtash](https://github.com/awesome-gtash)
- [Otazuki](https://github.com/otazuki004)

## Copyright & License 👮

 - Copyright (C) 2023-present by [Otazuki](github.com/otazuki004) ❤️️
 - Licensed under the terms of the [MIT License](https://github.com/Awesome-Gtash/ShikiXMusic/blob/master/LICENSE)
    
ShikiXMusic is Free Software: You can use, study share and improve it at your will. Specifically you can redistribute and/or modify it under the terms of the MIT License as published by the Free Software Foundation.    
## Made with ♥️ by [The Gtash](https://github.com/Awesome-Gtash) & [Otazuki](https://github.com/otazuki004)
