import pandas as pd
import jaconv
import re
import math


def main():
    format_file('KEN_ALL.CSV')
    format_file('JIGYOSYO.CSV')


def format_file(filename: str) -> None:
    with open('C:/Users/yuki_/python/dataset/' + filename, mode='r', encoding='cp932') as file:
        df = pd.read_csv(file, dtype='object', header=None).fillna('')
        data = df.to_numpy(copy=True).tolist()
    
    print(filename + ' is successfully opened!')
    
    new_data = []
    if filename == 'KEN_ALL.CSV':
        for row_i in range(len(data)):
            show_progress(row_i, len(data))
            if data[row_i][8].endswith('、') or data[row_i][8].count('（') - data[row_i][8].count('）') != 0:
                data[row_i + 1][8] = data[row_i][8] + data[row_i + 1][8]
                data[row_i][8] = ''
                continue
            else:
                data[row_i][8] = format_str(data[row_i][8], 'z2h')
                data[row_i][8] = replace_data(data[row_i][8])
                new_row = format_row(data[row_i])


            for i in range(len(new_row)):
                new_data.append(new_row[i])
    else:
        for row_i in range(len(data)):
            show_progress(row_i, len(data))
            data[row_i][5] = format_str(data[row_i][5], 'z2h')
            data[row_i][6] = format_str(data[row_i][6], 'z2h')
            
            new_data.append([data[row_i][7], data[row_i][3], data[row_i][4], data[row_i][5], data[row_i][6]])

    new_data = list(map(list, set(map(tuple, new_data))))
    new_data = sorted(new_data, key=lambda x: x[0])
    new_df = pd.DataFrame(new_data).to_csv('C:/Users/yuki_/python/output/formatted_' + filename, encoding='UTF-8', quoting=1)
    # np.savetxt('C:/Users/yuki_/python/output/' + filename, new_data, delimiter=',')
    print(filename + ' is successfully saved!')


def format_str(address: str, format: str) -> str:
    if format == 'h2z':
        address = jaconv.h2z(address)
    elif format == 'z2h':
        address = jaconv.z2h(address, kana=False, digit=True, ascii=True)
    return address


def format_row(row: list) -> list:
    new_row = row

    if '、' in row[8]:
        new_row = get_multiple_rows(row)
    else:
        new_row = [[row[2], row[6], row[7], row[8], '']]

    for row_i in range(len(new_row)):
        new_row[row_i][3] = re.sub(r'\(|\)', '', new_row[row_i][3])

    return new_row

def replace_data(text: str) -> str:
    if text == '以下に掲載がない場合' or '地割' in text: return ''
    if text == '一円': return text
    text = re.sub(r'\(([0-9]+階)\)', r' \1', text)
    text = re.sub(r'\(.+\)|の次に番地がくる場合|一円', '', text)
    return text


def get_multiple_rows(row: list) -> list:
    areas = row[8].split('、')
    new_rows = []
    for i in range(len(areas)):
        new_rows.append([row[2], row[6], row[7], areas[i], ''])
    return new_rows


def show_progress(i: int, len: int) -> None:
    pro_rate = len / 100
    pro_bar = ('=' * math.floor(i / pro_rate)) + (' ' * math.floor((len - i) / pro_rate))
    print('\r[{0}] {1}%'.format(pro_bar, round(i / len * 100, 2)), end='')
    if i + 1 == len: print('\n', end='')


if __name__ == '__main__':
    main()