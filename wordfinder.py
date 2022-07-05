"""Word Finder: finds random words from a dictionary."""

from random import choice

class WordFinder:
    def __init__(self, file_path):
        self.filePath = file_path
        self.text = []
        """ This opens the file in read"""
        file = open(self.filePath, 'r')
        """ This reads the file"""
        read_data = file.read()
        """ This this splits the list on the newline character and gives and array"""
        self.text = read_data.split('\n')
        """ This give a number of word when the class has an instance"""
        print('Total Words:', len(self.text))

    # def readFile(self):
        # file = open(self.filePath,"r")
        # for line in file:
        #     self.text.append(line)
        # print( f"This file has {len(self.text)} ")

        # file = open(self.filePath, 'r')
        # read_data = file.read()
        # self.text = read_data.split('\n')
        # print('Total Words:', len(self.text))
    def random(self):
        """This randomizes the word out of the text"""


        return choice(self.text)
      


