# 5장 응용예제 01

import random
import math

## 클래스와 함수 선언 ##
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printStores(start):
    current = start
    if current == None:
        return
    while current.link != head:
        current = current.link
        x, y = current.data[1:]
        print(current.data[0], '편의점, 거리 : ', math.sqrt(x*x + y*y))
    print()

def makeStoreList(store):
    global memory, head, current, pre

    node = Node()
    node.data = store
    memory.append(node)

    if head == None: # 편의점1
        head = node
        node.link = head
        return

    # 새 편의점이 첫번째 편의점보다 가까우면 첫번째 편의점으로 만든다
    nodeX, nodeY = node.data[1:]
    nodeDist = math.sqrt(nodeX * nodeX + nodeY * nodeY)
    headX, headY = head.data[1:]
    headDist = math.sqrt(headX * headX + headY * headY)

    if headDist > nodeDist : # 헤드 앞에 삽입
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return

    current = head # 중간에 삽입
    while current.link != head:
        pre = current
        current = current.link
        currX, currY = current.data[1:]
        currDist = math.sqrt(currX * currX + currY * currY)
        if currDist > nodeDist:
            pre.link = node
            node.link = current
            return

    current.link = node
    node.link = head

## 전역 변수 선언 ##
memory = []
head, current, pre = None, None, None

## 메인 코드 ##
if __name__ == "__main__":

    storeArray = []
    storeName = 'A'
    for _ in range(10):
        store = (storeName, random.randint(1,100), random.randint(1,100))
        storeArray.append(store)
        storeName = chr(ord(storeName)+1) # 편의점 이름을 A, B, C ... 순으로 변경

    for store in storeArray:
        makeStoreList(store)

    printStores(head)

# 5장 응용예제 02

## 클래스와 함수 선언 ##
class Node2():
    def __init__(self):
        self.plink = None
        self.data = None
        self.nlink = None

def printNodes(start):
    current = start
    if current.nlink == None:
        return
    print("정방향 ->", end=' ')
    print(current.data, end=' ')
    while current.nlink != None:
        current = current.nlink
        print(current.data, end=' ')
    print()
    print("역방향 ->", end=' ')
    print(current.data, end=' ')
    while current.plink != None:
        current = current.plink
        print(current.data, end=' ')

## 전역 변수 선언 ##
memory = []
head, current, pre = None, None, None
dataArray = ["북산", "능남", "상양", "해남", "풍전"]

## 메인 코드 ##
if __name__ == "__main__":

    node = Node2()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node2()
        node.data = data
        pre.nlink = node
        memory.append(node)

printNodes(head)
print()

# 6장 응용예제 01

import random

## 함수 선언 ##
def isStackFull() :
    global SIZE, stack, top
    if (top >= SIZE-1):
        return True
    else:
        return False

def isStackEmpty():
    global SIZE, stack, top
    if (top == -1):
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if (isStackFull()):
        return
    top +=1
    stack[top] = data

def pop():
    global SIZE, stack, top
    if (isStackEmpty()):
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():
    global SIZE, stack, top
    if (isStackEmpty()):
        return None
    return stack[top]

## 전역 변수 선언 ##
SIZE = 10
stack = [None for _ in range(SIZE)]
top = -1

## 메인 코드 ##

if __name__ == "__main__":

    stoneAry = ["빨강", "파랑", "초록", "노랑", "보라", "주황"]
    random.shuffle(stoneAry)

    print("과자집으로 가는 길 : ", end = " ")
    for stone in stoneAry :
        push(stone)
        print(stone, "->", end = ' ')
    print ("과자집")

    print("우리 집에 오는 길 : ", end = " ")
    while True:
        stone = pop()
        if stone == None:
            break
        print(stone, "->", end = ' ')
    print("우리집")

# 6장 응용예제 02

## 전역 변수 선언 ##
SIZE = 100
stack = [None for _ in range(SIZE)]
top = -1

## 메인 코드 ##
if __name__ == "__main__":

    with open("진달래꽃.txt",'r',encoding='UTF8') as rfp:
        lineAry = rfp.readlines()

    print("- 원본 -")
    for line in lineAry :
        push(line)
        print(line, end = ' ')
    print()

    print("- 거꾸로 처리된 결과 -")
    while True :
        line = pop()
        if line == None:
            break

        subStack = [None for _ in range(len(line))]
        subTop = -1

        for ch in line:
            subTop += 1
            subStack[subTop] = ch

        while True:
            if subTop == -1:
                break
            ch = subStack[subTop]
            subTop -= 1
            print(ch, end = ' ')