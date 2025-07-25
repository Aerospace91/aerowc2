import argparse
import sys

def main():

    args = parse_args()

    #Check if Input is being Piped
    if not sys.stdin.isatty():
        #If Piped, read from stdin
        content = sys.stdin.read()
        binary_content = content.encode('utf-8') #Convert to Bytes
        filename = "(stdin)"
    
    elif args.filename:
        #If File is provided, read from file
        content = open_file(args.filename)
        binary_content = open_binary_file(args.filename)
        filename = args.filename
    
    else:
        raise Exception("No File or Piped Input Provided")

    result = {
        'length': line_count(content),
        'words': word_count(content),
        'bytes': byte_count(binary_content),
        'chars': char_count(content)
    }

    if args.bytes:
        print(f"{result["bytes"]} {args.filename}")
    elif args.lines:
        print(f"{result["length"]} {args.filename}")
    elif args.words:
        print(f"{result["words"]} {args.filename}")
    elif args.characters:
        print(f"{result["chars"]} {args.filename}")
    else:
        print(f"{result["length"]} {result["words"]} {result["bytes"]} {args.filename}")
        
def parse_args():
    
    parser = argparse.ArgumentParser(
        prog = "Aero WC",
        description="Aero's Version of WC",
        epilog = "Have a nice day!"
    )

    parser.add_argument("filename", type=str, nargs="?", help="File to Process")
    parser.add_argument("-c", "--bytes", action="store_true", help="Show Byte Count of File")
    parser.add_argument("-l", "--lines", action="store_true", help="Show number of lines in the file")
    parser.add_argument("-w", "--words", action="store_true", help="Show number of words in File")
    parser.add_argument("-m", "--characters", action="store_true", help="Show number of characters in File")

    return parser.parse_args()

def open_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()
    
def open_binary_file(filepath):
    with open(filepath, "rb") as f:
        return f.read()

def byte_count(data):
    return len(data)

def line_count(data):
    return data.count('\n')

def word_count(data):
    return len(data.split())
    
# aerowc shows 332147, WC shows 339292
# Tried Regex, counting specific characters etc..   
def char_count(data):
    return len(data)

if __name__ == "__main__":
    main()