# 두 정수 사이의 소수를 출력하는 코드를 while문으로 만들어보자.
start = int(input("start number : "))
end = int(input("end number : "))

if end < start:
    start, end = end, start

k = 1
while k <= end:
    if i <= 1:
        continue
    if i % k == 0:
         break
    else:
        print(i, end=' ')