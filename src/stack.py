class Stack:
    def __init__(self, rect, n, i=1):
        self.idx = i
        self.rectangle = rect
        self.length = self.rectangle.length
        self.width = self.rectangle.width
        self.rotate = self.rectangle.rotate
        self.number = n

    def use(self, n_use=1, verbose=False):
        if (self.number - n_use) >= 0:
            self.number -= n_use
            if self.number <= 0:
                return 0

        if verbose:
            return self.number

    def set_idx(self, idx):
        self.idx = idx

    def left(self):
        return self.number

    def to_dict(self):
        return {
            "idx": self.idx,
            "length": self.rectangle.length,
            "width": self.rectangle.width,
            "rotate": self.rotate,
            "number": self.number
        }

    def square(self):
        return self.rectangle.square() * self.number
