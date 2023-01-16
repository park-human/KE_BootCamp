# fahrenheit = float(input('화씨 온도 : '))
# celsius = (fahrenheit - 32.0) * (5.0/9.0)
# print(f'화씨 온도 {fahrenheit}도는 섭씨 온도 {celsius:.4f}입니다.')

furry = True
large = True
if furry:
    if large:
        print("It's a yeti.")
    else:
        print("It's a cat.")
else:
    if large:
        print("It's a whale.")
    else:
        print("It's a human.")

x = 7
print(5 < x < 10)

# False
a = []
print(bool(a))
a.append(5)
print(bool(set()))
print(bool(dict()))
print(bool("ace"))

# in이 있는 다중비교
letter = 'o'
if letter == 'a' or letter == 'e' or letter == 'i'\
    or letter == 'o' or letter == 'u':
    print(letter, 'is a vowel')
else: print(letter, 'is not a vowel')

vowels = 'aeiou'
letter = 'u'
if letter not in vowels:
    print('모음 없음!')
else: print('모음 있음!')