from wordfinder import WordFinder
from random import choice

class RandomWord(WordFinder):

    def __init__(self, file_path):
        super().__init__(file_path)
        self.fixed_text = []
    