# -*- coding: utf-8 -*-

try:
    from constants import *
    from command import * 
    from settings import *
    from line import *
    import urllib2, urllib, json
    import re, sys, os, argparse
    from threading import Thread
    from time import sleep
    from random import randint, randrange, uniform
    from goslate import Goslate
    from pafy import new
except ImportError, e:
    print "[+] Please install -> %s first!" % (e)

try:
    client = LineClient(authToken=Settings().AUTH_TOKEN)
except Exception as reason:
    print "[+] Login Failed! [+]"
    print "[+] Reason: ", reason

class LineAutoBot(object):
    def __init__(self, group):
        self.group = group
        self.__consts = Constants()
        self.__settings = Settings()
        self.__trans = Goslate()
        self.obj = json.loads(self.__consts.WANCAK_RAND.read())

    def katamutiara(self):
        count_rows = 0
        with open(os.path.join(os.path.dirname(__file__), self.__consts.PATH_KATAMUTIARA,\
            'kalimat.txt'),'r') as f:
            read_kalimat = f.readlines()
        with open(os.path.join(os.path.dirname(__file__), self.__consts.PATH_KATAMUTIARA,\
            'bagian.txt'),'r') as fs:
            read_bagian = fs.readlines()
            count_rows+=sum(1 for _ in read_bagian)
        for x in range(0, count_rows+1):
            j = randint(0, 110)
            join_data = "<bot-filsafat>" + "\n\n" + \
            read_kalimat[j] + "\n" + read_bagian[j]
            self.group.sendMessage(join_data)
            break
        return count_rows

    def translate(self, msg):
        detect = str(self.__trans.detect(msg))
        if 'id' in detect:
            send_translate = "<bot-translate> %s " % (self.__trans.translate(msg[14:], 'en'))
            send = self.group.sendMessage(send_translate)
        elif 'en' in detect:
            send_translate = "<bot-translate> %s " % (self.__trans.translate(msg[14:], 'id'))
            send = self.group.sendMessage(send_translate)
        else:
            send = self.group.sendMessage("<bot-translate> Gak ngerti!")

    # Running under Linux OS/Windows OS/Etc.
    def meme(self):
        self.__consts.WANCAK_RAND.close()
        url_image = str(self.obj['img'])
        urlreq = urllib2.Request(url_image, headers=self.__consts.CONST_REFERER)
        op = urllib2.urlopen(urlreq)
        sv_file = open(url_image[-38:],'wb+')
        sv_file.write(str(op.read()))
        sv_file.close()
        self.group.sendImage(url_image[-38:])

    # Running under Linux OS Only.
    """
    def another_meme(self):
        self.__consts.WANCAK_RAND.close()
        url_image = str(self.obj['img'])
        header = 'Referer: http://1cak.com/'
        savedir = '/tmp/'
        cmd = "wget %s --header='%s' -P %s" % (url_image, header,savedir)
        get_image = os.system(cmd)
        #regex_url = re.search('http://cdn14.1cak.com/posts/(.*)', url_image).group(1)
        position = '%s%s' % (savedir, url_image[-38:])
        self.group.sendImage(position)
    """

    # convert youtube video to mp3.
    def youtubemp3(self, link, profile, mesg):
        try:
            if profile in mesg:
                sys.exit()
            else:
                url = "%s%s" % (self.__consts.YOUTUBE_CONVERTER, link)
                #header = 'Referer: http://youtubeinmp3.com/api/'
                #urlreq = urllib2.Request(url, headers=header)
                urlop = urllib2.urlopen(url)
                obj = json.loads(urlop.read())
                msg = "\
                \n [+] Judul: %s \
                \n[+] Link Download Mp3: %s" % (obj['title'], obj['link'])
                self.group.sendMessage(msg)
        except Exception: 
            self.group.sendMessage("[+] Sory bro!, URL youtube tidak valid! [+]")

    # download youtube video with the best quality.
    def youtube_download(self, url, profile, mesg):
        try:
            if profile in mesg:
                sys.exit()
            else:
                video = new(url)
                get_vid = video.getbest(preftype="mp4")
                #dl = get_vid.download(quiet=False, filepath=self.__settings.SITE_PATH)
                msg = " \
                \n [+] Judul Video: %s \n \
                \n[+] Uploader: %s \n \
                \n[+] Durasi: %s \n \
                \n[+] Link Download: %s%s.%s \n \
                \n[+] File video akan dihapus 1 menit lagi. \n \
                " % (video.title, video.author, video.duration, self.__settings.SITE_URL, \
                    video.title.replace(" ", "%20"), get_vid.extension)
                self.group.sendImageWithURL(video.thumb)
                self.group.sendMessage(msg)
        except Exception:
            self.group.sendMessage("[+] Sory broh!, URL youtube tidak valid! [+]")

    def another_simsimi(self, msg, name, profile, mesg):
        if profile in mesg:
            sys.exit()
        else:
            acak = str(int(uniform(100000,300000)))
            data = {'av': 5.2, 'ft': 1.0, 'lc': 'id', 'os': 'i', 'req': msg, \
            'tz': "Asia/Jakarta", 'uid': acak}
            url = self.__consts.SIMI_CHAT + urllib.urlencode(data)
            data = urllib2.urlopen(url)
            jawab = json.loads(data.read())
            bot_jawab = "<bot> @%s: %s" % (name, jawab['sentence_resp'].replace\
                ("simi", self.__settings.REPLACEMENT_CALL))
            self.group.sendMessage(bot_jawab)

    def jadwal_bioskop(self):
        nresults = urllib2.urlopen(self.__consts.MOVIE_PLAYING)
        obj = json.loads(nresults.read())
        nresults.close()
        total = 0
        msg = ''
        try:
            dt = "\n <bot> Misi permisi, ini film di bioskop yang lagi tayang ...\n"
            for out in obj:
                print ""
                show = "\n [+] Judul: %s \n [~] Link: %s \n" % (out['title'], out['url'])
                join_data = ''.join(show.split("\t"))
                outmsg = "%s" % (join_data)
                msg+=outmsg
                total+=1
            lastmsg = "\n [+] Total film baru tayang: %d film" % (total)
            self.group.sendMessage(dt+msg+lastmsg)
        except urllib2.HTTPError as err:
            print "Something went wrong!", err
        return total, msg

# Execute it !
def execute_bot(data, obj):
    try:
        n1 = 2
        cmd = Command()
        myprofile = str(client.profile)
        messages1 = data.getRecentMessages(count=n1)
        for x in range(0, n1):
            last_message = str(messages1[x])
            regex = re.search('msg="(.+?)"', last_message).group(1)
            regex_name = re.search('sender=<LineContact (.+?)>', last_message).group(1)
            quote = urllib.quote_plus(regex)
            if cmd.bot_cmd(0) in last_message:
                if myprofile in last_message:
                    continue
                elif Settings().HERE_IAM_YOUR_BOSS in regex_name:
                    reply = "<bot> %s" % (cmd.bos_reply())
                    data.sendMessage(reply)
                    obj.another_simsimi(regex[10:], regex_name, myprofile, str(messages1[0]))
                else:
                    obj.another_simsimi(regex[10:], regex_name, myprofile, str(messages1[0]))
                    continue
            elif cmd.bot_cmd(1) in last_message:
                obj.katamutiara()
            elif cmd.bot_cmd(2) in last_message:
                obj.jadwal_bioskop()
            elif cmd.bot_cmd(3) in last_message:
                msg = "[+] Trying to translate: %s" % (regex[14:])
                data.sendMessage(msg)
                obj.translate(regex)
            elif cmd.bot_cmd(4) in last_message:
                msg = "[+] Here the pic bro %s!" % (regex_name)
                data.sendMessage(msg)
                obj.meme()
            elif cmd.bot_cmd(5) in last_message:
                obj.youtubemp3(regex[15:], myprofile, str(messages1[0]))
            elif cmd.bot_cmd(6) in last_message:
                obj.youtube_download(regex[14:], myprofile, str(messages1[0]))
            elif cmd.bot_cmd(7) in last_message:
                data.sendMessage(cmd.help())
            elif cmd.bot_cmd(8) in last_message:
                if cmd.bos_name() in regex_name:
                    data.sendMessage("<bot> Bye!")
                    client.leaveGroup(data)
                else:
                    data.sendMessage("<bot> Oops, gak bisa!")
    except Exception, e:
        print e    

def show_details(data):
    for i in range(0, len(data)):
        if data[i] is not None:
            print "%s," % (data[i].name),

def show_details_group_or_room(data, stats):
    if stats is 'groups':
        for i in range(0, len(data)):
            if data[i] is not None:
                if data[i].is_joined is True:
                    print "[+] Group %d : %s ( Already Joined )" % (i+1, data[i].name)
                else:
                    print "[+] Group %d : %s ( Invited )" % (i+1, data[i].name)
    elif stats is 'rooms':
        for i in range(0, len(data)):
            if data[i] is not None:
                r_contacts = data[i]
                data[i] = "Room%d" % (i+1)
                init_room = data[i]
                print "[+] %d. Room's Alias -> %s ( %s )" % (i+1, init_room, r_contacts.contacts)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-sg','--showgroups',\
    help='Show All Groups In Your Contact', action='store_true')
    parser.add_argument('-sr','--showrooms',\
    help='Show All Rooms In Your Contact', action='store_true')
    parser.add_argument('-sc','--showcontacts',\
    help='Show All Contacts', action='store_true')
    parser.add_argument('-sa','--showall',\
    help='Show All Groups, Rooms, and Contacts', action='store_true')
    parser.add_argument('-r','--refresh',\
    help='Refresh All Groups, Rooms, and Contacts', action='store_true')
    # merging
    merge = parser.add_argument_group('Important Arguments', "Executing Bot Command")
    merge.add_argument('--mode', help='Mode group/room/contact')
    merge.add_argument('--target', help='Target group/room/contact')
    merge.add_argument('--execute', help='Execute the bot', action='store_true')
    # acc groups
    parser.add_argument('--accept-group', help='Accept Group')
    option = parser.parse_args()

    execute_mode = [option.mode, option.target, option.execute]
    groups = client.groups
    rooms = client.rooms
    contacts = client.contacts

    if option.showgroups:
        show_details_group_or_room(groups, "groups")
    elif option.showrooms:
        show_details_group_or_room(rooms, "rooms")
    elif option.showcontacts:
        print "[+] Contacts: ", show_details(contacts)
    elif option.showall:
        print "[+] Groups: ", show_details(groups)
        print "[+] Rooms: ", rooms
        print "[+] Contacts: ", show_details(contacts)
    elif all(execute_mode):
        if 'group' in option.mode:
            if 'all' in option.target:
                for i in range(0, len(groups)):
                    group = client.getGroupByName(groups[i].name) 
                    obj = LineAutoBot(group)
                    # threading start!
                    s_thread = Thread(target=execute_bot, args=(group, obj))
                    s_thread.start()
                    s_thread.join()
            else:
                group = client.getGroupByName(option.target)
                obj = LineAutoBot(group)
                execute_bot(group, obj)
        elif 'room' in option.mode:
            if 'all' in option.target:
                for i in range(0, len(rooms)):
                    init_room = rooms[i]
                    obj = LineAutoBot(init_room)
                    # threading start!
                    s_thread = Thread(target=execute_bot, args=(init_room, obj))
                    s_thread.start()
                    s_thread.join()
            else:
                for i in range(0, len(rooms)):
                    init_room = "Room%d" % (i+1)
                    if init_room in option.target:
                        init_room = rooms[i]
                        obj = LineAutoBot(init_room)
                        execute_bot(init_room, obj)
        elif 'contact' in option.mode:
            contact = client.getContactByName(option.target)
            obj = LineAutoBot(contact)
            execute_bot(contact, obj)
    elif option.accept_group:
        group = client.getGroupByName(option.accept_group)
        accept_group = client.acceptGroupInvitation(group)
        tosend = "<bot> " + Settings().WELCOME_MESSAGE
        group.sendMessage(tosend)
    elif option.refresh:
        client.refreshContacts()
        client.refreshGroups()
        client.refreshActiveRooms()
        print "[+] All Contacts, Groups, Rooms already Refreshed! [+]"
    else: parser.print_help()