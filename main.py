import math
import pickle


class Rectangle:
    def __init__(self, length, width, n, r=False):
        self.idx = 1
        self.length = length
        self.width = width
        self.number = n
        self.rotate = r

    def square_one(self):
        return self.length * self.width

    def square_all(self):
        return self.length * self.width * self.number

    def use(self, n_use=1, verbose=False):
        if (self.number - n_use) >= 0:
            self.number -= n_use
            if self.number <= 0:
                return 0

        if verbose:
            return self.number

    def left(self):
        return self.number

    def set_idx(self, idx):
        self.idx = idx

    def to_dict(self):
        return {
            "idx": self.idx,
            "length": self.length,
            "width": self.width,
            "n": self.number,
            "rotate": self.rotate
        }


class Package:
    def __init__(self):
        self.idx_count = 0
        self.pack = []

    def add_rect(self, item):
        self.idx_count += 1
        item.set_idx(self.idx_count)
        self.pack.append(item)

    def remove_rect(self, idx):
        for item in self.pack:
            if item.idx == idx:
                self.pack.remove(item)

    def show_pack(self):
        return [i.to_dict() for i in self.pack]

    def find_rect(self, first_d, second_d=None):
        res = []
        for item in self.pack:
            if item.length == first_d:
                if not second_d:
                    res.append(item)
                elif item.width == second_d:
                    res.append(item)
            elif item.width == first_d:
                if not second_d:
                    res.append(item)
                elif item.length == second_d:
                    res.append(item)
        return res

    def get_by_idx(self, idx: int) -> Rectangle:
        for item in self.pack:
            if item.idx == idx:
                return item

    def use_by_idx(self, idx, n_use=1):
        for item in self.pack:
            if item.idx == idx:
                item.use(n_use)
                if item.number == 0:
                    print(f"idx={item.idx} removed: n=0")
                    self.pack.remove(item)

    def square(self):
        res = 0
        for item in self.pack:
            res += item.square_all()
        return res


class Sheet:
    def __init__(self, length, width):
        self.length = length
        self.width = width


if __name__ == '__main__':
    pack = Package()
    rec1 = Rectangle(1000, 250, 2)
    rec2 = Rectangle(1000, 500, 2)
    pack.add_rect(rec1)
    pack.add_rect(rec2)
    print(pack.show_pack())
    print([i.to_dict() for i in pack.find_rect(250)])
    print(pack.square())
    pack.use_by_idx(2, 2)
    pack.use_by_idx(1, 2)
    print(pack.show_pack())
    print(pack.square())
