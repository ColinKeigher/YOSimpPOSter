from BeautifulSoup import BeautifulSoup

class newreply(object):
    def __init__(self, settings, textdata):
        self.settings = settings
        self.textdata = textdata
        self.details = None

    def initReply(self):
        bs = BeautifulSoup(self.textdata)
        forms = bs.findAll('form')
        for form in forms:
            if form.get('action') == 'newreply.php':
                inputs = form.findAll('input')
                i = {}
                for inputval in inputs:
                    if inputval.get('type') in ['hidden', 'checkbox']:
                        name = inputval.get('name')
                        value = inputval.get('value')
                        i[name] = value                  
                self.details = i

    def createReply(self, content):
        if self.details is None:
            self.initReply()
        self.details['message'] = content

'''
from forum_interface.newreply import newreply
np = newreply(settings=None, target=None)
np.initReply()
'''