# import random
# secret = random.randint(1,10)
# guess = int(input('정답은? :'))
# if secret == guess:
#     print('정답입니다.')
# elif secret > guess:
#     print(f'정답보다 작은 수입니다. 정답은 {secret}.')
# else:
#     print(f'정답보다 큰 수입니다. 정답은 {secret}')

# start = 'Na' * 4 + '\n'
# middle = 'Hey' * 2 + '\n'
# end = 'Goodbye'
# print(start + middle + end)

# name = 'Henny'
# print('P' + name[1:])

# univ = 'Inha University'
#print(univ[8:])
#print(univ[5:15])
#print(univ[:4])
#print(univ[6:10])
#print(univ[0:-1:3])

#pirates_list = ['Luffy', 'Law', 'Captain Kid']
#pirates_string = ', '.join(pirates_list)
#print('Captain Trio:',pirates_string)

# 연습문제 5.1
#song = """When an eel grabs your arm,
#And it causes great harm,
#That's - a moray!"""
#song = song.replace(' m'," M")
#print(song)
#print()

# 연습문제 5.2

#questions = [
#"We don't serve strings around here. Are you a string?",
#"What is said on Father's Day in the forest?",
#"What makes the sound 'Sis! Boom! Bah!'?"
#]
#answers = [
#"An exploding sheep.",
#"No, I'm a frayed knot.",
#"'Pop!' goes the weasel."
#]

#q_a = ((0,1),(1,2),(2,0))
#for q, a in q_a:
#    print('Q: ',questions[q])
#    print('A: ',answers[a])
#    print()

# 연습문제 5.3

#poem = """My kitty cat likes %s,
#My kitty cat likes %s,
#My kitty cat fell on his %s
#And now thinks he's a %s."""
#words = ('roast beef', 'ham', 'head', 'clam')
#print(poem % words)

#while

#while True:
#    dan = int(input('Dan : '))

    #if 1 < dan < 10:
#    if 2 <= dan <= 9:
#        i = 1
#        while i < 10:
#            print('{0} * {1} = {2}'.format(dan, i, dan*i))
#            i = i+1
#        break
#    else:
#        print('2에서 9 사이의 값을 입력하세요.')

# break
#while True:
#    stuff = input("String to capitalize [type q to quit]: ")
#    if stuff == "q":
#        break
#    print(stuff.capitalize())

# continue
#while True:
#    value = input("Integer, please [q to quit]: ")
#    if value == 'q': #quit
#        break
#    number = int(value)
#    if number % 2 == 0: #짝수
#        continue
#    print(number, '의 제곱은', number*number,'입니다.')

# else
numbers = [1,3,5]
position = 0
while position < len(numbers):
        number = numbers[position]
        if number % 2 == 0:
             print('짝수 찾음', number)
             break
        position += 1 # += : 오른쪽 값을 왼쪽 값에 더하고 재정의
else : #break 문이 호출되지 않은 경우
             print('짝수 없음')

#for
while True:
    dan = int(input('Dan (0 to quit): '))

    if dan == 0: #exit
        break
    if 1 < dan < 10:
        for i in range(1, 10):
            print('{0} * {1} = {2}'.format(dan, i, dan * i))
    else:
        print('2에서 9 사이의 값을 입력하세요.')

word = 'thudx'
for letter in word:
    if letter == 'x':
        print("Eek! An 'x'!")
        break
else:
        print("No 'x' in there.")