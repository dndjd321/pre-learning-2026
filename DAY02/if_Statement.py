# if_Statement.py - 제어문 -> 조건문 if
# 제어문 중 최초로 만들어진 것이 if 문
# if 조건 :
#   처리할 내용
# else :
#   처리할 내용


age = 16

print("담배주세요")
if age > 19:    # 항상 참인 조건
    print("담배를 산다")
else:           # 항상 거짓인 조건
    print("민증주세요")

print()

bloodType = 'A' # B, AB, O

if bloodType == 'A':
    print("A형입니다.")
elif bloodType == 'B':
    print("B형입니다.")
elif bloodType == 'AB':
    print("AB형입니다.")
elif bloodType == 'O':
    print("O형입니다.")
else:
    print("???")


print()

is_adult = True
is_gender = "Female"

# 이중 if문으로 분기
if is_adult == True :
    print("대인입니다. 20,000원 입니다")

    if is_gender == "Male":
        print("남탕으로 가세요.")
    else :
        print("여탕으로 가세요.")
else:
    print("소인입니다. 12,000원 입니다")

    if is_gender == "Male":
        print("남탕으로 가세요.")
    else :
        print("여탕으로 가세요.")


print()

# and 논리연산자로 분기
is_adult = False
is_gender = "Male"

if is_adult == True and is_gender == "Male":
    print("대인, 남자입니다. 20,000원 입니다.")
elif is_adult == True and is_gender == "FeMale":
    print("대인, 여자입니다. 20,000원 입니다.")
elif is_adult == False and is_gender == "Male":
    print("소인, 남자입니다. 12,000원 입니다.")
elif is_adult == False and is_gender == "FeMale":
    print("소인, 여자입니다. 12,000원 입니다.")
else:
    print("무료")


print(not is_adult)






