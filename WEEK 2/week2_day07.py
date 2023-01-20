# class

# class Pokemon:
#     def __init__(self, owner, skills):
#         self.owner = owner
#         self.skills = skills.split('/')
#         print(f"포켓몬 생성 :", end=' ')
#
#     def info(self):
#         print(f"{self.owner}의 포켓몬이 사용 가능한 스킬")
#         for i in range(len(self.skills)):
#             print(f'{i+1} : {self.skills[i]}')
#         # for skill in self.skills:
#         #     print(f'{skill}')
#
#     def attack(self, idx):
#         print(f'{self.skills[idx]} 공격 시전!')
#
#
# class Pikachu(Pokemon):  # inheritance
#     def __init__(self, owner, skills):
#         super().__init__(owner, skills)
#         self.name = "피카츄"
#         print(f"{self.name}")
#
#     def attack(self, idx):  # override
#         print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격(전기) 시전!')
#
# class Ggoboogi(Pokemon):  # inheritance
#     def __init__(self, owner, skills):
#         super().__init__(owner, skills)
#         self.name = "꼬부기"
#         print(f"{self.name}")
#
#     def attack(self, idx):  # override
#         print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격(물) 시전!')
#
#     def swim(self):
#         print(f'{self.name}가 수영을 합니다')
#
# class Pairi(Pokemon):  # inheritance
#     def __init__(self, owner, skills):
#         super().__init__(owner, skills)
#         self.name = "파이리"
#         print(f"{self.name}")
#
#     def attack(self, idx):  # override
#         print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격(불) 시전!')
#
#     def swim(self):
#         print(f'{self.name}가 수영을 합니다')
#
# while True:
#     menu = input('1) 포켓몬 생성 2) 정보 조회 3) 공격 4) 프로그램 종료 : ')
#     if menu == '4':
#         print('프로그램을 종료합니다')
#         break
#     elif menu == '1':
#         pokemon = input('1) 피카츄 2) 꼬부기 3) 파이리 : ')
#         if pokemon == '1':
#             n = input('플레이어 이름 입력 : ')
#             s = input('사용 가능한 기술 입력(/로 구분) : ')
#             p = Pikachu(n, s)
#         elif pokemon == '2':
#             n = input('플레이어 이름 입력 : ')
#             s = input('사용 가능한 기술 입력(/로 구분) : ')
#             p = Ggoboogi(n, s)
#         elif pokemon == '3':
#             n = input('플레이어 이름 입력 : ')
#             s = input('사용 가능한 기술 입력(/로 구분) : ')
#             p = Pairi(n, s)
#         else:
#             print('메뉴에서 골라주세요')
#         info_attack = input('1) 정보 조회 2) 공격')
#         if info_attack == '1':
#             p.info()
#         elif info_attack =='2':
#             p.info()
#             attack_menu = input('공격 번호 선택 : ')
#             p.attack(int(attack_menu)-1)
#         else:
#             print('메뉴에서 골라주세요')
#     else:
#         print('메뉴에서 골라주세요')
#
# p0 = Pokemon('아이리스', '어떤 공격')
# p0.attack(0)
# p0.swim()  # 꼬부기 클래스의 객체들이 사용할 수 있는 고유 메서드

# pk1 = Pikachu('한지우', '번개/100만 볼트')
# #pk1.info()
# ggo1 = Ggoboogi('오바람', '고속스핀/거품/몸통박치기')
# #ggo1.info()
# ggo1.swim()
# ggo1.attack(2)
# pk1.attack(1)


#pi1.info()
# p1 = Pokemon('한지우', '50만 볼트/100만 볼트/번개')
# p2 = Pokemon('오바람', '고속스핀/거품/몸통박치기/하이드로펌프')

# class Animal:
#     def says(self):
#         return 'I speak!'
#
# class Horse(Animal):
#     def says(self):
#         return 'Neigh!'
#
# class Donkey(Animal):
#     def says(self):
#         return 'Hee-haw!'
#
# class Mule(Donkey, Horse):
#     pass
#
# class Hinny(Horse, Donkey):
#     pass
#
# m1 = Mule()
# h1 = Hinny()
# Mule.says()
# hinny.says()

# Mixin
# class PrettyMixin():
#     def time_print(self):
#         import datetime
#         print(datetime.date.today())
#     def dump(self):
#         import pprint
#         pprint.pprint(vars(self))
# class Thing(PrettyMixin):
#     pass
#
# t = Thing()
# t.time_print()
# t.name = "Nyarlathotep"
# t.feature = "ichor"
# t.age = "eldritch"

# Getter/Setter Method
# class Duck():
# 	def __init__(self, input_name):
# 		self.hidden_name = input_name
#
# 	def get_name(self):
# 		print('inside the getter')
# 		return self.hidden_name
#
# 	def set_name(self, input_name):
# 		print('inside the setter')
# 		self.hidden_name = input_name
# 	name = property(get_name, set_name)

# class Duck():
#	color:white
#     def __init__(self, input_name):
#         self.hidden_name = input_name
#     @property
#     def name(self):
#         print('inside the getter')
#         return self.hidden_name
#     @name.setter
#     def name(self, input_name):
#         print('inside the setter')
#         self.hidden_name = input_name

# don = Duck('Donald')
# print(don.color, Duck.color)
# don.color = 'blue'
# print(don.color, Duck.color)
# Duck.color = 'green' # 클래스 변수 값 변경
# print(don.color, Duck.color)
# d2 = Duck('Induk')
# print(don.color, Duck.color, d2.color)

#print(don.get_name())
# print(don.name)
#don.set_name('Donna')
# don.name = "Donna"
#print(don.get_name())
# print(don.name)
# don.hidden_name = "Kim Inha"
# don.name = "Jin"
# print(don.get_name())

# class method
# class A():
# 	count = 0
# 	def __init__(self):
# 		A.count += 1
# 	def exclaim(self):
# 		print("I'm an A!")
# 	@classmethod
# 	def kids(cls):
# 		print("A has", cls.count, "little objects.")
#
# easy_a = A()
# breezy_a = A()
# wheezy_a = A()
#
# A.kids()

# Duck Typing
import math
class Shape:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def get_area(self):
		print('도형의 면적을 출력합니다.')


class Circle(Shape):
	def __init__(self, x, y, radius):
		super().__init__(x,y)
		self.radius = radius

	def get_area(self):
		return math.pi * self.radius * self.radius


class Rectangle(Shape):
	def __init__(self, x, y, width, length):
		super().__init__(x, y)
		self.width = width
		self.length = length

	def get_area(self):
		return self.width * self.length


class Cylinder(Circle):
	def __init__(self, x, y, radius, height):
		super().__init__(x,y, radius)
		self.height = height

	def get_area(self):		# get_volume
		return super().get_area() * self.height

def __repr__(self):
	return f'사각형의 좌표는 x:{self.x}, y:{self.y}이고 넓이는 {self.get_area()}입니다.'

def __add__(self, other):
	# 두 사각형 넓이의 합
	# return (self.width * self.length) + (other.width * other.length)
	# 각 사각형의 width의 합과 length의 합의 곱
	return Rectangle(0, 0, (self.width + other.width),(self.length + other.length))

cy1 = Cylinder(20, 20, 10.0, 2)
c1 = Circle(100, 100, 10.0)
c2 = Circle(50, 50, 2.0)
r1 = Rectangle(100, 50, 5, 2)
r2 = Rectangle(70,30,10,15)

print(r2)
print(cy1.get_area())
print(f'사각형의 좌표는 x:{self.x}, y:{self.y}이고 넓이는 {self.get_area()}입니다.')
print(r1)
#print(r1 + r2)
print(c1.get_area())
print(c2.get_area())