import requests
from requests import session

from newreply import newreply
from parse import parse

class forums(object):
    def __init__(self, settings):
        self.settings = settings
        self.login_url = 'https://forums.somethingawful.com/account.php?action=loginform'
        self.account = self.settings['account']

    def genData(self, url):
        with session() as s:
            accnt = self.account
            accnt['action'] = 'login'
            s.post(self.login_url, data=accnt)
            r = s.get(url)
        return r

    def threadRecent(self, threadid):
        url = 'https://forums.somethingawful.com/newreply.php?action=newreply&threadid={}'.format(threadid)
        req = self.genData(url=url)
        p = parse(textdata=req.text)
        return p.parseNewReply()


'''
from settings import settings
from forum_interface.forums import forums
f = forums(settings=settings)
print f.threadRecent(threadid='3764241')
'''

'''
from settings import settings
from forum_interface.forums import forums
f = forums(settings=settings)
print f.cookies
'''