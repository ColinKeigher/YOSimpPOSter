import requests
from BeautifulSoup import BeautifulSoup

class newreply(object):
    def __init__(self, settings, target):
        self.settings = settings
        self.target = 'https://forums.somethingawful.com/newreply.php?action=newreply&threadid=3768013'

    def initReply(self):
        r = requests.get(self.target)
        bs = BeautifulSoup(r.text)
        forms = bs.findAll('form')
        for form in forms:
            print form
            if form.get('action') == 'newreply.php':
                print form

'''
from forum_interface.newreply import newreply
np = newreply(settings=None, target=None)
np.initReply()
'''