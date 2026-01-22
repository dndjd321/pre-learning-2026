# fileRead.py - 파일 읽기

# 파일 오픈(읽기모드)
file = open("./DAY03/mySecondFile.txt", "r", encoding="UTF-8")

# 파일 읽기 - 파일을 하나의 문자열로 읽어서 변수 content에 담는다
content = file.read()

# txt 파일 용량이 너무 클 경우에는 내용을 읽어오는 도중에 비정상 종료됨
print(content)

# 파일 닫기
file.close()

print("파일 한 번에 읽기 완료")

print()

# 파일 오픈(읽기모드)
file2 = open("./DAY03/myFirstFile.txt", "r", encoding="UTF-8")

# 파일 한 줄씩 읽기 
while(True):
    line = file2.readline()
    if not line:
        break
    
    print(line, end="")


# 파일 닫기
file2.close()

print("파일 한 줄씩 읽기 완료")
