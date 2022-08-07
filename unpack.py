import os
import sys
import shutil


def main():
    try:
        dir = input('input dir name: ')
        files = os.listdir(dir)
        for file in files:
            shutil.unpack_archive(f'{dir}/{file}', f'{dir}/out')
            sys.stdout.write(f'\033[2K\033[G {file} is unpacked')
            sys.stdout.flush()
    except Exception as e:
        print(e)
        exit(1)


if __name__ == '__main__':
    main()
