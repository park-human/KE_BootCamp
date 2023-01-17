# list
import copy
a=[1,2,[5,-9]]
b=copy.deepcopy(a)
c=list(a)
d=a[:]
a[2][1] = 7 #mutable, deepcopy b는 영향 x
print(a,b,c,d)

#a=[1,2,[5,-9]]
#b=a.copy()
#c=list(a)
#d=a[:]
#a[2][1] = 7 #mutable, b/c/d 모두 영향
#print(a,b,c,d)

big_bang = ['GD', '태양', '탑', '대성', '승리']
exo = ['백현', '첸']
# big_bang.append('인하')
big_bang.insert(1, '인하')
# print(big_bang * 2)

# exo.extend(big_bang)
# exo = exo + big_bang
exo.append(big_bang)
print(exo)
print(exo[2][2])  # 태양
print(exo[-1][-4])  # 태양
exo[-2] = '시우민'
print(exo)
# print(exo.pop())  # 빅뱅 pop
print(exo[2].pop())  # 승리 pop
print(exo)
print(exo[2].pop(-2))  # 탑 pop
print(exo)
del exo[2][-1]  # 대성 delete
print(exo)
# exo.remove('인하')  # not in exo
exo[2].remove('인하')
print(exo)

exo.clear()
print(exo)

# scores = ('B+', 'A+', 'C+')
# print(scores[1], scores[2])
# temp = list(scores)
# temp[1] = 'C+'
# temp[2] = 'A+'
# scores = tuple(temp)
# print(scores[1], scores[2])

primes = [2, 19, 3.0, 5, 7, 11]
#print(sorted(primes))
primes.sort()
print(primes)

#mixed = [6, 4, 5, 'A', 7, '트와이스', 'B', 'b', '마마무']
#mixed.sort()
#print(mixed)

mixed = ['6', '4', '5', 'A', '7', '트와이스', 'B', 'b', '마마무']
mixed.sort()
print(mixed)

days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'bear']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for days, fruits, drink, desserts in zip(days, fruits, drinks, desserts):
	print(days, ": drink", "- eat", fruits, "- enjoy", desserts)