import pandas as pd
import json
import math

def main():
    with open('C:/Users/yuki_/python/dataset/formatted_KEN_ALL.CSV', mode='r', encoding='UTF-8') as file:
        df = pd.read_csv(file, dtype='object').fillna('')
        arrays = df.to_numpy(copy=True).tolist()
    
    data = get_json(arrays)

    with open('C:/Users/yuki_/python/output/KEN_ALL.json', mode='w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    with open('C:/Users/yuki_/python/dataset/formatted_JIGYOSYO.CSV', mode='r', encoding='UTF-8') as file:
        df = pd.read_csv(file, dtype='object').fillna('')
        arrays = df.to_numpy(copy=True).tolist()
    
    data = get_json(arrays)

    with open('C:/Users/yuki_/python/output/JIGYOSYO.json', mode='w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def get_json(arrays: list):
    data = []
    for row_i in range(len(arrays)):
        show_progress(row_i, len(arrays))
        data.append({
            'zipcode': arrays[row_i][1],
            'pref': arrays[row_i][2],
            'city': arrays[row_i][3],
            'ward': arrays[row_i][4],
            'others': arrays[row_i][5]
        })
    
    return {'data': data}


def show_progress(i: int, len: int) -> None:
    pro_rate = len / 100
    pro_bar = ('=' * math.floor(i / pro_rate)) + (' ' * math.floor((len - i) / pro_rate))
    print('\r[{0}] {1}%'.format(pro_bar, round(i / len * 100, 2)), end='')
    if i + 1 == len: print('\n', end='')


if __name__ == '__main__':
    main()