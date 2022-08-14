#!/usr/bin/env python3
import sys
import re
from typing import Optional, List, Callable


class Buffer:
    values: List[str]

    def __init__(self) -> None:
        self.values = []

    def append(self, value: str) -> None:
        self.values.append(value)

    def reset(self) -> None:
        self.values = []

    def flush(self, flush_line: Callable[[str], None], flag: bool) -> None:
        if flag:
            for line in self.values:
                flush_line(line)
        self.reset()


class bcolors:
    HEADER = "\033[95m"
    SUBHEADER = "\033[33m"
    BOLD = "\033[1m"
    PLACEHOLDER = "\033[3m"
    ENDC = "\033[0m"


def format_placeholder(text: str) -> str:
    return re.sub("{(.+?)}", bcolors.PLACEHOLDER + r"{\1}" + bcolors.ENDC, text)
    

def print_header(text: str) -> None:
    print(f"{bcolors.HEADER}{text}{bcolors.ENDC}", end="")
    return


def print_sub_header(text: str) -> None:
    print(f"{bcolors.SUBHEADER}{text}{bcolors.ENDC}", end="")
    return


def is_mark(text: str) -> bool:
    return text.startswith("@") or text.startswith("=")


def parse_print_text(text: str) -> None:
    if text.startswith("@"):
        print_header(text[1:])
    elif text.startswith("="):
        print_sub_header(text[1:])
    else:
        print(text, end="")
    return


def run_help(filename: str, match: Optional[str], isGrep: bool) -> None:
    use_buffer: bool = False if match is None else True
    found_match: bool = False
    buffer = Buffer()
    with open(filename) as file:
        for raw_line in file:
            line = format_placeholder(text=raw_line)
            if isGrep:
                if match is not None and match in line:
                    parse_print_text(line)
            elif use_buffer:
                if match is not None and match in line:
                    found_match = True
                if is_mark(text=line):
                    buffer.flush(flush_line=parse_print_text, flag=found_match)
                    found_match = False
                buffer.append(line)
            else:
                parse_print_text(line)
    buffer.flush(flush_line=parse_print_text, flag=found_match)
    return


if __name__ == "__main__":
    num_args: int = len(sys.argv)
    filename: str = ""
    match: Optional[str] = None
    isGrep: bool = False
    if num_args < 2:
        print("Please provide a file")
    elif num_args == 2:
        filename = sys.argv[1]
    else:
        filename = sys.argv[1]
        match = " ".join(sys.argv[2:])
        if num_args > 3 and sys.argv[-1] == "1":
            isGrep = True
            match = " ".join(sys.argv[2:-1])
    run_help(filename=filename, match=match, isGrep=isGrep)
