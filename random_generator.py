import json
import random
from datetime import datetime, timedelta
import re
import kana2initial


def get_user_input():
    print('input data type')
    print('0: patients data  1: institutions data')
    type = input()
    print('input data num')
    num = int(input())
    return [type, num]


def main():
    [type, num] = get_user_input()
    if type == '0':
        get_patient_data(num)
    elif type == '1':
        get_institution_data(num)


def get_patient_data(num):
    patients = []
    replies = ['至急', '1週間', 'なし']
    cares = ['要支援 1', '要支援 2', '要介護 1', '要介護 2', '要介護 3', '要介護 4', '要介護 5']
    care_rate = ['1割', '2割', '3割', '全額']
    food = ['普通', '少ない', '摂取困難', '普通食', 'トロミ食', '半固形']
    toilet = ['トイレ', 'ポータブルトイレ', '尿器', 'オムツ', '自立', '一部介助', '全介助']
    talking = ['可能', '簡単な会話可能', '不可能']
    families = ['内科','神経内科','呼吸器科','呼吸器内科','消化器科','消化器内科','胃腸科','腎臓内科','循環器科','漢方内科','心療内科','老年心療内科','アレルギー科','小児科','心臓小児科','皮膚科','小児皮膚科','精神科','神経科','児童精神科','老年精神科','外科','小児外科','肛門科','整形外科','リウマチ科','産婦人科','産科','婦人科','眼科','耳鼻咽喉（いんこう）科','気管食道科','泌尿器科','性病科','脳外科','放射線科','麻酔科','ペインクリニック内科','形成外科','リハビリテーション科']
    home = ['自宅', '入院', '施設']
    family_type = ['同居', '独居', '日中独居']
    for i in range(num):
        gender = 'male' if random.randint(0, 1) == 0 else 'female'
        patients.append({
            'id':i + 1,
            'register': get_random_date('2020/01/01', '2025/12/31').strftime('%Y/%m/%d'),
            'name': get_random_name(gender),
            'gender': gender,
            'birthday': get_random_date('1900/01/01', '2025/12/31').strftime('%Y/%m/%d'),
            'age': random.randint(0, 150),
            'address': get_random_address(),
            'tel': str(random.randint(10000000000, 99999999999)),
            'diseaseName': get_random_disease(),
            'replyDate': replies[random.randint(0, 2)],
            'hasDementia': '有' if random.randint(0, 1) == 0 else '無',
            'careInsurance': cares[random.randint(0, 6)],
            'careInsuranceRate': care_rate[random.randint(0, 3)],
            'treatments': get_random_treatments('公開'),
            'food': {
                'volume': food[random.randint(0, 2)],
                'type': food[random.randint(3, 5)],
                'limit': '有' if random.randint(0, 1) == 0 else '無',
                'num': random.randint(1000, 2000)
            },
            'toilet': {
                'day': {
                    'type': toilet[random.randint(0, 3)],
                    'help': toilet[random.randint(4, 6)]
                },
                'night': {
                    'type': toilet[random.randint(0, 3)],
                    'help': toilet[random.randint(4, 6)]
                }
            },
            'ADL': toilet[random.randint(4, 6)],
            'talking': talking[random.randint(0, 2)],
            'symptoms': get_random_symptom(),
            'doctor': {
                'primary': {
                    'name': get_random_name('male' if random.randint(0, 1) == 0 else 'female'),
                    'family': families[random.randint(0, len(families) - 1)],
                    'IC': ['私はその人を常に先生と呼んでいた。だから此処でもただ先生と書くだけで本名は打ち明けない。これは世間を憚かる遠慮というよりも、その方が私に取って自然だからである。私はその人の記憶を呼び起すごとに、すぐ「先生」と云いたくなる。筆を執っても心持は同じ事である。余所々々しい頭文字などはとても使う気にならない。', 'ある日の暮方の事である。一人の下人が、羅生門の下で雨やみを待っていた。']
                },
                'regular': {
                    'name': get_random_name('male' if random.randint(0, 1) == 0 else 'female'),
                    'family': families[random.randint(0, len(families) - 1)]
                }
            },
            'home': home[random.randint(0, 2)],
            'dischargeDate': get_random_date('2000/01/01' ,'2030/12/31').strftime('%Y/%m/%d'),
            'backbed': {
                'register': get_random_date('2000/01/01', '2030/12/31').strftime('%Y/%m/%d'),
                'institution': get_random_hospital()
            },
            'careManager': {
                'institution': get_random_hospital(),
                'tel': str(random.randint(10000000000, 99999999999)),
                'manager': get_random_name('male' if random.randint(0, 1) == 0 else 'female')
            },
            'homeNursingTEL': str(random.randint(10000000000, 99999999999)),
            'request': {
                'patient': ['私は、その男の写真を三葉、見たことがある。', '石炭をば早や積み果てつ。中等室の卓のほとりはいと静にて、熾熱燈の光の晴れがましきも徒なり。今宵は夜毎にこゝに集ひ来る骨牌仲間も「ホテル」に宿りて、舟に残れるは余一人のみなれば。'],
                'family': ['「ではみなさんは、そういうふうに川だと言われたり、乳の流れたあとだと言われたりしていた、このぼんやりと白いものがほんとうは何かご承知ですか」先生は、黒板につるした大きな黒い星座の図の、上から下へ白くけぶった銀河帯のようなところを指さしながら、みんなに問いをかけました。', 'えたいの知れない不吉な塊が私の心を始終圧えつけていた。']
            },
            'emergency': {
                'hospitalization': '有' if random.randint(0, 1) == 0 else '無',
                'care': '有' if random.randint(0, 1) == 0 else '無'
            },
            'familyType': family_type[random.randint(0, 2)],
            'housemate': get_random_name('male' if random.randint(0, 1) == 0 else 'female'),
            'keyPerson': {
                'name': get_random_name('male' if random.randint(0, 1) == 0 else 'female'),
                'relationship': '親',
                'tel': str(random.randint(10000000000, 99999999999))
            }
        })
    
    with open('C:/Users/yuki_/python/output/random_data.json', mode='w', encoding='UTF-8') as file:
        json.dump({'data': patients}, file, ensure_ascii=False, indent=4)


def get_institution_data(num):
    institutions = []
    families = ['内科','神経内科','呼吸器科','呼吸器内科','消化器科','消化器内科','胃腸科','腎臓内科','循環器科','漢方内科','心療内科','老年心療内科','アレルギー科','小児科','心臓小児科','皮膚科','小児皮膚科','精神科','神経科','児童精神科','老年精神科','外科','小児外科','肛門科','整形外科','リウマチ科','産婦人科','産科','婦人科','眼科','耳鼻咽喉（いんこう）科','気管食道科','泌尿器科','性病科','脳外科','放射線科','麻酔科','ペインクリニック内科','形成外科','リハビリテーション科']
    
    for i in range(num):
        institutions.append({
            'id': i + 1,
            'name': get_random_hospital(),
            'address': get_random_address(),
            'doctor': get_random_name('male' if random.randint(0, 1) == 0 else 'female'),
            'tel': str(random.randint(10000000000, 99999999999)),
            'family': families[random.randrange(0, len(families))],
            'url': get_random_url(),
            'mail': get_random_mail(),
            'treatments': get_random_treatments('非公開' if random.randint(0, 1) == 0 else '公開'),
            'business': get_random_business_hours(),
            'night': '可能' if random.randint(0, 1) == 0 else '不可能',
            'achievement': get_random_achievement(),
            'lastUpdate': get_random_date('2000/01/01', '2025/12/31').strftime('%Y/%m/%d')
        })
    
    with open('C:/Users/yuki_/python/output/random_data.json', mode='w', encoding='UTF-8') as file:
        json.dump({'data': institutions}, file, ensure_ascii=False, indent=4)


def get_random_date(start_date, end_date):
    start_date = datetime.strptime(start_date, '%Y/%m/%d')
    end_date = datetime.strptime(end_date, '%Y/%m/%d')
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return start_date + timedelta(days=random_number_of_days)


def get_random_name(gender):
    with open('C:/Users/yuki_/python/dataset/name.json', mode='r', encoding='UTF-8') as file:
        obj = json.load(file)
    rand = random.randint(0, min(len(obj['male']), len(obj['female'])) - 1)
    if gender == 'male':
        obj['male'][rand]['initial'] = kana2initial.convert(obj['male'][rand]['firstRuby'], obj['male'][rand]['lastRuby'])
        return obj['male'][rand]
    else:
        obj['female'][rand]['initial'] = kana2initial.convert(obj['female'][rand]['firstRuby'], obj['female'][rand]['lastRuby'])
        return obj['female'][rand]


def get_random_address():
    with open('C:/Users/yuki_/python/dataset/address.json', mode='r', encoding='UTF-8') as file:
        obj = json.load(file)
    rand = random.randint(0, len(obj['data']) - 1)
    return obj['data'][rand]


def get_random_disease():
    with open('C:/Users/yuki_/python/dataset/disease.json', mode='r', encoding='UTF-8') as file:
        obj = json.load(file)
    rand = random.randint(0, len(obj['data']) - 1)
    return obj['data'][rand]


def get_random_treatments(state):
    if state == '非公開': return [state]
    rarity = 1
    treatments = ['tpn','btm','thoracentesis','celiocentesis','tfnt','tfpeg','tracheostomy','ventilator','aspiration','stoma','iuc','idc','insulin','dec','oxygen','drug','pacemaker']
    indexes = []
    array = []
    while rarity > 0.1:
        rarity *= random.random()
        index = random.randint(0, len(treatments) - 1)
        if index in indexes: continue
        treatment = treatments[index]
        array.append(treatment)
        indexes.append(index)
    return array


def get_random_symptom():
    rarity = 1
    symptoms = ['言語障害', '意識障害', '嘔気', '嘔吐', '便秘', '下痢', '頻尿', '尿閉', '腹水', '呼吸困難', '咳', '嚥下困難', '浮腫']
    indexes = []
    array = []
    while rarity > 0.1:
        rarity *= random.random()
        index = random.randint(0, len(symptoms) - 1)
        if index in indexes: continue
        symptom = symptoms[index]
        array.append(symptom)
        indexes.append(index)
    return array


def get_random_hospital():
    with open('C:/Users/yuki_/python/dataset/hospital_with_university.json', mode='r', encoding='UTF-8') as file:
        obj = json.load(file)
    rand = random.randint(0, len(obj['data']) - 1)
    return obj['data'][rand]


def get_random_mail():
    with open('C:/Users/yuki_/python/dataset/mail.json', mode='r', encoding='UTF-8') as file:
        obj = json.load(file)
    rand = random.randrange(0, len(obj['data']))
    return obj['data'][rand]


def get_random_url():
    mail = get_random_mail()
    return "http://{}.example.com".format(re.match(r'(\S+)@', mail).group(0))


def get_random_business_hours():
    return {
        'monday': {
            'start': '09:00',
            'end': '17:00'
        },
        'tuesday': {
            'start': '09:00',
            'end': '17:00'
        },
        'wednesday': {
            'start': '09:00',
            'end': '17:00'
        },
        'thursday': {
            'start': '09:00',
            'end': '17:00'
        },
        'friday': {
            'start': '09:00',
            'end': '17:00'
        },
        'saturday': {
            'start': '09:00',
            'end': '17:00'
        },
        'sunday': {
            'start': '09:00',
            'end': '17:00'
        },
    }


def get_random_achievement():
    return {
        'data': []
    }


if __name__ == '__main__':
    main()