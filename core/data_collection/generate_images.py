import csv
from PIL import ImageFont
from utils.generate_image import generate_image
from utils.pymongo_get_database import get_database

dbname = get_database()
quran_words_collection = dbname["quran_words"]
quran_words = quran_words_collection.find()


def generate_images():
    font_names = ["eljaza", "hijazi", "naskh", "ruqah", "thuluth"]
    for font in font_names:
        font_path = f"../../static/raw/fonts/{font}.ttf"
        csv_file_path = "../../static/csv/words_id.csv"
        font_size = 35
        font_object = ImageFont.truetype(font_path, size=font_size)

        with open(csv_file_path, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            field = ["word_id"]
            writer.writerow(field)

        for word in quran_words:
            text = word["word"]
            word_id = word["id"]
            with open(csv_file_path, "a", newline="") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([word_id])

            generate_image(text, word_id, font_object, font, text_y_offset=-4)
