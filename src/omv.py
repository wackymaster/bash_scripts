#!/usr/bin/env python3
import os, shutil, sys


def move_file(filename: str, destination: str):
    shutil.move(src=filename, dst=os.path.join(destination, filename))
    return


def create_prompt(directory: str) -> str:
    print("\033[95m---  Contents --- \033[0m")
    dir_numbering = {}
    index = 0
    for _, content, _ in os.walk(directory):
        for folder in content:
            folder_path = os.path.join(directory, folder)
            if not os.path.isdir(folder_path):
                continue
            print(f"({index}) {folder}")
            dir_numbering[index] = folder_path
            index += 1
        break
    
    print("\033[33m-- Other options --\033[0m")
    print("(u) Go up a directory")
    print("(q) Quit")
    print(f"(.) move to here ({directory})")
    option = input("\033[1mWhere to move file to?: \033[0m")

    if option == "q":
        sys.exit(1)
    elif option == ".":
        return directory
    elif option == "u":
        destination = create_prompt(directory=os.path.dirname(directory))
        return destination
    else:
        option = int(option)
        chosen_directory = dir_numbering[option]
        # Repeat/recurse until user quits or hits enter
        destination = create_prompt(directory=chosen_directory)
        return destination


def main():
    if len(sys.argv) < 3:
        print("Please supply file to move")
    else:
        directory = sys.argv[1]
        for file in sys.argv[2:]:
            destination = create_prompt(directory)
            move_file(filename=file, destination=destination)


if __name__ == "__main__":
    main()
