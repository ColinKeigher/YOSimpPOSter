from content import content

from random import randint

class decisions(object):
    def __init__(self, settings, last_post=0, force_lower=False, recent=None):
        self.min_post = 10
        self.max_paragraphs = 3
        self.quote_expiration = 3600
        self.quote_self = False
        self.recent = recent
        self.last_post = last_post
        self.settings = settings
        self.force_lower = force_lower
        self.recentReply = None
        self.canProceed = False

    def shouldProceed(self):
        recent = self.recentPost()
        if recent['userName'].lower() != self.settings['account']['username'].lower():
            self.canProceed = True

    def recentPost(self):
        recentPost = sorted(self.recent['posts'].keys())[-1]
        self.recentReply = self.recent['posts'][recentPost]
        return self.recentReply

    def generateContent(self):
        c = content(settings=self.settings)
        c.paragraphs = randint(1, self.max_paragraphs)
        out = c.makeContent()
        if self.force_lower:
            out = out.lower()
        if randint(1,10) in [2, 5, 6]:
            out = self.generateQuote() + out
        return out

    def generateQuote(self):
        recent = self.recentPost()
        out = '[quote="{}" post="{}"]{}[/quote]'
        out = out.format(recent['userName'], recent['postID'].replace('post', ''), 
            recent['postContents'])
        return out