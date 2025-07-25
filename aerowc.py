import argparse

def main():

    parser = argparse.ArgumentParser(description="Aero's Version of WC")

    parser.add_argument("filename")
    parser.add_argument("-c", "--bytes", action="store_true", help="Show Byte Count of File")
    parser.add_argument("-l", "--lines", action="store_true", help="Show number of lines in the file")

    args = parser.parse_args()

    if args.bytes:
        print(f"{byte_count(args.filename)} {args.filename}")
    elif args.lines:
        print(f"{line_count(args.filename)} {args.filename}")
        


def byte_count(filename):
    with open(filename, "rb") as f:
        return len(f.read())

def line_count(filename):
    with open(filename, "r") as f:
        return sum(1 for line in f)

if __name__ == "__main__":
    main()