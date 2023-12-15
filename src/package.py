class Package:
    def __init__(self):
        self.idx_count = 0
        self.pack = []

    def add_stack(self, stack):
        self.idx_count += 1
        stack.set_idx(self.idx_count)
        self.pack.append(stack)

    def remove_stack(self, idx):
        for item in self.pack:
            if item.idx == idx:
                self.pack.remove(item)

    def show_pack(self):
        return [i.to_dict() for i in self.pack]

    def find_stack(self, first_d, second_d=None):
        res = []
        for item in self.pack:
            if item.rectangle.length == first_d:
                if not second_d:
                    res.append(item)
                elif item.rectangle.width == second_d:
                    res.append(item)
            elif item.rectangle.width == first_d:
                if not second_d:
                    res.append(item)
                elif item.rectangle.length == second_d:
                    res.append(item)
        return res

    def get_by_idx(self, idx: int):
        for item in self.pack:
            if item.idx == idx:
                return item

    def use_by_idx(self, idx, n_use=1):
        for item in self.pack:
            if item.idx == idx:
                item.use(n_use)
                if item.number == 0:
                    print(f"idx:{item.idx} removed: n=0")
                    self.pack.remove(item)

    def square(self):
        res = 0
        for item in self.pack:
            res += item.square()
        return res

    def rect_list(self):
        res = []
        for item in self.pack:
            res.append(item.rectangle)
        return res

    def sort_width(self):
        self.pack.sort(key=lambda st: st.width, reverse=True)

    def sort_square(self):
        self.pack.sort(key=lambda st: st.width * st.length, reverse=True)
