# input 2 numbers

#start = int(input("start number : "))
#end = int(input("end number : "))
#print(start, end)

#start_end = input("start and end number : ").split()
#print(start_end)
#print(int(start_end[0]), int(start_end[1]))

#start = int(input("start number : "))
#end = int(input("end number : "))
#print(start, end)
#for k in range(start, end+1):
#    print(k, end=' ') # 줄바꿈 대신에 띄어쓰기

# 두 수 사이의 소수를 출력한다
start = int(input("start number : "))
end = int(input("end number : "))

if end < start:
	start, end = end, start

for i in range(start, end+1): # i는 start부터 end+1까지이다.
	if i <= 1:
		continue                  # 1은 소수가 아니므로 1을 입력시 무시한다. (i +1)
	for k in range(2, i):
		if i % k == 0:            # i를 k로 나눴을 때 0이 나오면 소수가 아니다
			break
	else:
		print(i, end=' ')
print()
print(i)

# ex. 6-1
for k in [3, 2, 1, 0]:
	print(k)