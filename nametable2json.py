import json


def main():
    lines = []
    obj = {'data': []}
    print('input table')
    while True:
        val = list(map(str, input().split()))
        if val:
            lines.append(val)
        else:
            break
    
    for line in lines:
        obj['data'].append({'last':line[0], 'first':line[1], 'lastRuby':line[2], 'firstRuby':line[3]})
    
    with open('C:/Users/yuki_/python/output/name.json', mode='w', encoding='UTF-8') as file:
        json.dump(obj, file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()