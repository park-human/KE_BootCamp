# function : prime number
# def isprime(n):
#     """
#     매개변수로 받은 정수가 소수인지 여부를 판정하는 함수
#     :param n: integer number
#     :return: true or false
#     """
#     if n <= 1:
#         return False
#     for k in range(2, n):
#         if n % k == 0:
#             return False
#     else:
#         return True
#
# help(isprime)
# # print(isprime(43))
#
# start = int(input("input start number : "))
# end = int(input("input end number : "))
#
# if end < start:
#     start, end = end, start
#
# for i in range(start, end+1):
#     if isprime(i):
#         print(i, end=' ')
import random

# function
#def do_nothing():
#    pass
#do_nothing()
#print(do_nothing())

#mamamoo = ['화사','솔라','휘인','문별']
# print(mamamoo.pop()) # 삭제할 값 리턴 후 삭제
#print(mamamoo.remove('문별')) # 삭제만. 즉, 리턴값 없음(None 출력)
#print(mamamoo)

# def nonbuggy(arg, result=None):
# 	if result is None:
# 		result = []
# 	result.append(arg)
# 	print(result)
#
# print(nonbuggy('a'))
# print(nonbuggy('b'))

# 놀이공원 입장객의 유형(성인/아동)과 총 금액 계산하기 (단, 입장객의 나이는 1~60 사이 랜덤)

import random
def calculate_fee(args)-> list:
    """
    놀이공원 요금 계산 프로그램
    :param args: ages in list
    :return: 전체 인원 수, 어른 수, 아이 수, 지불할 총 입장료
    """
    total = 0
    adults = 0
    kids = 0
    for age in args:
        if 19 <= age:
            total = total + 10000
            adults = adults + 1
        else:
            total = total + 3000
            kids = kids + 1
    return [len(args), adults, kids, total]

no_of_visitor = int(input('총 인원수를 입력하세요. : '))
ages = [random.randint(1,60) for age in range(no_of_visitor)]
results = calculate_fee(ages)
print(f'총 인원 수: {results[0]}분. 성인 {results[1]}명, 아동 {results[2]}명, 총 요금은 {results[3]}원입니다.')

# def print_more(required1, required2, *args):
# 	print('Need this one:', required1)
# 	print('Need this one, too.', required2)
# 	print('All the rest:', args)
#
# print_more('cap','gloves','scarf','monocle','mustache wax')