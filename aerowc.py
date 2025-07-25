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
        

def open_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()
    
def open_binary_file(filepath):
    with open(filepath, "rb") as f:
        return f.read()

def byte_count(filename):
    data = open_binary_file(filename)
    return len(data)

def line_count(filename):
    data = open_file(filename)
    return data.count('\n')

def word_count(filename):
    data = open_file(filename)
    return len(data.split())
    
# aerowc shows 332147, WC shows 339292
# Tried Regex, counting specific characters etc..   
def char_count(filename):
    data = open_file(filename)
    return len(data)

if __name__ == "__main__":
    main()