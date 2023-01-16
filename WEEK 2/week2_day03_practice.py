#prime number

number = int(input("input number : "))
counts = 0

k = 1
while k <=10:
    if number % k == 0:
        counts += 1
    k += 1
if counts == 2:
    print(f'{number} is a prime number!')
else:
    print(f'{number} is NOT a prime number.')

# for
number = int(input("input number : "))
counts = 0

for k in range(1, number+1):
    if number % k == 0:
        counts = counts +1
if counts == 2:
    print(f'{number} is a prime number!')
else:
    print(f'{number} is NOT a prime number.')

#prime number v0.3 loopcounts ==

number = int(input("input number : "))
counts = 0

for k in range(2, number):
    if number % k == 0:
        counts = counts + 1

if counts: # 0이 아니면
    print(f'{number} is NOT a prime number.')
else:
    print(f'{number} is a prime number.')

#prime number v0.4 boolean type + break

number = int(input("input number : "))
is_prime = True

for k in range(2, number):
    if number % k == 0:
        is_prime = False
        break # 소수 아니라는 결과 나오면 k반복문 일찍 멈추기 → 소수가 아닐때 성능 향상
    #prink(k)
if is_prime:
    print(f'{number} is a prime number!')
else:
    print(f'{number} is NOT a prime number.')

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