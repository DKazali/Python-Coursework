class Verification:
    rWord = None
    uWord = None

    def ver(self, random, user):
        self.rWord = random
        self.uWord = user
        if self.uWord == self.rWord:
            return True
        else:
            return False
