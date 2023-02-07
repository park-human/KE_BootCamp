## 함수 선언 ##
def isQueueFull():
	global SIZE, queue, front, rear
	if (rear == SIZE-1):
		return True
	else:
		return False
def isQueueEmpty():
	global SIZE, queue, front, rear
	if (front == rear):
		return True
	else:
		return False

def enQueue(data):
	global SIZE, queue, front, rear
	if (isQueueFull()):
		print("큐가 꽉 찼습니다.")
		return
	rear += 1
	queue[rear] = data
def deQueue():
	global SIZE, queue, front, rear
	if (isQueueEmpty()):
		print("큐가 비었습니다.")
		return None
	front +=1
	data = queue[front]
	queue[front] = None

	for i in range(front+1, rear+1):
		queue[i-1] = queue[i]
		queue[i] = None
	front = -1
	rear -= 1

	return data

def peek():
	global SIZE, queue, front, rear
	if (isQueueEmpty()) :
		print('큐가 비었습니다.')
		return None
	return queue[front+1]

# 7장 응용예제 01

## 전역 변수 선언 ##
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

## 메인 코드 ##
if __name__ == "__main__":
	enQueue('손님1')
	enQueue('손님2')
	enQueue('손님3')
	enQueue('손님4')
	enQueue('손님5')
	print('대기 줄 상태 : ',queue)

	for _ in range(rear+1):
		print(deQueue(), '님 식당에 입장')
		print('대기 줄 상태 : ', queue)

	print('영업 종료')

# 7장 응용예제 02