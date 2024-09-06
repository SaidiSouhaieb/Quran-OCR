import json


def dump_json_data(data):
    json_file_path = "temp/quran_words.json"
    with open(json_file_path) as fp:
        words = json.load(fp)

    words.append(data)
    json_object = json.dumps(
        words, indent=4, ensure_ascii=False, separators=(",", ": ")
    )
    with open(json_file_path, "w") as outfile:
        outfile.write(json_object)
