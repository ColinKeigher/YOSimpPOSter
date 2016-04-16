from random import randint

class decisions(object):
    def __init__(self, last_post=0):
        self.min_post = 10
        self.last_post = last_post

    def shouldPost(self):
