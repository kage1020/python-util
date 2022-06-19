def main():
    print('main function')


def convert(first, last):
    return "{}.{}.".format(get_initial(first[0]), get_initial(last[0]))


def get_initial(char):
    if char == 'あ' or char == 'ア': return 'A'
    if char == 'い' or char == 'イ' or char == 'ゐ': return 'I'
    if char == 'う' or char == 'ウ': return 'U'
    if char == 'え' or char == 'エ' or char == 'ゑ': return 'E'
    if char == 'お' or char == 'オ' or char == 'を' or char == 'ヲ': return 'O'
    if (char == 'か' or char == 'き' or char == 'く' or char == 'け' or char == 'こ' 
        or char == 'カ' or char == 'キ' or char == 'ク' or char == 'ケ' or char == 'コ'): return 'K'
    if (char == 'が' or char == 'ぎ' or char == 'ぐ' or char == 'げ' or char == 'ご'
        or char == 'ガ' or char == 'ギ' or char == 'グ' or char == 'ゲ' or char == 'ゴ'): return 'G'
    if (char == 'さ' or char == 'し' or char == 'す' or char == 'せ' or char == 'そ'
        or char == 'サ' or char == 'シ' or char == 'ス' or char == 'セ' or char == 'ソ'): return 'S'
    if (char == 'ざ' or char == 'ず' or char == 'ぜ' or char == 'ぞ' or char == 'づ'
        or char == 'ザ' or char == 'ズ' or char == 'ゼ' or char == 'ゾ' or char == 'ヅ'): return 'Z'
    if (char == 'た' or char == 'つ' or char == 'て' or char == 'と'
        or char == 'タ' or char == 'ツ' or char == 'テ' or char == 'ト'): return 'T'
    if (char == 'だ' or char == 'で' or char == 'ど'
        or char == 'ダ' or char == 'デ' or char == 'ド'): return 'D'
    if (char == 'な' or char == 'に' or char == 'ぬ' or char == 'ね' or char == 'の'
        or char == 'ナ' or char == 'ニ' or char == 'ヌ' or char == 'ネ' or char == 'ノ'): return 'N'
    if (char == 'は' or char == 'ひ' or char == 'へ' or char == 'ほ'
        or char == 'ハ' or char == 'ヒ' or char == 'ヘ' or char == 'ホ'): return 'H'
    if (char == 'ば' or char == 'び' or char == 'ぶ' or char == 'べ' or char == 'ぼ'
        or char == 'バ' or char == 'ビ' or char == 'ブ' or char == 'ベ' or char == 'ボ'): return 'B'
    if (char == 'ぱ' or char == 'ぴ' or char == 'ぷ' or char == 'ぺ' or char == 'ぽ'
        or char == 'パ' or char == 'ピ' or char == 'プ' or char == 'ペ' or char == 'ポ'): return 'P'
    if (char == 'ま' or char == 'み' or char == 'む' or char == 'め' or char == 'も'
        or char == 'マ' or char == 'ミ' or char == 'ム' or char == 'メ' or char == 'モ'): return 'M'
    if char == 'や' or char == 'ゆ' or char == 'よ' or char == 'ヤ' or char == 'ユ' or char == 'ヨ': return 'Y'
    if (char == 'ら' or char == 'り' or char == 'る' or char == 'れ' or char == 'ろ'
        or char == 'ラ' or char == 'リ' or char == 'ル' or char == 'レ' or char == 'ロ'): return 'R'
    if char == 'わ' or char == 'ワ': return 'W'
    if char == 'ち' or char == 'チ': return 'C'
    if char == 'ふ' or char == 'フ': return 'F'
    if char == 'じ' or char == 'ぢ' or char == 'ジ' or char == 'ヂ': return 'J'


if __name__ == '__main__':
    main()