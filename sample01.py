import argparse

def count_lines(filename, verbose=False):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            if verbose:
                print(f"Counting lines in {filename}...")
            return len(lines)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

def main():
    parser = argparse.ArgumentParser(description="Count lines in a file.")
    parser.add_argument("filename", type=str, help="File to count lines in")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")

    args = parser.parse_args()
    num_lines = count_lines(args.filename, args.verbose)

    if num_lines is not None:
        print(f"Total lines: {num_lines}")

if __name__ == "__main__":
    main()
