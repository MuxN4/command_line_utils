import os
import datetime

def filter_files(files, args): #Filter a list of filenames based on given criteria
    filtered_files = []
    for file in files:
        file_path = os.path.join(args.directory, file)
        if args.extension and not file.endswith(args.extension):
            continue
        if args.size and os.path.getsize(file_path) != args.size:
            continue
        if args.modified:
            mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d')
            if mod_time != args.modified:
                continue
        filtered_files.append(file)   # If file meets all criteria, add to filtered list
    return filtered_files
