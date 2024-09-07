def extract_verse_surah_numbers(verse):
    # Example
    # 1|3|الرَّحْمَـٰنِ الرَّحِيم
    parts = verse.split("|")
    try:
        surah_number = int(parts[0])
        verse_number = int(parts[1])
    except:
        print("None Surah and Verse")
        surah_number = None
        verse_number = None

    return surah_number, verse_number
