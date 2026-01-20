# pre-learning-2026
부경대 IoT 개발자 과정 사전학습 리포지토리

## 1일차
- 과정소개
- 학습 리포지토리 생성
- 마크다운 학습
  1. 제목
    ```markdown
    # 제목1
    ## 제목2
    ### 제목3
    #### 제목4
    ##### 제목5
    ###### 제목6 ( 잘 사용하지 않음 - 기본 폰트보다 작음)
    <!-- 주석(HTML 주석과 동일) -->
    ```

  2. 목록
    ```markdown
    - 목록
    * 목록
    1. 숫자목록
    2. 숫자목록
    ```

  3. 링크, 이미지
    ```markdown
    [네이버](https://www.naver.com)

    ![이미지](imgUrl)

    ## 이미지 사이즈 조절
    src : 이미지 Url
    width : 이미지 가로 사이즈 설정(px)
    <img src="imgUrl" width="500" />
    ```
    - [네이버](https://www.naver.com)
    
    - ![이미지](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRr_-62a40u3lSIyRP5EKOjJeQiZROwTeVCOQ&s)
    
    - <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRr_-62a40u3lSIyRP5EKOjJeQiZROwTeVCOQ&s" width="400" />
    
    - 이미지와 링크의 차이는 !의 유무로 확인할 수 있음.
    
    - <img width="703" height="463" alt="image" src="https://github.com/user-attachments/assets/f52bf34a-08c1-4af0-b785-dab583d4be31" />

 
  4. 가로줄
     ```markdown
     ---
     ```
---
  5. 코드 블럭
     - 소스코드를 작성할 때 코드 하이라이터, 영역표시 할 때 사용.
     - 백틱('`') 1회 또는 3회 입력 시 사용.
     - 3회 입력 시에는 백틱 사이에 표시언어를 입력
     ```python
     print('Hello, Python!')
     ```
     - 1회 입력 시에는 일반적인 문장에서 한 단어를 강조하고 싶을때 `인라인 코드블럭`을 사용
    
  6. 단어 강조 및 밑줄
     ```markdown
     **, ~~, __, html의 u 태그, html i 태그
     ```
     - 문장을 작성할 시 **강조**, ~~취소선~~, __강조2__, <u>밑줄</u>, <i>이태릭</i> 을 사용할 수 있습니다.


- GitHub local Repository 생성
  1. Git for Windows 설치
     - https://git-scm.com/ 에서 `Install for Windows` 클릭
     - Standalone Installer -> Git for Windows/x64 Setup 클릭
     - Git 설치 옵션은 기본 세팅 그래도 사용 가능(변경X)
     - cmd 또는 powershell 에서 `git --version` 또는 `git -v` 명령어로 확인
  2. GitHub Desktop 설치
     - https://desktop.github.com/download/ 에서 다운로드(Download for Windows) 클릭 후 설치
     - 계정 브라우저 연동
  3. GitHub Repository Clone
     - GitHub Desktop 메뉴 -> Clone Repository 클릭 -> GitHub.com 탭에서 저장소 검색 후 선택
       -> Local Path 지정 후 아래에 나오는 `Clone` 버튼 클릭

- Visual Studio Code 설치
  1. https://code.visualstudio.com/ 에서 Download for Windows 버튼 클릭
  2. 설치 `C:\DEV\IDE\MicroSoft VS Code`에 설치
  3. Extensions -> Korean Pack for Visual Studio Code 설치 후 재시작

- 추가 설치 프로그램
  1. Notepad++ 에디터 - https://notepad-plus-plus.org/downloads/
  2. 픽픽 - https://picpick.net/

- **Python** 개발환경 설정
  1. https://www.python.org/ 에서 Download의 Python 3.1x.x 버튼 클릭
  2. Installer -> `Add python.exe to PATH` 체크 활성화 후 `Customize Installation` 클릭
  3. Documentation 체크 해제, for all users 체크 활성화 후 Next 클릭
  4. Advanced Options 에서 Install Python 3.1x for all users 체크 활성화
  5. Advanced Options > Customize install location 경로 변경 ex) C:\DEV\LANG\Python314
     <img width="656" height="415" alt="image" src="https://github.com/user-attachments/assets/9d38f1a5-6ad1-46fa-b92c-e44f2f045d59" />
  
  6. Setup was Successful(설치완료) 후 Disable path length limit 클릭(필수)
     <img width="656" height="415" alt="image" src="https://github.com/user-attachments/assets/15c3ab86-8c26-4574-a88e-beb039bea1cd" />
     
  7. cmd 또는 powershell 열고, `python --version` 명령어 입력 후 확인
  8. Visual Studio Code -> Extensions(확장) 에서 Python 검색 후 설치
  9. VS Code 재오픈 폴더 생성
     

- 프로그램 개발 개념















