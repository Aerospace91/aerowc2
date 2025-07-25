import argparse
import regex

def main():

    parser = argparse.ArgumentParser(description="Aero's Version of WC")

    parser.add_argument("filename")
    parser.add_argument("-c", "--bytes", action="store_true", help="Show Byte Count of File")
    parser.add_argument("-l", "--lines", action="store_true", help="Show number of lines in the file")
    parser.add_argument("-w", "--words", action="store_true", help="Show number of words in File")
    parser.add_argument("-m", "--characters", action="store_true", help="Show number of characters in File")

    args = parser.parse_args()

    if args.bytes:
        print(f"{byte_count(args.filename)} {args.filename}")
    elif args.lines:
        print(f"{line_count(args.filename)} {args.filename}")
    elif args.words:
        print(f"{word_count(args.filename)} {args.filename}")
    elif args.characters:
        print(f"{char_count(args.filename)} {args.filename}")
        


def byte_count(filename):
    with open(filename, "rb") as f:
        return len(f.read())

def line_count(filename):
    with open(filename, "r") as f:
        return sum(1 for line in f)

def word_count(filename):
    with open(filename, "r") as f:
        data = f.read()
        return len(data.split())
    
# aerowc shows 332147, WC shows 339292
# Tried Regex, counting specific characters etc..   
def char_count(filename):
    with open(filename, "r", encoding="utf-8", errors="replace") as f:
        return len(f.read())

if __name__ == "__main__":
    main()