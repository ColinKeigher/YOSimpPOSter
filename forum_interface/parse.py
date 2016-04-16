from BeautifulSoup import BeautifulSoup
import re
from time import strptime, mktime

class parse(object):
    def __init__(self, textdata):
        self.textdata = textdata
        self.htmldata = BeautifulSoup(textdata)

    def stripHTML(self, textdata):
        tag = False
        out = ''
        newlines = ['<br>', '<p>', '</p>', '<br />']
        for newline in newlines:
            textdata = textdata.replace(newline, '\n')
        out = re.sub('<[^<]+?>', '', textdata)
        out = '\n'.join([x for x in out.split('\n') if x != ''])
        return out

    def stripQuote(self, textdata):
        lines = textdata.split('\n')
        out = []
        for line in lines:
            if 'fucked around with this message at' not in line:
                if len(line) > 7:
                    if not line[:6] == 'quote:':
                        out.append(line)
                else:
                    out.append(line)
        return '\n'.join(out)

    def stripURL(self, textdata):
        out = []
        lines = textdata.split('\n')
        for line in lines:
            i = [x for x in line.split() if 'http://' not in x or 'https://' not in x]
            out.append(' '.join(i))
        return '\n'.join(out)


    def parseTimeStamp(self, timestamp):
        tformat = '%b %d, %Y %H:%M'
        out = strptime(timestamp, tformat)
        out = mktime(out)
        return int(out)

    def parseNewReply(self):
        divs = self.htmldata.findAll('div')
        out = {}
        for div in divs:
            if div.get('id') == 'thread':
                out['posts'] = self.parseReplies(textdata=div)
        return out

    def parseReplies(self, textdata):
        tables = textdata.findAll('table')
        out = {}
        for table in tables:
            if table.get('class') == 'post ':
                postID = table.get('id')
                userName = table.findAll('dt')[0].contents[0]
                for cell in table.findAll('td'):
                    if cell.get('class') == 'postbody':
                        postContents = self.stripURL(self.stripQuote(self.stripHTML('\n'.join([str(x) for x in cell.contents]))))
                    elif cell.get('class') == 'postlinks':
                        userID = int(cell.findAll('li')[0].findAll('a')[0].get('href').split('=')[-1])
                    elif cell.get('class') == 'postdate':
                        timeStamp = self.parseTimeStamp(cell.contents[-1].replace('\n',''))
                i = {
                    'postID': postID, 'userName': userName, 'postContents': postContents,
                    'userID': userID, 'timeStamp': timeStamp,
                }
                out[postID] = i
        return out