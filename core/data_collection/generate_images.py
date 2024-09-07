import csv
import os
import sys

from PIL import ImageFont
from utils.generate_image import generate_image

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from core.utils.pymongo_get_database import get_database

dbname = get_database()
quran_words_collection = dbname["quran_words"]
quran_words = quran_words_collection.find()


def generate_images():
    font_names = ["eljaza", "hijazi", "naskh", "ruqah", "thuluth"]
    number_words_generated = 0
    for font in font_names:
        print(font)
        # try:
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
            # print(f"Finished generating {number_words_generated} words!")
            number_words_generated += 1
        print(f"Finished generating words with font {font}")
        quran_words.rewind()
        # except Exception as e:
        #     print(f"Exception: {e}")
        #     pass


if __name__ == "__main__":
    generate_images()
    print("Finished generating images with all fonts!")
