import sys
import json


def main():
    try:
        src = input('input file name: ')
        with open(src, mode='r', encoding='UTF-8') as f:
            ctx = json.load(f)
        arr = [
            {
                'coordinate':s['geometry']['coordinates'][len(s['geometry']['coordinates'])//2],
                'name':s['properties']['N02_005']
            }
            for s in ctx['features']
        ]
        name = src.replace('.geojson', '.json')
        with open(name, mode='w', encoding='UTF-8') as f:
            json.dump({'bus_stop': arr}, f, ensure_ascii=False, indent=2)
        sys.stdout.write(f'\033[2K\033[G converted {src}')
        sys.stdout.flush()
    except Exception as e:
        print(e)
        exit(1)


if __name__ == '__main__':
    main()
