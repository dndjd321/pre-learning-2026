# fileWrite.py - 파일 쓰기

# open('파일경로', '모드')
# 모드 : w(쓰기), r(읽기), a(추가)

# 파일 열기
file = open("./DAY03/myFirstFile.txt", "w")

# 파일 내용 작성
file.write("Hello, Python.\n")
file.write("Python file I/O is fun.\n")
file.write("I'm student.\n")

# 파일 닫기
file.close()

print("myFirstFile.txt 파일 작성 완료.")

# 문자열을 여러개 담은 리스트(배열)
lines = ["안녕하세요\n", "반갑습니다.\n", "파이썬입니다.\n"]

# 인코딩 : 글자체계, UTF-8 : 전 세계 언어를 표현할 수 있는 인코딩 형식
file2 = open("./DAY03/mySecondFile.txt", "w", encoding="UTF-8")
file2.writelines(lines)
file2.close()
print("mySecondFile.txt 파일 작성 완료.")


