import sys
import glob
import json


def main():
    try:
        src = input('input source dir name: ')
        des = input('input destination dir name: ')
        attr = input('input attribute name for bus stop name: ')
        files = glob.glob(f'{src}/*.geojson')
        for file in files:
            with open(file, mode='r', encoding='UTF-8') as f:
                ctx = json.load(f)
            arr = [{'coordinate':s['geometry']['coordinates'],'name':s['properties'][attr]} for s in ctx['features']]
            name = file.replace(src, des).replace('.geojson', '.json')
            with open(name, mode='w', encoding='UTF-8') as f:
                json.dump({'bus_stop': arr}, f, ensure_ascii=False, indent=2)
            sys.stdout.write(f'\033[2K\033[G converted {file}')
            sys.stdout.flush()
    except Exception as e:
        print(e)
        exit(1)


if __name__ == '__main__':
    main()
