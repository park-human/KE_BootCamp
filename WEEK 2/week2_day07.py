# class

class Pokemon:
    def __init__(self, owner, skills):
        self.owner = owner
        self.skills = skills.split('/')
        print(f"포켓몬 생성 :", end=' ')

    def info(self):
        print(f"{self.owner}의 포켓몬이 사용 가능한 스킬")
        for i in range(len(self.skills)):
            print(f'{i+1} : {self.skills[i]}')
        # for skill in self.skills:
        #     print(f'{skill}')

    def attack(self, idx):
        print(f'{self.skills[idx]} 공격 시전!')


class Pikachu(Pokemon):  # inheritance
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "피카츄"
        print(f"{self.name}")

    def attack(self, idx):  # override
        print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격(전기) 시전!')

class Ggoboogi(Pokemon):  # inheritance
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "꼬부기"
        print(f"{self.name}")

    def attack(self, idx):  # override
        print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격(물) 시전!')

    def swim(self):
        print(f'{self.name}가 수영을 합니다')

class Pairi(Pokemon):  # inheritance
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "파이리"
        print(f"{self.name}")

    def attack(self, idx):  # override
        print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격(불) 시전!')

    def swim(self):
        print(f'{self.name}가 수영을 합니다')

while True:
    menu = input('1) 포켓몬 생성 2) 정보 조회 3) 공격 4) 프로그램 종료 : ')
    if menu == '4':
        print('프로그램을 종료합니다')
        break
    elif menu == '1':
        pokemon = input('1) 피카츄 2) 꼬부기 3) 파이리 : ')
        if pokemon == '1':
            n = input('플레이어 이름 입력 : ')
            s = input('사용 가능한 기술 입력(/로 구분) : ')
            p = Pikachu(n, s)
        elif pokemon == '2':
            n = input('플레이어 이름 입력 : ')
            s = input('사용 가능한 기술 입력(/로 구분) : ')
            p = Ggoboogi(n, s)
        elif pokemon == '3':
            n = input('플레이어 이름 입력 : ')
            s = input('사용 가능한 기술 입력(/로 구분) : ')
            p = Pairi(n, s)
        else:
            print('메뉴에서 골라주세요')
        info_attack = input('1) 정보 조회 2) 공격')
        if info_attack == '1':
            p.info()
        elif info_attack =='2':
            p.info()
            attack_menu = input('공격 번호 선택 : ')
            p.attack(attack_menu-1)
        else:
            print('메뉴에서 골라주세요')
    else:
        print('메뉴에서 골라주세요')

p0 = Pokemon('아이리스', '어떤공격')
p0.attack(0)
# p0.swim()  # 꼬부기 클래스의 객체들이 사용할 수 있는 고유 메서드

pk1 = Pikachu('한지우', '번개/100만 볼트')
#pk1.info()
ggo1 = Ggoboogi('오바람', '고속스핀/거품/몸통박치기')
#ggo1.info()
ggo1.swim()
ggo1.attack(2)
pk1.attack(1)


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