# functions.py - 함수
# def 함수명 ([매개변수]):
#   함수 내 로직(코드 작성)
# 매개변수 == 파라미터(parameter) == 아규먼트(Argument)

# 기본 정의되어 있는 함수 사용 ( 내장함수 )
print()
print("Hello, Python")
print(str(10))

# 함수 정의
def Say_hello():
    #   pass    # pass는 코드 오류를 방지하는 장치
    print("Hello, everyone.")
    #   return None 이 숨겨져 있는 형태

# 매개변수 1개 사용
def Say_hello2(name):
    print("Halo, I'm " + name)

# 매개변수 2개 사용
def Add(x, y):
    result = x + y
    return result

# 매개변수 없이 반환
def Process():
    result = "Done"
    return result

# 함수 호출
Say_hello()
Say_hello2("Joon")
print(str(Add(10,5)))
print(Process())




