def extract_verse_surah_numbers(verse):
    # Example
    # 1|3|الرَّحْمَـٰنِ الرَّحِيم
    parts = verse.split("|")
    surah_number = int(parts[0])
    verse_number = int(parts[1])

    return surah_number, verse_number
