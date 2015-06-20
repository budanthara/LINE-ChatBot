# -*- coding: utf-8 -*-

from random import randint
from settings import *

class Command:
    def __init__(self):
        self.__boss_name = Settings().HERE_IAM_YOUR_BOSS

        self.jawab = \
        [
            "wah ada si bos %s, sungkem bos!", 
            "tuan muda sekaligus bos yang aku hormati %s",
            "hormat grak! bos %s datang ...",
            "mengabdi pada boss %s!",
            "*ngumpet, pak bos %s dateng",
            "wahai pak bos %s ku yang mulia",
            "bos ku %s yang tampan akhirnya berbicara", 
            "hormat sama pak boss %s yang ganteng",
            "boss %s datang , boss %s datang *sungkem",
            "pak bos %s ku yang kucinta",
            "aku setia, mengabdi pada bos %s"
        ]

        self.commands = \
        [
            "!botreply",
            "!botkatamutiara",
            "!botbioskop",
            "!bottranslate",
            "!botmeme",
            "!botyoutubemp3",
            "!botyoutubedl",
            "!bothelp",
            "!botkick" # this only works for the instruction of the boss.
        ]

        self.help_info = " \
            \n [+] Bot Help & About [+] \n \
            \n[~] List Of Commands: \n \
            \n[1]. !botreply <pesan> \
            \n[2]. !botkatamutiara \
            \n[3]. !botbioskop\
            \n[4]. !bottranslate <pesan> ( ID - EN / EN - ID) \
            \n[5]. !botmeme \
            \n[6]. !botyoutubemp3 <url youtube> \
            \n[7]. !botyoutubedl <url youtube> \
            \n[8]. !bothelp \n \
            \n[x] Coded by snoww0lf with Love & Peace <3. [x]"

    def bot_cmd(self, selected):
        return self.commands[selected]

    def bos_reply(self):
        return self.jawab[randint(0, len(self.jawab)-1)] % (self.__boss_name)

    def bos_name(self):
        return self.__boss_name
        
    def help(self):
        return self.help_info