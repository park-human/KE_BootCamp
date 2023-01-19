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

# def something(n):
#     a=5
#     a=a+n
#     print(a)
#
# something(1)
# something(3)

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

# def div_calc(a,b):
#     """
#     나누기 함수
#     :param a: 분자
#     :param b: 분모
#     :return: 계산결과
#     """
#     return a / b
#
# print(div_calc(15,3))
# try:
#     (div_calc(15,0))
# except:
#     print('0으로는 나눌 수 없습니다.')

# try:
#     expr = input('분자와 분모를 입력하세요 : ').split()
#     print(int(expr[0]) / int(expr[1]))
#
# except ValueError as err:
#     print(f'숫자를 입력해주세요. ({err})')
# except ZeroDivisionError as err:
#     print(f'분모에 0이 올 수 없습니다.({err})')
# except IndexError as err:
#     print(f'입력 값의 범위에 문제가 있습니다.({err})')
# except Exception as other:
#     print(f'예외 발생 : {other}')
# else: # 예외가 발생하지 않았을 때
#     print('프로그램 정상', end=' ')
# finally: # 예외 발생 여부와 상과없이 무조건 실행
#     print('종료')

# 9.1
# def good():
#     return ['Harry', 'Ron', 'Hermione']
#
# 9.2
# cnts = 0
# def get_odds():
#     for num in range(10):
#         if num % 2:
#             yield num
#
# odds = get_odds()
# for i in odds:
#     cnts += 1
#     if cnts == 3:
#         print(i)
#
# 9.3
# def test():
#
#     print('start')
#     print('end')
#
# groups = {
#     '빅뱅':['GD','태양','탑','대성','승리'],
#     '마마무':['문별','솔라','휘인','화사']
# }
#
# 조건 : 빅뱅의 탈퇴 멤버 '승리'는 조건문을 사용하여 필터링한다.
#
# for group, members in groups.items():
#     print('f{group}의 멤버')
#     for member in members:
#         if member !="승리":
#             print(member)

# class
# class Pokemon:
#     def __init__(self):
#         print("포켓몬 객체 생성됨")
# p1 = Pokemon()
# p2 = Pokemon()
# print(p1, p2) # 서로 다른 두 객체

class Pokemon:
    def __init__(self, name, owner, type, skills):
        self.name = name
        self.owner = owner
        self.type = type
        self.skills = skills.split('/')
        #print(f"포켓몬 '{name}' 생성됨")

    def info(self):
        print(f"{self.owner}의 포켓몬은 {self.name}는 {self.type}속성입니다.")
        #print(f"{self.name}의 스킬: {self.skills}")
        for skill in self.skills:
            print(skill)

class Pikachu(Pokemon): #inheritance
    pass

pi1 = Pikachu('피카츄', '한지우', '전기', '100만 볼트')
pi1.info()
p1 = Pokemon('피카츄', '한지우','번개', '100만 볼트/전기자석파/전기쇼크')
p2 = Pokemon('꼬부기', '오바람','물', '고속스핀/하이드로펌프/메가톤펀치')

#p1.info()
#p2.info()
# print(f'{p1.owner}의 포켓몬은 {p1.name}입니다.')
# print(f'{p2.owner}의 포켓몬은 {p2.name}입니다.')
#print(p1, p2) # 서로 다른 두 객체