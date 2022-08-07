import os
import sys
import shutil


def main():
    try:
        src = input('input source dir name: ')
        des = input('input destination dir name: ')
        rmv = input('remove dirs automatically? (y): ')
        os.makedirs(des, exist_ok=True)
        dirs = os.listdir(src)
        for dir in dirs:
            files = os.listdir(f'{src}/{dir}')
            for file in files:
                shutil.move(f'{src}/{dir}/{file}', des)
            sys.stdout.write(f'\033[2K\033[G {dir} is merged')
            sys.stdout.flush()
            if rmv == 'y':
                os.rmdir(f'{src}/{dir}')
        if rmv == 'y':
            os.rmdir(src)
    except Exception as e:
        print(e)
        exit(1)


if __name__ == '__main__':
    main()
