# 9장 응용예제 01
# ## 클래스와 함수 선언 ##
# class Graph():
#     def __init__(self, size):
#         self.SIZE = size
#         self.graph = [[0 for _ in range(size)] for _ in range(size)]
#
# def printGraph(g):
#     print('          ', end=' ')
#     for v in range(g.SIZE):
#         print("%9s" % storeAry[v][0], end = ' ')
#     print()
#     for row in range(g.SIZE):
#         print("%9s" % storeAry[row][0], end = ' ')
#         for col in range(g.SIZE):
#             print("%8d" % g.graph[row][col], end = ' ')
#         print()
#     print()
#
# ## 전역 변수 ##
# G1 = None
# storeAry = [['GS25',30],['CU',60],['Seven11',10],['MiniStop',90],['Emart24',40]]
# GS25, CU, Seven11, MiniStop, Emart24 = 0, 1, 2, 3, 4
#
# ## 메인 코드 ##
# gSize = 5
# G1 = Graph(gSize)
# G1.graph[GS25][CU] = 1; G1.graph[GS25][Seven11] = 1
# G1.graph[CU][GS25] = 1; G1.graph[CU][Seven11] = 1; G1.graph[CU][MiniStop] = 1
# G1.graph[Seven11][GS25] = 1; G1.graph[Seven11][CU] = 1; G1.graph[Seven11][MiniStop] = 1
# G1.graph[MiniStop][Seven11] = 1; G1.graph[MiniStop][CU] = 1; G1.graph[MiniStop][Emart24] = 1
# G1.graph[Emart24][MiniStop] = 1
#
# print('편의점 그래프')
# printGraph(G1)
#
# stack = []
# visitedAry = []
#
# current = 0
# maxStore = current
# maxCount = storeAry[current][1]
# stack.append(current)
# visitedAry.append(current)
#
# while (len(stack) != 0):
#     next = None
#     for vertex in range(gSize):
#         if G1.graph[current][vertex] == 1:
#             if vertex in visitedAry:
#                 pass
#             else:
#                 next = vertex
#                 break
#         if next != None:
#             current = next
#             stack.append(current)
#             visitedAry.append(current)
#
#             if storeAry[current][1] > maxCount:
#                 maxCount = storeAry[current][1]
#                 maxStore = current
#         else:
#             current = stack.pop()
#
# print("포켓몬빵 최대 보유 편의점(개수) : ", storeAry[maxStore][0],"(", storeAry[maxStore][1], ")")

# 9장 응용예제 02

## 클래스와 함수 선언 ##
class Graph():
    def __init__(self,size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

def printGraph(g):
    print('   ', end =' ')
    for v in range(g.SIZE):
        print(cityAry[v], end = ' ')
    print()

    for row in range(g.SIZE):
        print(cityAry[row], end =' ')
        for col in range(g.SIZE):
            print("%3d" % g.graph[row][col], end=' ')
        print()
    print()

def findVertex(g, findVtx):
    stack = []
    visitedAry = []

    current = 0
    stack.append(current)
    visitedAry.append(current)

    while (len(stack) != 0):
        next = None
        for vertex in range(gSize):
            if g.graph[current][vertex] != 0:
                if vertex in visitedAry:
                    pass
                else:
                    next = vertex
                    break
        if next != None:
            current = next
            stack.append(current)
            visitedAry.append(current)
        else:
            current = stack.pop()

    if findVtx in visitedAry:
        return True
    else:
        return False

## 전역 변수 선언 ##
G1 = None
cityAry = ['서울', '뉴욕', '런던', '북경', '방콕', '파리']
서울, 뉴욕, 런던, 북경, 방콕, 파리 = 0, 1, 2, 3, 4, 5

## 메인 코드 ##
gSize = 6
G1 = Graph(gSize)

G1.graph[서울][뉴욕] = 80; G1.graph[서울][북경] = 10
G1.graph[뉴욕][서울] = 80; G1.graph[뉴욕][북경] = 40; G1.graph[뉴욕][방콕] = 70
G1.graph[런던][방콕] = 30; G1.graph[런던][파리] = 60
G1.graph[북경][서울] = 10; G1.graph[북경][뉴욕] = 40; G1.graph[북경][방콕] = 50
G1.graph[방콕][파리] = 20; G1.graph[방콕][북경] = 50; G1.graph[방콕][뉴욕] = 70; G1.graph[방콕][런던] = 30
G1.graph[파리][런던] = 60; G1.graph[파리][방콕] = 20

print('해저 케이블 연결을 위한 전체 연결도')
printGraph(G1)

## 가중치 간선 목록 ##
edgeAry = []
for i in range(gSize):
    for k in range(gSize):
        if G1.graph[i][k] != 0:
            edgeAry.append([G1.graph[i][k],i,k])

from operator import itemgetter
edgeAry = sorted(edgeAry, key=itemgetter(0), reverse = False)

newAry = []
for i in range(0, len(edgeAry),2):
    newAry.append(edgeAry[i])

index = 0
while (len(newAry) > gSize -1):
    start = newAry[index][1]
    end = newAry[index][2]
    saveCost = newAry[index][0]

    G1.graph[start][end] = 0
    G1.graph[end][start] = 0

    startYN = findVertex(G1,start)
    endYN = findVertex(G1,end)

    if startYN and endYN:
        del(newAry[index])
    else:
        G1.graph[start][end] = saveCost
        G1.graph[end][start] - saveCost
        index += 1

print('가장 효율적인 해저 케이블 연결도')
printGraph(G1)