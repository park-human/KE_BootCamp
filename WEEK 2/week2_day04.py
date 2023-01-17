# list
#import copy
#a=[1,2,[5,-9]]
#b=copy.deepcopy(a)
#c=list(a)
#d=a[:]
#a[2][1] = 7 #mutable, deepcopy b는 영향 x
#print(a,b,c,d)

#a=[1,2,[5,-9]]
#b=a.copy()
#c=list(a)
#d=a[:]
#a[2][1] = 7 #mutable, b/c/d 모두 영향
#print(a,b,c,d)

#big_bang = ['GD', '태양', '탑', '대성', '승리']
#exo = ['백현', '첸']
# big_bang.append('인하')
#big_bang.insert(1, '인하')
# print(big_bang * 2)

# exo.extend(big_bang)
# exo = exo + big_bang
#exo.append(big_bang)
#print(exo)
#print(exo[2][2])  # 태양
#print(exo[-1][-4])  # 태양
#exo[-2] = '시우민'
#print(exo)
# print(exo.pop())  # 빅뱅 pop
#print(exo[2].pop())  # 승리 pop
#print(exo)
#print(exo[2].pop(-2))  # 탑 pop
#print(exo)
#del exo[2][-1]  # 대성 delete
#print(exo)
# exo.remove('인하')  # not in exo
#exo[2].remove('인하')
#print(exo)

#exo.clear()
#print(exo)

# scores = ('B+', 'A+', 'C+')
# print(scores[1], scores[2])
# temp = list(scores)
# temp[1] = 'C+'
# temp[2] = 'A+'
# scores = tuple(temp)
# print(scores[1], scores[2])

#primes = [2, 19, 3.0, 5, 7, 11]
#print(sorted(primes))
#primes.sort()
#print(primes)

#mixed = [6, 4, 5, 'A', 7, '트와이스', 'B', 'b', '마마무']
#mixed.sort()
#print(mixed)

#mixed = ['6', '4', '5', 'A', '7', '트와이스', 'B', 'b', '마마무']
#mixed.sort()
#print(mixed)

#days = ['Monday', 'Tuesday', 'Wednesday']
#fruits = ['banana', 'orange', 'peach']
#drinks = ['coffee', 'tea', 'bear']
#desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
#for days, fruits, drink, desserts in zip(days, fruits, drinks, desserts):
#	print(days, ": drink", "- eat", fruits, "- enjoy", desserts)

# list comprehension

# odd_lists = [ i for i in range (1,11) if i % 2 == 1]
#
# odd_tuples = ( i for i in range (1,11) if i % 2 == 1)
# print(odd_tuples)
# #<generator object <genexpr> at 0x000001D40FEF5700>
# print(type(odd_tuples))
#
# odd_lists = []
# for i in range(1, 11):
#   if i % 2 == 1:
#   	odd_lists.append(i)
# print(odd_lists)

# dictionary

#students = {'name' : '박하연', 'age':24, 'eyes':[1.2,0.2]}
# for k in students:
# for k in students.keys()
#for k in students.values():
#for k, v in students.items():
    #print(k)
    #print(f'{k}:{v}')
#print(f'이름은 {students["name"]}, 나이는 {students["age"]}세', end=" ")
#print(f'시력은 좌: {students["eyes"][0]}, 우: {students["eyes"][1]}')

# 안주 추천 프로그램
import random

# alcohol_foods = {
#     '맥주' : '치킨',
#     '소주' : '골뱅이소면',
#     '와인' : '치즈',
#     '고량주' : '짬뽕'
# }
1
alcohol_foods = dict(맥주='치킨', 소주='골뱅이소면', 와인='치즈', 고량주='짬뽕')
alcohol_list = list(alcohol_foods) # extract keys
food_list = [food for food in alcohol_foods.values()] # extract values and append list

while True:
    alcohol = input(f'술을 선택하세요. 1){alcohol_list[0]} 2){alcohol_list[1]} 3){alcohol_list[2]} 4){alcohol_list[3]} 5) 아무거나 6) 계산 : ')
    if alcohol == '6':
        print('다음에 또 오세요.')
        break

    # elif alcohol == '1' :
    #     print(f'{alcohol_list[0]}에 어울리는 안주는 {alcohol_foods[alcohol_list[0]]}입니다.')
    # elif alcohol == '2' :
    #     print(f'{alcohol_list[1]}에 어울리는 안주는 {alcohol_foods[alcohol_list[1]]}입니다.')
    # elif alcohol == '3' :
    #     print(f'{alcohol_list[2]}에 어울리는 안주는 {alcohol_foods[alcohol_list[2]]}입니다.')
    # elif alcohol == '4' :
    #     print(f'{alcohol_list[3]}에 어울리는 안주는 {alcohol_foods[alcohol_list[3]]}입니다.')

    elif '1' <= alcohol <= '4':
        print(f'{alcohol_list[int(alcohol) - 1]}에 어울리는 안주는 {alcohol_foods[alcohol_list[int(alcohol) - 1]]}입니다.')
    elif alcohol == '5':
        print(f'{random.choice(alcohol_list)}에 어울리는 안주는 {random.choice(food_list)}입니다.')
    else:
        print('메뉴에서 골라주세요.')

for food in enumerate(food_list): #tuple return
    print(food[1])
