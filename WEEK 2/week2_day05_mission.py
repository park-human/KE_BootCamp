# 8
# 9-1
def good():
    return ['Harry', 'Ron', 'Hermione']

print(good())

# 9-2
def get_odds():
    for number in range(1, 10, 2):
        yield number

count = 1
for number in get_odds():
    if count == 3:
        print("3번째 홀수는", number)
        break
    count +=1