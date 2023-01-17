# 두 정수 사이의 소수를 출력하는 코드를 while문으로 만들어보자.
start = int(input("start number : "))
end = int(input("end number : "))

if end < start:
    start, end = end, start

i = start
while i < end+1:
    if i <= 1:
        i += 1
        continue
    k = 2
    while k < i:
        if i % k == 0:
            break
        k +=1
    else:
        print(i, end=' ')
    i +=1
