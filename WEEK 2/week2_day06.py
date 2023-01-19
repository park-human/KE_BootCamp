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

def sub_int(x,y):
	return x-y

# decorator
def document_info(func):
	def new_function(*args, **kwargs):
		print('실행중인 함수: ', func.__name__)
		print('위치 기반 인수들: ', args)
		print('키워드 기반 인수들: ', kwargs)
		result = func(*args, **kwargs)
		print('실행결과: ', result)
		return result
	return new_function

print(sub_int(7,3))
info_sub_int = document_info(sub_int)
r = info_sub_int(7,3)
print(r)

@document_info
def sub_int (x,y):
	return x - y

@document_info
def squares(n):
	return n * n

print(sub_int(7,3))
print(squares(5))
