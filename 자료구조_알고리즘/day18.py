#Code09-03
## 클래스와 함수 선언 ##
class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

## 전역 변수 선언 ##
G1 = None
stack = []
visitedAry = []

## 메인 코드 ##
G1 = Graph(9)
G1.graph[0][1] = 1; G1.graph[0][2] = 1; G1.graph[0][4] = 1
G1.graph[1][2] = 1; G1.graph[1][2] = 1; G1.graph[1][3] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1; G1.graph[2][4] = 1; G1.graph[2][5] = 1
G1.graph[3][1] = 1; G1.graph[3][2] = 1
G1.graph[4][0] = 1; G1.graph[4][2] = 1; G1.graph[4][6] = 1; G1.graph[4][7] = 1
G1.graph[5][3] = 1
G1.graph[6][4] = 1; G1.graph[6][8] = 1
G1.graph[7][4] = 1; G1.graph[7][8] = 1
G1.graph[8][6] = 1; G1.graph[8][7] = 1

for row in range(4):
    for col in range(4):
        print(G1.graph[row][col], end = ' ')
    print()

current = 0 # 시작 정점
stack.append(current)
visitedAry.append(current)

while (len(stack) != 0):
    next = None
    for vertex in range(4):
        if G1.graph[current][vertex] != 0 :
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

print('방문 순서 : ', end = ' ')
for i in visitedAry :
    print(chr(ord('A') + i), end = ' ')