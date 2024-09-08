import re
import os
import uuid
import json
import sys

from utils.extract_verse_surah_numbers import extract_verse_surah_numbers
from utils.filter_text import filter_text
from utils.generate_uuid import generate_unique_id
from utils.dump_json_data import dump_json_data

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from core.utils.pymongo_get_database import get_database

dbname = get_database()
quran_words_collection = dbname["quran_words"]


def generate_word_json():
    quran_verses_path = "../../static/text/quran_verses.txt"
    generated_words = []
    with open(quran_verses_path, "r") as quran_file:
        verses = quran_file.readlines()
        line_number = 0
        for verse in verses:
            try:
                surah_number, verse_number = extract_verse_surah_numbers(verse)
                verse_words = filter_text(verse).split()
                for word in verse_words:
                    if word not in generated_words:
                        word_id = generate_unique_id()
                        verse_data = {
                            "word": word,
                            "id": str(word_id),
                            "surah_number": surah_number,
                            "verse_number": verse_number,
                        }
                        # dump_json_data(verse_data)
                        quran_words_collection.insert_one(verse_data)
                        generated_words.append(word)
                    line_number += 1
                    if line_number % 1000 == 0:
                        print(f"Finished generating and saving {line_number} words")
            except Exception as e:
                print(f"Exceptoin: {e}")
                pass


if __name__ == "__main__":
    generate_word_json()
    print("Finished exctracting words and saving to database!")
