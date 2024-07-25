import argparse
import os
import shutil
import logging
from utils import validate_directory
from filters import filter_files
from logging_config import setup_logging

def parse_arguments():
    parser = argparse.ArgumentParser(description='Rename files in a specified directory based on given patterns.')
    parser.add_argument('directory', type=str, help='Directory where files to rename are located')
    parser.add_argument('--pattern', type=str, required=True, help='Renaming pattern')
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

    for i, file in enumerate(files):
        src = os.path.join(args.directory, file)
        dst = os.path.join(args.directory, args.pattern.format(i=i, original=file))
        try:
            shutil.move(src, dst)
            logging.info(f"Renamed {src} to {dst}")
        except Exception as e:
            logging.error(f"Error renaming {src} to {dst}: {e}")

if __name__ == "__main__":
    setup_logging()
    main()
