import json


def main():
    point = input('input Airport file name: ')
    ref = input('input AirportReference name: ')
    with open(point, mode='r', encoding='UTF-8') as f:
        points = json.load(f)
    with open(ref, mode='r', encoding='UTF-8') as f:
        refs = json.load(f)
    ref_map = { p['properties']['C28_000']:p['geometry']['coordinates'] for p in refs['features'] }
    points = { 
        p['properties']['C28_005']: ref_map[p['properties']['C28_101'].replace('#','')]
        for p in points['features']
    }
    name = point.replace('.geojson', '.json')
    with open(name, mode='w', encoding='UTF-8') as f:
        json.dump({'points': points}, f, ensure_ascii=False, indent=2)



if __name__ == '__main__':
    main()
