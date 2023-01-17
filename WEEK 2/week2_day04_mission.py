# 7장
year_lists = [1999,2000,2001,2002,2003,2004]
print(f'7.2: year_lists의 세 번째 생일은 {year_lists[3]}년도이다.')
print(f'7.3: year_lists 중 가장 나이가 많을 때는 {year_lists[-1]}년도이다.')
things = ['mozarella', 'cinderella', 'salmonella']
print('7.5:', things[1].capitalize(), things,', 변경되지 않는다.')
print('7.6 :', things[0].upper())
things.remove('salmonella')
print('7.7 :', things)
surprise = ['Groucho', 'Chico', 'Harpo']
surprise[-1] = surprise[-1].lower()
surprise[-1] = surprise[-1][::-1]
surprise[-1] = surprise[-1].capitalize()
print('7.9 : ',surprise[-1])

even_list = [number for number in range(10) if number % 2 == 0]
print('7.10 : ',even_list)

print('7.11 :')
start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a map"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog","walk the dog"),
    ("fun", "say we're done")
    ]
start2 = "Someone better"

start1_caps=" ".join([word.capitalize() + "!" for word in start1])
for first, second in rhymes:
    print(f"{start1_caps} {first.capitalize()}!")
    print(f"{start2}{second}")

# 8장

#8.1
e2f = {'dog':'chein', 'cat':'chat','walrus':'morse'}
#8.2
print(e2f['walrus'])
#8.3
f2e = {v:k for k, v in e2f.items()}
#8.4
print(f2e['chein'])
#8.5
for value in f2e.values():
    print(value)
#8.6
life = {
    'animals':{
        'cats':[
            'Henri',
            'Grumpy',
            'Lucy'
        ],
        'octopi':{},
        'emus':{}
    },
    'plants':{},
    'other':{}
}
#8.7
print(life.keys())
#8.8
print(life['animals'].keys())
#8.9
print(life['animals']['cats'])
#8.10
squares = {key: key ** 2 for key in range(10)}
print(squares)
