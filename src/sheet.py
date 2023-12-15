class Sheet:
    def __init__(self, length, width):
        self.idx = 0
        self.length = length
        self.width = width
        self.parts = []
        self.start_points = [(0, 0)]
        self.n_parts = len(self.parts)

    def square(self):
        return self.length * self.width

    # def used_square(self):
    #     return self.length * self.width
    #
    # def left(self):
    #     return self.length * self.width

    def add_part(self, part):
        self.parts.append(part)

    def remove_start_point(self, start_p):
        self.start_points.remove(start_p)

    def get_start_points(self):
        return self.start_points

    def add_start_point(self, start_p):
        if type(start_p) == list:
            self.start_points.extend(start_p)
        elif type(start_p) == tuple:
            self.start_points.append(start_p)

    def to_list(self):
        res = []
        for item in self.parts:
            res.append(
                {
                    "idx": item.idx,
                    "rectangle": (item.rectangle.length, item.rectangle.width),
                    "start": item.start_coordinates
                }
            )
        return res
