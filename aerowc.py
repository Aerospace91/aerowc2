import argparse

def main():

    parser = argparse.ArgumentParser(description="Aero's Version of WC")

    parser.add_argument("filename")
    parser.add_argument("-c", "--bytes", action="store_true", help="Show Byte Count of File")

    args = parser.parse_args()

    with open(args.filename, "rb") as f:
        data = f.read()

    if args.bytes:
        print(f"{byte_count(data)} {args.filename}")
        


def byte_count(data):
    return len(data)



if __name__ == "__main__":
    main()