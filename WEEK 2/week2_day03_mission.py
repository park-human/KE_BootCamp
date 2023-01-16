# 연습문제 5.4 / 5.5

letter = '''Dear {situation} {name},

Thank you for your letter. We are sorry that our {product} {verbed} in your {room}. Please note that it should never be used in a {room}, especially near any {animals}.

Send us your receipt and {amount} for shipping and handling. We will send you another {product} that, in our tests, is {percent}% less likely to have {verbed}.

Thank you for your not support.
Sincerely,
{spokesman}
{job_title}'''

print(letter.format(situation='customer',name='Hayeon',product='computer',verbed='crashed',room='bathtub',animals='cats',amount='$100',percent='70',spokesman='Cassidy',job_title='Manager'))

# 연습문제 5.6
names = ['duck', 'gourd', 'spitz']
for name in names:
    cap_name = name.capitalize()
    print('%sy Mc%sface' % (cap_name, cap_name))
print()

# 연습문제 5.7 - format
names = ['duck', 'gourd', 'spitz']
for name in names:
    cap_name = name.capitalize()
    print('{}y Mc{}face'.format(cap_name, cap_name))
print()

# 연습문제 5.8 - f-문자열
names = ['duck', 'gourd', 'spitz']
for name in names:
    cap_name = name.capitalize()
    print(f'{cap_name}y Mc{cap_name}face')
print()

# 연습문제 6.2
guess_me = 7
number = 1
while True:
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    elif number > guess_me:
        print('oops')
        break
    number += 1

# 연습문제 6.3
guess_me = 5
number = 0
for number in range(10):
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    elif number > guess_me:
        print('oops')
        break