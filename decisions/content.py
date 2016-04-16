import markovify

class content(object):
    def __init__(self, settings):
        self.settings = settings
        self.markov_text = None
        self.sentence_length = 160
        self.lines = 2
        self.paragraphs = 2

    def loadText(self):
        filename = self.settings['details']['data']
        with open(filename, 'r') as fread:
            self.markov_text = markovify.Text(fread.read())

    def makeSentence(self):
        if self.markov_text is None:
            self.loadText()
        out = self.markov_text.make_short_sentence(self.sentence_length)
        if out[-1] != '.':
            out = '{}.'.format(out)
        return out

    def makeParagraph(self):
        out = [self.makeSentence() for x in xrange(0, self.lines)]
        return ' '.join(out)

    def makeContent(self):
        out = [self.makeParagraph() for x in xrange(0, self.paragraphs)]
        return '\n\n'.join(out)

'''
from decisions.content import content
from settings import settings
c = content(settings=settings)
print c.makeContent()
'''