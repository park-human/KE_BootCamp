# import webbrowser
# import time
#
# def is_stack_full():
#     global SIZE, stack, top
#     if top >= SIZE -1 :
#         return True
#     else:
#         return False
#
# def is_stack_empty():
#     global SIZE, stack, top
#     if top == -1:
#         return True
#     else:
#         return False
#
# def push(data):
#     global SIZE, stack, top
#     if is_stack_full():
#         print("Stack is FULL!")
#         return
#     top = top + 1
#     stack[top] = data
#
# def pop():
#     global SIZE, stack, top
#     if is_stack_empty():
#         print("Stack is EMPTY!")
#         return
#     temp = stack[top]
#     stack[top] = None
#     top = top - 1
#     return temp
#
# def peek():
#     global SIZE, stack, top
#     if is_stack_empty():
#         print("Stack is EMPTY!")
#         return None
#     return stack[top]
#
# # SIZE = 5
# # stack = [None for _ in range(SIZE)]
# # top = -1
# #
# # if __name__ == "__main__":
# #     urls = ['inha.ac.kr', 'yale.edu', 'harvard.edu']
# #
# #     for url in urls:
# #         push(url)
# #         webbrowser.open('http://' + url)
# #         print(url, end = '-->')
# #         time.sleep(1)
# #
# #     print("방문 종료")
# #     time.sleep(5)
# #
# #     while True:
# #         url = pop()
# #         if url == None:
# #             break
# #         webbrowser.open('http://'+ url)
# #         print(url, end = '->')
# #         time.sleep(1)
# #     print('방문 종료')
#
# def checkBracket(expr):
#     for ch in expr:
#         if ch in '([{<':
#             push(ch)
#         elif ch in ')]}>':
#             out=pop()
#             if ch == ')' and out == '(':
#                 pass
#             elif ch == ']' and out == '[':
#                 pass
#             elif ch == '}' and out == '{':
#                 pass
#             elif ch == '>' and out == '<':
#                 pass
#             else:
#                 return False
#         else:
#             pass
#     if is_stack_empty():
#         return True
#     else:
#         return False

# SIZE = 5
# stack = [None for _ in range(SIZE)]
# top = -1
#
# if __name__ == "__main__":
#     expression_array = ['(2*[3+1)', '(A+B)', ')A+B(', '(A+B]', '(<A+[B-V}/[C*D]>)']
#     for expr in expression_array :
#         top = -1
#         print(expr, "->", checkBracket(expr))

# ## 함수 선언 부분 ##
# def is_queue_full():
#     global SIZE, queue, front, rear
#     if ((rear+1) % SIZE == front) :
#         return True
#     else:
#         return False
#
# def is_queue_empty():
#     global SIZE, queue, front, rear
#     if (front == rear):
#         return True
#     else:
#         return False
#
# def push(data):
#     global SIZE, queue, front, rear
#     if is_queue_full():
#         print("Queue is FULL!")
#         return
#     top = top + 1
#     stack[top] = data
#
# def enQueue(data):
#     global SIZE, queue, front, rear
#     if is_queue_empty():
#         print("Queue is EMPTY!")
#         return
#     rear = (rear+1) % SIZE
#     queue[rear] = data
#
# def deQueue():
# 	global SIZE, queue, front, rear
# 	if (is_queue_empty()):
# 		print('Queue is EMPTY!')
# 		return None
# 	front = (front+1) % SIZE
# 	data = queue[front]
# 	queue[front] = None
# 	return data
#
# def peek():
#     global SIZE, queue, front, rear
#     if (is_stack_empty()):
#         print("Stack is EMPTY!")
#         return None
#     return queue[(front+1) % SIZE]
#
# ## 전역 변수 선언 부분 ##
# SIZE = int(input("큐 크키를 입력하세요 : "))
# queue = [None for _ in range(SIZE)]
# front = rear = 0
#
# ## 메인 코드 부분 ##
# if __name__ == "__main__":
#     select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 : ")
#
#     while (select != 'X' and select !='x'):
#         if select == 'I' or select == 'i':
#             data = input('입력할 데이터 : ')
#             enQueue(data)
#             print("큐 상태 : ", queue)
#             print("front : ", front, ", rear : ", rear)
#
#         elif select == 'E' or select == 'e':
#             data = deQueue()
#             print("추출된 데이터 : ", data)
#             print("큐 상태 : ", queue)
#             print("front : ", front, ", rear : ", rear)
#
#         elif select == "V" or select == "v":
#             data = peek()
#             print("확인된 데이터 : ", data)
#             print("큐 상태 : ", queue)
#             print("front : ", front, ", rear : ", rear)
#         else:
#             print('입력이 잘못됨')
#
#         select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 입력 : ")
#     print('프로그램 종료!')

# TreeNode
class TreeNode(): # 이진 트리 노드 생성
	def __init__ (self):
		self.left = None
		self.data = None
		self.right = None

node1 = TreeNode()
node1.data = 'Pirate'

node2 = TreeNode()
node2.data = 'Mugiwara'
node1.left = node2

node3 = TreeNode()
node3.data = 'Heart'
node1.right = node3

node4 = TreeNode()
node4.data = 'Luffy'
node2.left = node4

node5 = TreeNode()
node5.data = 'Zoro'
node2.right = node5

node6 = TreeNode()
node6.data = 'Law'
node3.left = node6

def preorder(node):
	if node == None:
		return
	print(node.data, end = '->')
	preorder(node.left)
	preorder(node.right)

def inorder(node):
	if node == None:
		return
	inorder(node.left)
	print(node.data, end = '->')
	inorder(node.right)

def postorder(node):
	if node == None :
		return
	postorder(node.left)
	postorder(node.right)
	print(node.data, end = '->')

print('전위 순회 : ', end = ' ')
preorder(node1)
print('끝')

print('중위 순회 : ', end = ' ')
inorder(node1)
print('끝')

print('후위 순회 : ', end = ' ')
postorder(node1)
print('끝')