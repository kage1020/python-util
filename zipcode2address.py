import pandas as pd


def main():
    print('input zipcode: ', end='')
    zipcode = input()
    get_address(zipcode)


def get_address(zipcode):
    dfNormal = pd.read_csv(
        'C:/Users/yuki_/python/dataset/KEN_ALL.csv', 
        encoding='cp932', 
        names=['areaCode', 'oldZipcode', 'zipcode', 'prefHalf', 'cityHalf', 'wardHalf', 'pref', 'city', 'ward', 'option1', 'option2', 'option3', 'option4', 'option5', 'option6'],
        dtype={'areaCode': 'object', 'oldZipcode': 'object', 'zipcode': 'object', 'prefHalf': 'object', 'cityHalf': 'object', 'wardHalf': 'object', 'pref': 'object', 'city': 'object', 'ward': 'object', 'option1': 'object', 'option2': 'object', 'option3': 'object', 'option4': 'object', 'option5': 'object', 'option6': 'object'}
    )
    dfCompany = pd.read_csv(
        'C:/Users/yuki_/python/dataset/JIGYOSYO.CSV',
        encoding='cp932',
        names=['jis', 'nameHalf', 'name', 'pref', 'city', 'ward', 'others', 'zipcode', 'oldZipcode', 'area', 'option1', 'option2', 'option3'],
        dtype={'jis': 'object', 'nameHalf': 'object', 'name': 'object', 'pref': 'object', 'city': 'object', 'ward': 'object', 'others': 'object', 'zipcode': 'object', 'oldZipcode': 'object', 'area': 'object', 'option1': 'object', 'option2': 'object', 'option3': 'object'}
    )
    rows = dfNormal[dfNormal['zipcode'] == zipcode]

    address = {
        'zipcode': zipcode,
        'results': [],
        'type': 'personal'
    }
    for i in range(len(rows)):
        address['results'].append({
            'prefecture': rows.iat[i, 6],
            'city': rows.iat[i, 7],
            'ward': rows.iat[i, 8]
        })

    if len(address['results']) == 0: 
        rows = dfCompany[dfCompany['zipcode'] == zipcode]

        if len(rows) == 0: address['type'] = 'null'
        else:
            address['type'] = 'company'
            address['results'].append({
                'prefecture': rows.iat[0, 3],
                'city': rows.iat[0, 4],
                'ward': rows.iat[0, 5],
                'others': rows.iat[0, 6]
            })

    print(address)


if __name__ == '__main__':
    main()