# 9.3
def test(func):
    def new_func(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return new_func

@test
def greeting():
    print("Greetings, Earthling")

print(greeting())

# 9.4

class OopsException(Exception):
    def __init__(self):
        super().__init__('Caught an oops')

def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        if x % 3 != 0:
            raise OopsException
        print(x)
    except Exception as e:
        print('예외가 발생했습니다.', e)
three_multiple()