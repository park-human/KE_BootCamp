# Chapter 4 : IF

# 4.3 비교하기: if, elif, else
disaster = True
if disaster:
    print("Woe!")
else:
    print("Whee!")

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

color = "mauve"
if color == "red":
    print("It's a tomato")
elif color == "green":
    print("It's a green pepper")
elif color == "bee purple":
    print("I don't know what it is, but only bees can see it")
else:
    print("I've never heard of the color", color)

# 4.4 True와 False

some_list = ['haha']
if some_list:
    print("There's something in here")
else:
    print("Hey, it's empty!")

# 4.5 여러 개 비교하기: in

letter = 'h'
if letter == 'a' or letter == 'e' or letter == 'i' \
        or letter == 'o' or letter == 'u':
    print(letter, 'is a vowel')
else:
    print(letter, 'is not a vowel')

vowels = 'aeiou'
vowel_set = {'a','e','i','o','u'}
letter = 'o'

if letter in vowels:
    print(letter, 'is a vowel')
if letter in vowel_set:
    print(letter, 'is a vowel')

# 4.6 새로운 기능: 바다코끼리 연산자

tweet_limit = 280
tweet_string = "Blah" * 50
# diff = tweet_limit - len(tweet_string)
# if diff >= 0:
#     print("A fittig tweet")
# else:
#    print("Went over by", abs(diff))

if diff := tweet_limit - len(tweet_string) >= 0:
    print("A fitting tweet")
else:
    print("Went over by", abs(diff))

diff = tweet_limit - len(tweet_string) >=0
print(diff)

# Chapter 5 : 텍스트 문자열
# 5.1 따옴표로 문자열 생성

print("'Snap' =",'Snap')
poem = '''There was a Young Lady of Norway,
blah blah
blah'''
print(poem)

# 5.2 문자열 타입으로 변환: str()
str(98.6)