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