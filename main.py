import pickle
from src.package import Package
from src.rectangle import Rectangle
from src.stack import Stack
from src.sheet import Sheet
from src.part import Part

file_name = "save.bin"

# def place_rectangle(package, sheet_l, sheet_w):
#     result = [Sheet(sheet_l, sheet_w)]
#     count_p = 0
#     count_sh = 0
#     coordinates = [(0, 0)]
#
#     # sorting by width
#     package.sort_square()
#
#     for item in package.pack:
#         for _ in range(item.number):
#             for x, y in coordinates:
#                 if x + item.length <= sheet_l and y + item.width <= sheet_w:
#                     count_p += 1
#                     result[count_sh].add_part(Part(item.rectangle, (x, y), idx=count_p))
#                     item.use()
#                     coordinates.remove((x, y))
#
#                     coordinates.append((x, y + item.width))
#                     coordinates.append((x + item.length, y))
#
#                     print(coordinates)
#                     break
#             else:
#                 result.append(Sheet(sheet_l, sheet_w))
#                 count_sh += 1
#                 result[count_sh].idx = count_sh
#                 count_p = 1
#                 result[count_sh].add_part(Part(item.rectangle, (0, 0), idx=count_p))
#                 item.use()
#                 coordinates = [(0, item.width), (item.length, 0)]
#
#                 print(coordinates)
#     return result


def place_rectangle(package, sheet_l, sheet_w):
    result = [Sheet(sheet_l, sheet_w)]
    count_p = 0
    count_sh = 0
    coordinates = [(0, 0, 0)]

    # sorting by width
    package.sort_square()
    package.sort_width()

    for item in package.pack:
        for _ in range(item.number):
            for x, y, s in coordinates:
                if x + item.length <= sheet_l and y + item.width <= sheet_w:
                    count_p += 1
                    result[count_sh].add_part(Part(item.rectangle, (x, y), idx=count_p))
                    item.use()
                    coordinates.remove((x, y, count_sh))

                    coordinates.append((x, y + item.width, count_sh))
                    coordinates.append((x + item.length, y, count_sh))

                    print(coordinates)
                    break
            else:
                result.append(Sheet(sheet_l, sheet_w))
                count_sh += 1
                result[count_sh].idx = count_sh
                count_p = 1
                result[count_sh].add_part(Part(item.rectangle, (0, 0, count_sh), idx=count_p))
                item.use()
                coordinates.append((0, item.width, count_sh))
                coordinates.append((item.length, 0, count_sh))

                print(coordinates)
    return result


if __name__ == '__main__':
    pack = Package()
    stack1 = Stack(Rectangle(1000, 500), 2)
    stack2 = Stack(Rectangle(500, 1000), 4)
    pack.add_stack(stack1)
    pack.add_stack(stack2)
    # print(pack.show_pack())
    # print([(i.length, i.width) for i in pack.rect_list()])
    # print([i.to_dict() for i in pack.find_stack(1000)])
    # print(pack.square())
    # pack.use_by_idx(2, 2)
    # pack.use_by_idx(1, 2)
    # print(pack.show_pack())
    # print(pack.square())
    # sheet_1 = Sheet(5600, 1240)

    with open(file_name, "wb") as fh:
        pickle.dump(place_rectangle(pack, 2000, 1000), fh)

    with open(file_name, "rb") as fh:
        unpacked = pickle.load(fh)

    print([i.to_list() for i in unpacked])
