## 함수 선언 부분 ##
class Graph():
	def __init__ (self, size):
		self.SIZE = size
		self.graph = [[0 for _ in range(size)] for _ in range(size)]

## 전역 변수 선언 부분 ##
G1, G2 = None, None

## 메인 코드 부분 ##
G1 = Graph(4)
G1.graph[0][1] = 1; G1.graph[0][2] = 1; G1.graph[0][3] = 1
G1.graph[1][0] = 1; G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][2] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1

print('## G1 무방향 그래프 ##')
for row in range(4):
	for col in range(4):
		print(G1.graph[row][col], end = ' ')
	print()

G3 = Graph(4)
G3.graph[0][1] = 1; G3.graph[0][2] = 1
G3.graph[3][0] = 1; G3.graph[3][2] = 1

print('## G3 방향 그래프 ##')
for row in range(4):
	for col in range(4):
		print(G3.graph[row][col], end = ' ')
	print()

# # BFS
# from collections import deque
#
#
# class Graph:
#     def __init__(self, size):
#         self.SIZE = size
#         self.graph = [[0 for x in range(size)] for x in range(size)]
#
#
# g = None
# # queue = []
# queue = deque([])  # deque as queue
# visited_array = []
#
#
# G1 = Graph(9)
# A, B, C, D, E, F, G, H, I = 0, 1, 2, 3, 4, 5, 6, 7, 8
# G1.graph[A][B] = 1; G1.graph[A][2] = 1; G1.graph[A][4] = 1
# G1.graph[B][2] = 1; G1.graph[B][3] = 1; G1.graph[B][3] = 1
# G1.graph[C][2] = 1; G1.graph[C][3] = 1; G1.graph[C][3] = 1
# G1.graph[D][2] = 1; G1.graph[D][3] = 1; G1.graph[D][3] = 1
# G1.graph[E][2] = 1; G1.graph[E][3] = 1; G1.graph[E][3] = 1
# G1.graph[F][2] = 1; G1.graph[F][3] = 1; G1.graph[F][3] = 1
# G1.graph[G][2] = 1; G1.graph[G][3] = 1; G1.graph[G][3] = 1
# G1.graph[H][2] = 1; G1.graph[H][3] = 1; G1.graph[H][3] = 1
# G1.graph[I][G] = 1; G1.graph[I][H] = 1
#
#
# current = 0
# queue.append(current)  # enqueue
# visited_array.append(current)
#
# while len(queue) != 0:
#     next = None
#     for vertex in range(4):
#         if G1.graph[current][vertex] == 1:
#             if vertex in visited_array:
#                 pass
#             else:
#                 next = vertex
#                 break
#
#     if next is not None:
#         current = next
#         queue.append(current)  # enqueue
#         visited_array.append(current)
#     else:
#         # current = queue.pop(0)  # O(n), OVERHEAD
#         current = queue.popleft()  # O(1), dequeue
#
#
# for i in visited_array:
#     print(i, end=' --> ')
# print("END")

