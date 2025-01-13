import argparse
import os
import shutil
import sys


def main():
    """
    main function
    :return: None
    """
    parser = argparse.ArgumentParser(description='Simple Example')

    # Add some arguments
    parser.add_argument('-f', '--folder', help='the folder with the files to rename')
    parser.add_argument('-o', '--old', help='the old string to replace')
    parser.add_argument('-n', '--new', action='append', help='the new_list string to replace with')
    args = parser.parse_args()
    if args.folder is None or args.old is None or args.new is None:
        print('Usage: rename_files.py -f <folder> -o <old> -n <new> [-n <new_list> ...]')
        sys.exit(1)

    copy_files(args.folder, args.old, args.new)
    edit_config_files(args.folder, args.old, args.new)

def copy_files(folder, old_name, new_list):
    """
    Copy the files
    :param: folder -- the folder with the files to rename
    :param: old_name -- the old string to replace
    :param: new_list -- the new_list string to replace with
    :return: None
    """
    for filename in os.listdir(folder):
        if old_name in filename:
            for new_name in new_list:
                new_filename = filename.replace(old_name, new_name)
                print(f'Copying {filename} to {new_filename}')
                shutil.copy(f'{folder}/{filename}', f'{folder}/{new_filename}')

            # remove the original file
            os.remove(f'{folder}/{filename}')

def edit_config_files(folder, old_name, new_list):
    """
    Edit the config files
    :param: folder -- the folder with the files to rename
    :param: old_name -- the old string to replace
    :param: new_list -- the new_list string to replace with
    :return: None
    """
    for new_name in new_list:
        with open(f'{folder}/{new_name}_master.txt') as f:
            old_config = f.read()
            new_config = old_config.replace(old_name, new_name)

    with open(f'{folder}/{new_name}_master.txt', 'w') as f:
        f.write(new_config)

if __name__ == '__main__':
    main()
