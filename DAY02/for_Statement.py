# for_Statement.py - 제어문 -> 반복문 for
# for 변수 in 범위:
#   반복할 구문 

print(range(5))
print(list(range(5)))

for i in range(5):  # -> range(0, 5) => [0, 1, 2, 3, 4]
    print(i, end=" ")

print()

for i in range(1, 6):   # -> range(1, 6) => [1, 2, 3, 4, 5]
    print(i, end=" ")


print()

for i in range(5, 0, -1):   # -> range(5, 0, -1) => [5, 4, 3, 2, 1]
    print(i,end=" ")

print()

print("구구단")
for i in range(2, 10, 1):       # 2부터 10 미만까지 1씩 증가
    print(str(i) + "단 :" , end=" ")

    for k in range(1, 10, 1):   # 1부터 10 미만까지 1씩 증가
        print(str(i) + " * " + str(k) + " = " + str(i*k) + " " , end=" ")
    
    print()

print("구구단 종료")

print()


# 성적판별
score = int(input("점수를 입력하세요 >> ")) # 키보드 입력은 무조건 문자열로 되기 때문에
                                            # 숫자형으로 형변환 해줘야함.

if score >= 90:
    print("A학점입니다.")
elif score >= 80:
    print("B학점입니다.")
elif score >= 780:
    print("C학점입니다.")
else:
    print("F학점입니다.")


# # 예제 1
# for i in range(5):
#     print("안녕하세요.")


# # 예제 2
# total_score = 0
# scores = [88, 92, 75, 60, 95]
# for score in scores:
#     print("점수 : " + str(score))
#     total_score += score

# print("총 점수 : " + str(total_score))


# # 예제 3
# for i in range(1, 21, 1):
#     if(i % 3 == 0):
#         print(str(i) + " ", end=" ")
#     else:
#         continue

# print()


