import os
import argparse

def count_files(folder_path):
    files = os.listdir(folder_path)
    nmb_files = 0
    for file in files:
        nmb_files += 1

    return nmb_files

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count the number of files in a given folder.")
    parser.add_argument("folder_path", type=str, help="The path to the folder to count files in.")
    args = parser.parse_args()

    folder_path = args.folder_path
    number_of_files = count_files(folder_path)

    print(f"The number of files in '{folder_path}' is: {number_of_files}")
