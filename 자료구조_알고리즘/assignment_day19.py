# 10장 응용예제 01
def notation(base, n):
    if n < base:
        print(numberChar[n],end=' ')
    else:
        notation(base,n//base)
        print(numberChar[n%base],end=' ')

numberChar = ['0','1','2','3','4','5','6','7','8','9']
numberChar += ['A','B','C','D','E','F']

number = int(input('10진수 입력 : '))
print('\n 2진수 : ', end = ' ')
notation(2,number)
print('\n 8진수 : ', end = ' ')
notation(8,number)
print('\n 16진수 : ', end = ' ')
notation(16,number)
print()

# 11장 응용예제 01
def scoreSort(ary):
    n = len(ary)
    for end in range(1,n):
        for cur in range(end, 0, -1):
            if (ary[cur-1][1] > ary[cur][1]):
                ary[cur-1],ary[cur]=ary[cur],ary[cur-1]
    return ary

scoreAry = [['학생3',88],['학생1',99],['학생5',71],['학생4',78],['학생6',67],['학생2',92]]

print('정렬 전 : ', scoreAry)
scoreAry = scoreSort(scoreAry)
print('정렬 후 : ', scoreAry)
print('성적별 조 편성표')
for i in range(len(scoreAry)//2):
    print(scoreAry[i][0], ':', scoreAry[len(scoreAry)-1-i][0])

# 12장 응용예제 01
import random
import time

def selectionSort(ary):