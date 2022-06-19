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
        obj['data'].append({
            'prefecture': line[0],
            'city': line[1],
            'ward': line[2],
            'others': "{}-{}-{}".format(line[3], line[4], line[5]),
            'zipcode': line[6]
        })
    
    with open('C:/Users/yuki_/python/output/address.json', mode='w', encoding='UTF-8') as file:
        json.dump(obj, file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()