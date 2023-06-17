class Mem():
    def __init__(self, link, like_count, dislike_count):
        self.link = link
        self.like_count = like_count
        self.dislike_count = dislike_count
        
        self.raitng = self.like_count - self.dislike_count

    def data(self):
        return self.link, self.raitng