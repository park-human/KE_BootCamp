# def a():    # generator
#     yield 1
#     yield 2
#     yield 3
#
# def b():    # normal function
#     return 1
#     return 2
#     return 3
#
# print(a(), b())
# for i in a():
#     print(i)
#
# def my_range(first=0, last=10, step=1):
# 	number = first
# 	while number < last:
# 		yield number
# 		number += step
#
# ranger = my_range(1,5)
# for x in ranger:
# 	print(x)

# def sub_int(x,y):
# 	return x-y

# decorator
# def document_info(func):
# 	def new_function(*args, **kwargs):
# 		print('실행중인 함수: ', func.__name__)
# 		print('위치 기반 인수들: ', args)
# 		print('키워드 기반 인수들: ', kwargs)
# 		result = func(*args, **kwargs)
# 		print('실행결과: ', result)
# 		return result
# 	return new_function
#
# print(sub_int(7,3))
# info_sub_int = document_info(sub_int)
# r = info_sub_int(7,3)
# print(r)
#
# @document_info
# def sub_int (x,y):
# 	return x - y
#
# @document_info
# def squares(n):
# 	return n * n
#
# print(sub_int(7,3))
# print(squares(5))

# g = 1 #global variable
#
# def print_global():
#  	#g = 1 #local variable
# 	print(g)
#
# def change_print_global():
# 	global g
# 	print(g)
# 	g=2
# 	print(g)
#
# change_print_global()
# print_global()
# print(g)

# animal = 'fruitbat'
# def print_global():
# 	animal = 'wombat'
# 	print('inside print_global: ', animal)
#
# print('at the top level: ', animal)
# print_global()

# def change_and_print_global():
# 	print('inside change_and_print_global:', animal)
# 	animal = 'wombat'
# 	print('after the change:', animal)
#
# change_and_print_global()

# animal = 'fruitbat' # 전역 변수
# def change_local():
# 	animal = 'wombat' # 지역 변수
# 	print('locals: ', locals())
#
# print(animal)
# print(change_local())
# print('globals:',globals())

#recursion
# def factorial_iter(n):
#     """
#     반복문을 사용한 팩토리얼 함수
#     :param n: n!
#     "return: 팩토리얼 계산 결과 값
#     """
#     result = 1
#     for k in range(1,n+1):
#         result = result * k
#     return result
#
# def factorial_recu(n):
#     """
#     재귀 함수를 사용한 팩토리얼 계산 함수
#     :param n: n!
#     :return: 자기 자신을 호출 또는 1
#     """
#     if n == 1:
#         return 1 # 끝나는 조건
#     else:
#         return factorial_recu(n-1) * n
#
# print(factorial_iter(5))
# print(factorial_recu(5))