import os
from PIL import Image, ImageDraw


def textsize(text, font):
    im = Image.new(mode="P", size=(0, 0))
    draw = ImageDraw.Draw(im)
    _, _, width, height = draw.textbbox((0, 0), text=text, font=font)
    return width, height


def generate_image(text, id, font_object, font, width=192, height=64, text_y_offset=0):
    img = Image.new("RGB", (width, height), color="black")

    imgDraw = ImageDraw.Draw(img)

    text_width, text_height = textsize(text, font_object)

    x = (width - text_width) / 2
    y = (height - text_height) / 2 + text_y_offset

    imgDraw.text((x, y), text, font=font_object, fill="white")

    folder_path = f"../../static/processed/v2/images/{font}/"
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    save_path = os.path.join(folder_path, f"{id}.png")
    img.save(save_path)
