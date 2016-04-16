import requests
from requests import session

from newreply import newreply
from parse import parse

class forums(object):
    def __init__(self, threadid, settings):
        self.settings = settings
        self.login_url = 'https://forums.somethingawful.com/account.php?action=loginform'
        self.account = self.settings['account']
        self.threadid = threadid

    def genData(self, url, post=False, content=None):
        with session() as s:
            accnt = self.account
            accnt['action'] = 'login'
            s.post(self.login_url, data=accnt)
            if not post:
                r = s.get(url)
            else:
                r = s.get(url)
                if content is not None:
                    np = newreply(settings=self.settings, textdata=r.text)
                    np.createReply(content=content)
                    s.post(url, data=np.details)
        return r

    def genReply(self, content=None, return_data=False):
        url = 'https://forums.somethingawful.com/newreply.php?action=newreply&threadid={}'.format(self.threadid)
        req = self.genData(url=url)
        if return_data:
            return req.text
        else:
            self.genData(url=url, post=True, content=content)

    def threadRecent(self):
        p = parse(textdata=self.genReply(return_data=True))
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