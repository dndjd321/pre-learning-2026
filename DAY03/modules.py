# functions.py - 내장함수
# import 모듈명

import math     # 수학과 관련된 함수와 데이터를 담고있는 모듈
import datetime # 날짜, 시간과 관련된 함수와 데이터를 담고있는 모듈

pi = 3.141592
radius = 10

result = pi * radius * radius

print("원의 넓이 : " + str(result))

result = radius * radius * math.pi
print(math.pi)
print("원의 넓이 : " + str(result))

print(math.sqrt(16))
print(math.floor(4.8))  # 숫자 내림
print(math.ceil(4.1))   # 숫자 올림

print(datetime.datetime.now())

# 내장 함수
# 배열, 문자열 길이 리턴 함수
print(len("Hello"))
print(len([0,1,2,3,4]))

# 데이터형 리턴 함수
print(type(1))
print(type(pi))
print(type([0,1,2,3,4]))
print(type("Hello"))

print(int("80"))        # 정수형으로 형변환
print(float("4"))       # 실수형으로 형변환
print(str(3.141592))    # 문자열로 형변환


