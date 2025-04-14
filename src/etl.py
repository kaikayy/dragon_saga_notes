import os
import logging
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.parent
SOURCE_DIR = f"{SCRIPT_DIR}/data"


def sort_files(files: list[str]) -> list[str]:

    def parse_session_num(file: str):
        name = os.path.basename(file)
        session_num = name.split(" ")[1].split(".")[0]
        return int(session_num)

    return sorted(files, key=parse_session_num)


def get_files() -> list[str]:
    files = [
        f for f in os.listdir(SOURCE_DIR)
        if os.path.isfile(os.path.join(SOURCE_DIR, f)) and "Session" in f
        # when encountering first instance of combat ref file -> append combat file
    ]

    logging.warning(f"Found files {len(files)} - {files}")
    return sort_files(files)



def read_files() -> list[str]:

    files = get_files()
    lines = []
    for f in files:
        file_path = os.path.join(SOURCE_DIR, f)
        with open(file_path, 'r') as ll:
            for line in ll:
                lines.append(line.strip())

    return lines


def parse_roll_df():
    pass

def parse_status_df():
    pass


# character; roll result; roll type



def main():
    lines = read_files()
    print(len(lines)) 

    df = parse_roll_df()


if __name__ == "__main__":
    main()
