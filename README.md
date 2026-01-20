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








