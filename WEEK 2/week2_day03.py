# import random
# secret = random.randint(1,10)
# guess = int(input('정답은? :'))
# if secret == guess:
#     print('정답입니다.')
# elif secret > guess:
#     print(f'정답보다 작은 수입니다. 정답은 {secret}.')
# else:
#     print(f'정답보다 큰 수입니다. 정답은 {secret}')

# start = 'Na' * 4 + '\n'
# middle = 'Hey' * 2 + '\n'
# end = 'Goodbye'
# print(start + middle + end)

# name = 'Henny'
# print('P' + name[1:])

# univ = 'Inha University'
#print(univ[8:])
#print(univ[5:15])
#print(univ[:4])
#print(univ[6:10])
#print(univ[0:-1:3])

#pirates_list = ['Luffy', 'Law', 'Captain Kid']
#pirates_string = ', '.join(pirates_list)
#print('Captain Trio:',pirates_string)

# 연습문제 5.1
song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""
song = song.replace(' m'," M")
print(song)
print()

# 연습문제 5.2

questions = [
"We don't serve strings around here. Are you a string?",
"What is said on Father's Day in the forest?",
"What makes the sound 'Sis! Boom! Bah!'?"
]
answers = [
"An exploding sheep.",
"No, I'm a frayed knot.",
"'Pop!' goes the weasel."
]

q_a = ((0,1),(1,2),(2,0))
for q, a in q_a:
    print('Q: ',questions[q])
    print('A: ',answers[a])
    print()

# 연습문제 5.3

poem = """My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s
And now thinks he's a %s."""
words = ('roast beef', 'ham', 'head', 'clam')
print(poem % words)

# 연습문제 5.4

print('''Dear {situation} {name},

Thank you for your letter. We are sorry that our {product} {verbed} in your {room}. Please note that it should never be used in a {room}, especially near any {animals}.

Send us your receipt and {amount} for shipping and handling. We will send you another {product} that, in our tests, is {percent}% less likely to have {verbed}.

Thank you for your not support.
Sincerely,
{spokesman}
{job_title}'''.format(situation='customer',name='Hayeon',product='computer',verbed='crashed',room='bathtub',animals='cats',amount='$100',percent='70',spokesman='Cassidy',job_title='Manager'))