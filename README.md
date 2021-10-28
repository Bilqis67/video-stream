<p align="center"><a href="https://t.me/VeezVideoBot"><img src="https://github.com/levina-lab/video-stream/raw/main/driver/veezlogo.png"></a></p>
<p align="center">
    <br><b>Video Stream is a telegram bot project that's allow you to play video on telegram group video chat</b><br>


## 🧪 Get `SESSION_NAME` from below:

[![GenerateString](https://img.shields.io/badge/repl.it-generateString-yellowgreen)](https://replit.com/@levinalab/StringSession#main.py) ``Pyrogram``

## ✨ Features
- Music & Video stream support
- MultiChat support
- Playlist & Queue support
- Skip, Pause, Resume, Stop feature
- Music & Video downloader feature
- Inline Search support
- YouTube direct search support
- YouTube/Local/m3u8/Radio/Live stream support

## 🛠 Commands:
- `/play (query)` - play music from youtube
- `/stream (radio link)` - stream a live streaming content
- `/vplay (query)` - play video from youtube
- `/vstream (live link)` - play video live streaming content
- `/pause` - pause the streaming (admin only)
- `/resume` - resume the streaming (admin only)
- `/skip` - switch to next stream (admin only)
- `/stop` - end the streaming (admin only)
- `/playlist` - show you all the current stream list
- `/song (query)` - download music from youtube
- `/video (query)` - download video from youtube
- `/userbotjoin` - invite the userbot to join group (admin only)
- `/userbotleave` - instruct userbot to leave the group (admin only)
- `/leaveall` - order the userbot to leave from all group (sudo only)
- `/clean` - clean all raw files
- `/rmd` - clean all downloaded files

## Heroku Deployment 💜
The easy way to host this bot, deploy to Heroku, Change the app country to Europe (it will help to make the bot stable).

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Bilqis67/video-stream)

## VPS Deployment 📡

```sh
sudo apt update && apt upgrade -y
sudo apt install git curl python3-pip ffmpeg -y
pip3 install -U pip
curl -sL https://deb.nodesource.com/setup_16.x | bash -
sudo apt-get install -y nodejs
npm i -g npm
git clone https://github.com/levina-lab/video-stream # clone the repo.
cd video-stream
pip3 install -U -r requirements.txt
cp example.env .env # use vim to edit ENVs
vim .env # fill up the ENVs (Steps: press i to enter in insert mode then edit the file. Press Esc to exit the editing mode then type :wq! and press Enter key to save the file).
python3 main.py # run the bot.
```

# Credits 💖

- [Levina](https://github.com/levina-lab) ``Dev``
- [Zxce3](https://github.com/Zxce3) ``Dev``
- [DoellBarr](https://github.com/DoellBarr) ``Dev``
- [tofikdn](https://github.com/tofikdn) ``Dev``
- [Laky's](https://github.com/Laky-64) for [``py-tgcalls``](https://github.com/pytgcalls/pytgcalls)
- [Dan](https://github.com/delivrance) for [``Pyrogram``](https://github.com/pyrogram)

### Support & Updates 🎑
<a href="https://t.me/anjingsinijoin"><img src="https://img.shields.io/badge/Join-Group%20Support-blue.svg?style=for-the-badge&logo=Telegram"></a> <a href="https://t.me/GalleryClover"><img src="https://img.shields.io/badge/Join-Updates%20Channel-blue.svg?style=for-the-badge&logo=Telegram"></a>
