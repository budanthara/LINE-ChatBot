#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.bot import main

""""
 _      _____ _   _ ______ 
| |    |_   _| \ | |  ____|
| |      | | |  \| | |__   
| |      | | | . ` |  __|  
| |____ _| |_| |\  | |____ 
|______|_____|_| \_|______| CHATBOT v1.1 by darkdivision@cbfteam / snoww0lf@Noobs1337.

These list of external libraries/another services which are i used in this application.

- Kim TaeHoon's Library called LINE ( you are fuckin awesome dude! ;) ).
- Translate Library called Goslate.
- Youtube Video Downloader Library called Pafy.
- Simsimi's Protocol.
- 1cak ( written by ) and Now Playing 21 API Services in HerokuApp.
- YoutubeInMp3's API Service.

Thanks to: Google, StackOverflow, All of Python Communities, Developer Mailing List.

====================================================
[+] FAQ ( Frequently Asked Questions ) [+]

Q: How can i get the authentication token ( authtoken ) ?
A: Reverse LINE's app protocol, Google or check the source code of LINE'S library. 
   Please, try to find it by yourself dude!

Q: Whoa, i got the authentication token! So, where i can put this ?
A: Check "settings.py" inside "src" directory. Put it into AUTH_TOKEN variable.

Q: I got an error , how do i fix it ? 
A: 
    If you are not familiar with Python just wait for the official update source code by the author ( budanthara's github ).
    If you are a core pythonic programmer, try to fix it by yourself.

Q: I tried to chat with "!botreply" mode, but i didn't get any responses.
A: The first thing you should know. The bot will replying the messages when your LINE Account already added the others contact in the same group/room.
Q: But, how do i can add the others contact when the members of the group have so many members ? 
A: Mass add group members under development, so try to add it manually for a while. Sorry btw :p

Q: Why you are using Python to make and build this app ?
A: Python more scientific, supported library and the most powerful language that i've ever known in my entire coding experience.

[+] Line Messenger ChatBot Features [+]

[1]. !botreply <pesan> -> Auto Reply Feature.
[2]. !botbioskop -> Giving you an information about now playing cinemas/films.
[3]. !botkatamutiara -> Giving you a beatiful words.
[4]. !bottranslate <pesan> ( ID - EN / EN - ID) -> Translating from Indonesia to English, English to Indonesia.
[5]. !botmeme -> Giving you a funny meme image from 1cak site.
[6]. !botyoutubemp3 <url youtube> -> Giving you a link which has converted from Youtube's video to mp3.
[7]. !botyoutubedl <url youtube> -> Giving you a link to download *.mp4 file video with the best quality.

[!] Contact me at:

* https://twitter.com/0xfbadbeef
* https://github.com/budanthara
* http://cbfteam.web.id
* http://noobs1337.net
* LINE ID: @0xffa
====================================================
"""
if __name__ == '__main__':
    main()