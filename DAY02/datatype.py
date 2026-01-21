# datatype.py - 자료형

int_val = 10        # 정수형
pi_val = 3.14       # 실수형
str_val = "Hugo"    # 문자열 - Python에서 문자열은 '', "" 둘 다 사용.
                    # C, C++, C#, Java 등은 홑따옴표, 쌍따옴표가 다르게 동작
bool_val = False    # 불리언 ( 참, 거짓 )
                    # False == 0, True != 0 ( 보통은 1로 취급 )

print(int_val)
print(pi_val)
print(str_val)
print(bool_val)

print(str_val + str(pi_val))    # int_val은 정수형(숫자)이므로 문자열과 같이 
                                # 출력이 되고자 하면, 문자열로 치환이 필요함.



myName = "구병준"
myAge = 27
myHeight = 176.5

print("이름 : " + myName + ", 나이 : " + str(myAge) + ", 키 : " + str(myHeight) + "cm")

