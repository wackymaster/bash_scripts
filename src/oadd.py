#!/usr/bin/env python3
import os, shutil, sys

def move_file(filename: str, destination: str):
    shutil.move(src=filename, dst=os.path.join(destination, filename))
    return


def create_prompt(directory: str) -> str:
    dir_numbering = {}
    index = 0
    for _, folders, _ in os.walk(directory):
        for folder in folders:
            folder_path = os.path.join(directory, folder)
            print(f"({index}) {folder}")
            dir_numbering[index] = folder_path
            index += 1
        break
    print("(q) Quit")
    option = input("Where to move file to?: ")

    if option == "q":
        sys.exit(1)
    option = int(option)
    destination = dir_numbering[option]
    return destination


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Please supply file to move")
    else:
        directory = sys.argv[1]
        for file in sys.argv[2:]:
            destination = create_prompt(directory)
            move_file(filename=file, destination=destination)
