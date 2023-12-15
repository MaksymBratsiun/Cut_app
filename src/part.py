class Part:
    def __init__(self, rect, start, idx=0):
        self.idx = idx
        self.rectangle = rect
        self.start_coordinates = start  # left bottom corner tuple (x, y)
        self.finish_coordinates = (self.start_coordinates[0] + self.rectangle.length,
                                   self.start_coordinates[
                                       1] + self.rectangle.width)  # right top corner tuple (x1, y1)
