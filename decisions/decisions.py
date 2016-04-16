from content import content

from random import randint

class decisions(object):
    def __init__(self, settings, last_post=0):
        self.min_post = 10
        self.max_paragraphs = 2
        self.last_post = last_post
        self.settings = settings

    def generateContent(self):
        c = content(settings=self.settings)
        c.paragraphs = randint(1, self.max_paragraphs)
        return c.makeContent()