from wordfinder import WordFinder
from random import choice

class RandomWord(WordFinder):

    def __init__(self, file_path):
        super().__init__(file_path)
        self.fixed_text = []
    
    def random(self):
        for line in self.text:
                if not line[0] == " " or not line[0] == '#':
                    self.fixed_text.append(line)
        return choice(self.fixed_text)