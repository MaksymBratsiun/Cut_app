from PIL import Image, ImageDraw, ImageFont

file_name = "res.pdf"
# TITLE = "Title"
A4_pix = (1169, 827)
A4_real = (297, 210)
MAIN_LINE = 2
THIN_LINE = 1

MAIN_FRAME_MARGIN = (20, 5, 5, 5)  #mm; left, top, right, bottom; rect draws from left-top to right-bottom points
DRAWING_MARGIN = 10  # mm

m = round((A4_real[0] / A4_pix[0]), 5)  #scale

main_frame_coord = (round(MAIN_FRAME_MARGIN[0] / m),
                    round(MAIN_FRAME_MARGIN[1] / m),
                    round((A4_real[0] - MAIN_FRAME_MARGIN[2]) / m),
                    round((A4_real[1] - MAIN_FRAME_MARGIN[3]) / m))


class Item:
    def __init__(self, idx, height, width):
        self.idx = idx
        self.height = height
        self.width = width
        self.coordinates = None  # (sheet, x, y)


class Sheet:

    def __init__(self, idx, height, width):
        self.idx = idx
        self.height = height
        self.width = width
        self.items = []
        self.items_count = 0

    def add_item(self, item_):
        self.items_count += 1
        self.items.append(item_)


class Package:
    def __init__(self, name):
        self.name = name
        self.sheets_count = 0
        self.items_count = 0
        self.sheets = []

    def add_sheet(self, sheet_):
        self.sheets_count += 1
        self.items_count += sheet_.items_count
        self.sheets.append(sheet_)


def real_to_pix(real, m_):
    return round(real / m_)


def scale_calc(sheet_):
    scale_w = (sheet_.width / (A4_pix[0] - real_to_pix(MAIN_FRAME_MARGIN[0]+MAIN_FRAME_MARGIN[2]+2*DRAWING_MARGIN, m)))
    scale_h = (sheet_.height / (A4_pix[1] - real_to_pix(MAIN_FRAME_MARGIN[1]+MAIN_FRAME_MARGIN[3]+2*DRAWING_MARGIN, m)))
    return max([scale_w, scale_h])


def get_framed_image():
    image_ = Image.new("RGB", A4_pix, "white")
    drawing = ImageDraw.Draw(image_)
    drawing.rectangle(main_frame_coord, fill=None, outline="black", width=MAIN_LINE)
    return image_, drawing


def draw_sheet(drawing, sheet_inner, start_coord):
    scale = scale_calc(sheet_inner)
    x_end_sheet_pix = start_coord[0] + real_to_pix(sheet_inner.width, scale)
    height_sheet_pix = real_to_pix(sheet_inner.height, scale)
    y_end_sheet_pix = start_coord[1] + height_sheet_pix

    sheet_coord = start_coord[0], start_coord[1], x_end_sheet_pix, y_end_sheet_pix
    drawing.rectangle(sheet_coord, fill=None, outline="red", width=MAIN_LINE)

    for item_inner in sheet_inner.items:
        drawing = draw_item(drawing, item_inner, scale, start_coord)

    return drawing, sheet_inner, scale, y_end_sheet_pix


def draw_item(drawing, item_, scale, starts_coord):
    start_item_pix = (starts_coord[0] + real_to_pix(item_.coordinates[1], scale),
                      starts_coord[1] + real_to_pix(item_.coordinates[2], scale))
    x_end_item_pix = start_item_pix[0] + real_to_pix(item_.width, scale)
    y_end_item_pix = start_item_pix[1] + real_to_pix(item_.height, scale)
    item_coord = start_item_pix[0], start_item_pix[1], x_end_item_pix, y_end_item_pix
    drawing.rectangle(item_coord, fill=None, outline="blue", width=MAIN_LINE)
    return drawing


def draw_title(drawing, title):
    font = ImageFont.truetype("arial.ttf", 40)
    text_bbox = drawing.textbbox((0, 0), title, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_x = (A4_pix[0] - text_width) // 2
    text_y = (A4_pix[1] - text_height) // 2
    drawing.text((text_x, text_y), title, fill="black", font=font)
    return drawing


def pack_saving(output_path, pack):
    images = []

    # Title
    image, draw = get_framed_image()

    draw = draw_title(draw, pack.name)
    images.append(image)

    # New page
    image, draw = get_framed_image()
    start_sheet_pix = (main_frame_coord[0] + real_to_pix(DRAWING_MARGIN, m),
                       main_frame_coord[1] + real_to_pix(DRAWING_MARGIN, m))
    scale = None
    # Next page
    for sheet_next in pack.sheets:
        if scale is None:
            scale = scale_calc(sheet_next)
        out_of_range = start_sheet_pix[1] + MAIN_FRAME_MARGIN[3]+real_to_pix(sheet_next.height, scale)

        if out_of_range > main_frame_coord[3]:
            images.append(image)
            image, draw = get_framed_image()
            start_sheet_pix = (main_frame_coord[0] + real_to_pix(DRAWING_MARGIN, m),
                               main_frame_coord[1] + real_to_pix(DRAWING_MARGIN, m))
            draw, sheet_next, scale, y_end_sheet_pix = draw_sheet(draw, sheet_next, start_sheet_pix)
            start_sheet_pix = (start_sheet_pix[0],
                               y_end_sheet_pix + real_to_pix(DRAWING_MARGIN, m))
        else:
            draw, sheet_next, scale, y_end_sheet_pix = draw_sheet(draw, sheet_next, start_sheet_pix)
            start_sheet_pix = (start_sheet_pix[0],
                               y_end_sheet_pix + real_to_pix(DRAWING_MARGIN, m))

    images.append(image)
    images[0].save(output_path, save_all=True, append_images=images[1:])


if __name__ == '__main__':

    item = Item(1, 100, 750)
    item.coordinates = (1, 0, 0)
    item2 = Item(1, 100, 500)
    item2.coordinates = (1, 0, 100)
    sheet = Sheet(1, 220, 1000)
    sheet.add_item(item)
    sheet.add_item(item2)
    package = Package('New Title')
    for _ in range(2):
        package.add_sheet(sheet)

    print(item.__dict__)
    print(sheet.__dict__)
    print(package.__dict__)
    pack_saving(file_name, package)
