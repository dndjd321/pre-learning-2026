# functions.py - 내장함수
# import 모듈명

import math # 수학과 관련된 함수와 데이터를 담고있는 모듈

pi = 3.141592
radius = 10

result = pi * radius * radius

print("원의 넓이 : " + str(result))

result = radius * radius * math.pi
print(math.pi)
print("원의 넓이 : " + str(result))
