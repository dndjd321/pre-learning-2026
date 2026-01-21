# while_Statement.py - 제어문 -> 반복문 while
# while(조건이 참인 동안):
#   반복문

import time


# 카운트 다운
# count = 10
# while count > 0:
#     print(count)
#     count = count - 1
#     time.sleep(1)

# print("발사")


# count = 1
# while count > 0:
#     print(count)
#     count = count + 1
#     time.sleep(0.2)

# print("프로그램 종료")


# 입력에 따른 프로그램 종료
# count = 1
# while True:
#     user_Input = input("종료하려면 exit를 입력하세요.")

#     if(user_Input == "exit"):
#         print("반복문 탈출")
#         break
#     else:
#         count = count + 1
#         print(count)
#         print("사용자 입력 : " + user_Input)

# print("프로그램 종료")


# continue : 어떤 조건만 뛰어넘고 반복 진행
number = 0

while (number < 10):    # number가 11보다 적을 동안
    number += 1         # number = number + 1과 동일
    if (number == 3 or number == 6 or number == 9):
        print("짝")
        continue

    print(number)

print("프로그램 종료")




