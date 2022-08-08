import json


def main():
    point = input('input Airport file name: ')
    ref = input('input AirportReference name: ')
    with open(point, mode='r', encoding='UTF-8') as f:
        points = json.load(f)
    with open(ref, mode='r', encoding='UTF-8') as f:
        refs = json.load(f)
    ref_map = {p['properties']['C28_000']:p['geometry']['coordinates'] for p in refs['features']}
    arr = [
        {'coordinate':ref_map[p['properties']['C28_101'].replace('#','')],'name':p['properties']['C28_005']}
        for p in points['features']
    ]
    arr = list(map(json.loads, set(map(json.dumps, arr))))
    # https://qiita.com/kilo7998/items/184ed972571b2e202b40
    name = point.replace('.geojson', '.json')
    with open(name, mode='w', encoding='UTF-8') as f:
        json.dump({'airport': arr}, f, ensure_ascii=False, indent=2)



if __name__ == '__main__':
    main()
