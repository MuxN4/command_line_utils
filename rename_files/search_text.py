import argparse
import os
import logging
from utils import validate_directory
from filters import filter_files

def parse_arguments():
    parser = argparse.ArgumentParser(description='Search for a text pattern in files within a specified directory.')
    parser.add_argument('directory', type=str, help='Directory to search files in')
    parser.add_argument('--pattern', type=str, required=True, help='Text pattern to search for')
    parser.add_argument('--extension', type=str, help='Filter files by extension')
    parser.add_argument('--size', type=int, help='Filter files by size (in bytes)')
    parser.add_argument('--modified', type=str, help='Filter files by last modification date (YYYY-MM-DD)')
    return parser.parse_args()

def main():
    args = parse_arguments()
    if not validate_directory(args.directory):
        logging.error(f"Invalid directory: {args.directory}")
        return
    
    files = os.listdir(args.directory)
    files = filter_files(files, args)

    for file in files:
        file_path = os.path.join(args.directory, file)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                contents = f.read()
                if args.pattern in contents:
                    logging.info(f"Pattern found in {file_path}")
        except Exception as e:
            logging.error(f"Error reading {file_path}: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
