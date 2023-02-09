# # Code08-03 이진 탐색 트리의 삽입 작동
#
# ## 함수 선언 ##
# class TreeNode():
#     def __init__(self):
#         self.left = None
#         self.data = None
#         self.right = None
#
# ## 전역 변수 선언 ##
# memory = []
# root = None
# nameAry = ['커피','녹차','홍차','주스','물','콜라'] # 루트 노드의 데이터 : '커피'
#
# ## 메인 코드 ##
# node = TreeNode()
# node.data = nameAry[0]
# root = node
# memory.append(node) # 이름 배열의 첫 데이터를 루트 노드로 생성하고 메모리에 넣음
#
# for name in nameAry[1:]: # 이름 배열의 2번째부터 처리
#
#     node = TreeNode() # 새 노드 생성
#     node.data = name
#
#     current = root # 현재 작업 노드는 항상 루트 노드(커피)부터 시작
#     while True: # 새 노드가 자리를 찾을 때까지 무한 반복
#         if name < current.data:
#             if current.left == None: # 새 작업 노드가 작을 때는 왼쪽으로 진행
#                 current.left = node
#                 break
#             current = current.left # 현재 작업 노드를 왼쪽 자식 노드로 변경
#         else:
#             if current.right == None: # 새 작업 노드가 클 때는 오른쪽으로 진행
#                 current.right = node
#                 break
#             current = current.right
#     memory.append(node) # 위치를 찾아 자리를 잡은 새 노드를 메모리 공간에 넣음
# print("이진 탐색 트리 구성 완료!")
#
# # Code08-04 이진 탐색 트리의 검색 작동
# findName = '커피'
#
# current = root
# while True:
#     if findName == current.data :
#         print(findName, '을(를) 찾음.')
#         break
#     elif findName < current.data :
#         if current.left == None:
#             print(findName, '이(가) 트리에 없음')
#             break
#         current = current.left
#     else:
#         if current.right == None:
#             print(findName, '이(가) 트리에 없음')
#             break
#         current = current.right

def printStar(n):
    if n>=1:
        print('★' * n)
        printStar(n-1)
printStar(5)