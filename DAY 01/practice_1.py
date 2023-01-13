subjects = {
    '실용영어 L/S' : 'A+',
    '영문학개론' : 'B',
    '서구문화원형과 미디어' : 'C'
    }
#grade = '영문학개론'
#print(grade,"과목의 성적은", subjects[grade],"입니다.")

grade = subjects[input("성적 조회: ")]

print("해당 과목의 성적은",grade,"입니다.")

# f-string
print(f"해당 과목의 성적은 {grade} 입니다.")
