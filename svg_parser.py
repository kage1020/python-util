array = list(map(str, input().replace(',', ' ').split(' ')))

l = ''
for i in array:
    try:
        num = round(float(i), 2)
        # print(num)
        l += str(num) + ' '
    except ValueError:
        l += i + ' '
        continue

print(l)