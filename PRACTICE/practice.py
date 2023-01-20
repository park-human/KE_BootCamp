# 두 정수 사이의 소수를 출력하는 코드를 while문으로 만들어보자.
# start = int(input("start number : "))
# end = int(input("end number : "))
#
# if end < start:
#     start, end = end, start
#
# i = start
# while i < end+1:
#     if i <= 1:
#         i += 1
#         continue
#     k = 2
#     while k < i:
#         if i % k == 0:
#             break
#         k +=1
#     else:
#         print(i, end=' ')
#     i +=1

# 입장객의 유형(성인/아동)과 총 금액 계산하기 (단, 입장객의 나이는 1~60 사이 랜덤)
# 딕셔너리

# import random
# def calculate_fee(args)-> dict:
#     """
#     놀이공원 요금 계산 프로그램
#     :param args: ages in list
#     :return: {'no_of_visitor':전체 인원 수, 'no_of_adults':어른 수, 'no_of_kids':아이 수, 'total_amount':지불할 총 입장료}
#     """
#
#     total = 0
#     adults = 0
#     kids = 0
#
#     for age in args:
#         if 19 <= age:
#             total = total + 10000
#             adults = adults + 1
#         else:
#             total = total + 3000
#             kids = kids + 1
#     return {'no_of_visitor': len(args), 'no_of_adults':adults, 'no_of_kids':kids, 'total_fee':total}
#
# no_of_visitor = int(input('총 인원수를 입력하세요. : '))
# ages = [random.randint(1,60) for age in range(no_of_visitor)]
# results = calculate_fee(ages)
#
# print(f"총 인원 수: {results['no_of_visitor']}분. 성인 {results['no_of_adults']}명, 아동 {results['no_of_kids']}명, 총 요금은 {results['total_fee']}원입니다.")

# 제너레이터
# def test_generator():
#     yield 1
#     yield 2
#     yield 3
#
# print(test_generator())

#데코레이터
def decorate(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper

@decorate
def say_hi():
    print("Hi!")

print(say_hi())

# 재귀함수
def hello(count):
    if count == 0:
        return
    print('hello', count)
    count -=1
    hello(count)

print(hello(6))