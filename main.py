from forum_interface import forums
from decisions import decisions
from settings import settings

from sys import argv
from time import sleep
from random import randint

def printn(line):
    print('[*] {}'.format(line))

def main(threadid):
    printn('User account: {}'.format(settings['account']['username']))
    printn('Targetting thread ID: {}'.format(threadid))
    while True:
        f = forums(settings=settings, threadid=threadid)
        d = decisions(settings=settings, force_lower=settings['details']['force_lower'], 
            recent=f.threadRecent())
        d.shouldProceed()
        if d.canProceed:
            f.genReply(content=d.generateContent())
            printn('Posted to thread ID: {}'.format(threadid))
        else:
            printn('Not going to bother to reply as I was the last one in the thread.')
        random_wait = randint(30,1100)
        printn('Waiting {} seconds to post again.'.format(random_wait))
        sleep(random_wait)

if __name__ == '__main__':
    threadid = argv[1]
    print 'YOSimPOSter - An SA bot\n'
    main(threadid)