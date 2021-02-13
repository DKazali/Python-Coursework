import random


class Generator:
    RandomWord = None
    txtFile = open("words.txt", "r")
    Word = txtFile.read().split()

    def generate(self):
        self.RandomWord = random.choice(self.Word)
        return self.RandomWord
