# import webbrowser
# import time

def is_stack_full():
    global SIZE, stack, top
    if top >= SIZE -1 :
        return True
    else:
        return False

def is_stack_empty():
    global SIZE, stack, top
    if top == -1:
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if is_stack_full():
        print("Stack is FULL!")
        return
    top = top + 1
    stack[top] = data

def pop():
    global SIZE, stack, top
    if is_stack_empty():
        print("Stack is EMPTY!")
        return
    temp = stack[top]
    stack[top] = None
    top = top - 1
    return temp

def peek():
    global SIZE, stack, top
    if is_stack_empty():
        print("Stack is EMPTY!")
        return None
    return stack[top]

# SIZE = 5
# stack = [None for _ in range(SIZE)]
# top = -1
#
# if __name__ == "__main__":
#     urls = ['inha.ac.kr', 'yale.edu', 'harvard.edu']
#
#     for url in urls:
#         push(url)
#         webbrowser.open('http://' + url)
#         print(url, end = '-->')
#         time.sleep(1)
#
#     print("방문 종료")
#     time.sleep(5)
#
#     while True:
#         url = pop()
#         if url == None:
#             break
#         webbrowser.open('http://'+ url)
#         print(url, end = '->')
#         time.sleep(1)
#     print('방문 종료')

def checkBracket(expr):
    for ch in expr:
        if ch in '([{<':
            push(ch)
        elif ch in ')]}>':
            out=pop()
            if ch == ')' and out == '(':
                pass
            elif ch == ']' and out == '[':
                pass
            elif ch == '}' and out == '{':
                pass
            elif ch == '>' and out == '<':
                pass
            else:
                return False
        else:
            pass
    if is_stack_empty():
        return True
    else:
        return False

SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1

if __name__ == "__main__":
    expression_array = ['(2*[3+1)', '(A+B)', ')A+B(', '(A+B]', '(<A+[B-V}/[C*D]>)']
    for expr in expression_array :
        top = -1
        print(expr, "->", checkBracket(expr))