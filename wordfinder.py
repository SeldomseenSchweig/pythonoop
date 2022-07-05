"""Word Finder: finds random words from a dictionary."""

from random import choice

class WordFinder:
    def __init__(self, file_path):
        self.filePath = file_path
        """ This opens the file in read"""
        file = open(self.filePath, 'r')
        """ This reads the file"""
    
        """ This this splits the list on the newline character and gives and array"""
        self.text = self.parse(file)
        """ This give a number of word when the class has an instance"""
        print('Total Words:', len(self.text))

    def random(self):
        """This randomizes the word out of the text"""


        return choice(self.text)
    
class SpecialWordFinder(WordFinder):

    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""

        return [w.strip() for w in dict_file if w.strip() and not w.startswith("#")]

