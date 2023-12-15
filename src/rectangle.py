class Rectangle:
    def __init__(self, length, width, r=False):
        self.length = length
        self.width = width
        self.rotate = r

    def square(self):
        return self.length * self.width
