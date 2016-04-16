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
        d = decisions(settings=settings)
        f.genReply(content=d.generateContent())
        printn('Posted to thread ID: {}'.format(threadid))
        random_wait = randint(30,3600)
        printn('Waiting {} seconds to post again.'.format(random_wait))
        sleep(random_wait)

if __name__ == '__main__':
    threadid = argv[1]
    print 'YOSimPOSter - An SA bot\n'
    main(threadid)