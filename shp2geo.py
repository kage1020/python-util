import sys
import glob
import shapefile as shp
import json


def main():
    try:
        src = input('input source dir name: ')
        des = input('input destination name: ')
        files = glob.glob(f'{src}/*.shp')
        for file in files:
            sf = shp.Reader(file, encoding='cp932')
            fields = sf.fields[1:]
            names = [field[0] for field in fields]
            buffer = []
            for record in sf.shapeRecords():
                atr = dict(zip(names, record.record))
                geom = record.shape.__geo_interface__
                buffer.append(dict(type='Feature', geometry=geom, properties=atr))
            name = file.replace('.shp', '.geojson').replace(f'{src}\\', '')
            with open(f'{des}/{name}', mode='w', encoding='UTF-8') as f:
                json.dump({'type': 'FeatureCollection', 'features': buffer}, f, indent=2, ensure_ascii=False)
            sys.stdout.write(f'\033[2K\033[G converted to {name}')
            sys.stdout.flush()
    except Exception as e:
        print(e)
        exit(1)


if __name__ == '__main__':
    main()
