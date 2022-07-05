"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """


    def __init__(self, start):
        """ intiates the class makes start value whatever the person puts in """

        self.start = start
        self.next = start 
        self.reset()
        

    def generate(self):
        """ starts serial nums at the strart number then adds on """

        newNum = self.next
        self.next = self.next + 1
        return newNum

    def reset(self):
        """resets serial to start value"""
        self.next = self.start

        

