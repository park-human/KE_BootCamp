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
# print(f"총 인원 수: {results['no_of_visitor']}분. 성인 {results['no_of_adults']}명, 아동 {results['no_of_kids']}명, 총 요금은 {results['total_fee']}원입니다.")

# print(calculate_fee.__doc_)
#help(calculate_fee)

# def print_more(required1, required2, *args):
# 	print('Need this one:', required1)
# 	print('Need this one, too.', required2)
# 	print('All the rest:', args)
#
# print_more('cap','gloves','scarf','monocle','mustache wax')

def inha():
    print(42)
    """
    숫자 출력
    """

def call_func(f):
    """
    매개변수로 함수를 넘겨받아 실행
    f: 매개변수가 함수
    """
    f()

call_func(inha)
print(type(call_func))

def add_args(arg1,arg2):
    print(arg1 + arg2)
def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)
run_something_with_args(add_args,5,9)

def substract(n1,n2):
    print(n1 - n2)
def run_func(f,arg1,arg2):
    """
    함수를 매개 변수로 받아 함수 안에서 해당 함수를 실행
    f: 첫 번째 인수는 함수
    arg1: 정수 값
    arg2: 정수 값
    """
    f(arg1,arg2)
run_func(substract,7,2)

a = (5, 7, -1)
print(sum(a))

def knights(saying):
    def inner2():
        return "We are the knights who say:'%s'" % saying
    return inner2
a = knights('Duck')
b = knights('Hello')
print(a())
print(b())