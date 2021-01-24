# 이번에는 문서 파일을 읽어서 그 문서 파일 안에 있는 탭(tab)을 공백(space) 4개로 바꾸어 주는 스크립트를 작성해 보자.

# 필요한 기능은? 문서 파일 읽어 들이기, 문자열 변경하기
# 입력 받는 값은? 탭을 포함한 문서 파일
# 출력하는 값은? 탭이 공백으로 수정된 문서 파일

# 다음과 같은 형식으로 프로그램이 수행되도록 만들 것이다.
python tabto4.py src dst

# tabto4.py는 우리가 작성해야 할 파이썬 프로그램 이름이고 src는 탭을 포함하고 있는 원본 파일 이름이다. 
# dst는 파일 안의 탭을 공백 4개로 변환한 결과를 저장할 파일 이름이다.

# 예를 들어 a.txt 파일에 있는 탭을 4개의 공백으로 바꾸어 b.txt 파일에 저장하고 싶다면 다음과 같이 수행해야 한다.

python tabto4.py a.txt b.txt




### 1. 우선 다음과 같이 tabto4.py 파일을 작성해 보자.
# c:/doit/tabto4.py
import sys

src = sys.argv[1]
dst = sys.argv[2]

print(src)
print(dst)



### 2. 다음과 같이 수행했을 때 입력값이 정상적으로 출력되는지 확인해 보자.

python tabto4.py a.txt b.txt

### 입력으로 전달한 a.txt와 b.txt가 정상적으로 출력되는 것을 확인할 수 있다.




### 3. 테스트를 위한 원본 파일(탭을 포함하는 파일)인 a.txt를 다음과 같이 작성한다. 각 단어는 탭(\t) 문자로 분리되도록 입력해야 한다.
Life    is  too short
You need    pyhton



### 4. 이제 탭 문자를 포함한 a.txt 파일을 읽어서 탭을 공백 4개로 변환할 수 있도록 코드를 변경해 보자.
# c:/Python/doit/tabto4.py
import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " "*4)
print(space_content)

### 위 코드는 src에 해당되는 입력 파일을 읽어서 그 내용을 tab_content라는 변수에 저장한 후
### 문자열의 replace 함수를 사용하여 탭(\t)을 4개의 공백으로 변경하는 코드이다.



### 5. tabto4.py를 위와 같이 변경한 후 다음과 같은 명령을 수행해 보자.
python tabto4.py a.txt b.txt

### 아마도 탭 문자가 공백 4개로 변경되어 출력될 것이다. 
### 하지만 탭과 공백의 차이점을 눈으로 알 수는 없으므로 탭이 정상적으로 공백으로 변경되었는지 확인하기 어렵다.




### 6. 이제 변경된 내용을 b.txt파일에 저장할 수 있도록 다음과 같이 프로그램을 변경해 보자.

# c:Pyhton/doit/tabto4.py
import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("/t", " "*4)

f = open(dst, "w")
f.write(space_content)
f.close()

### 탭이 공백으로 변경된 space_content를 출력 파일인 dst에 쓰도록 코드를 수정하였다.




### 7. 프로그램을 실행하기 위해 다음 명령을 수행한다.
python tabto4.py a.txt b.txt


### 위 명령을 수행하면 b.txt 파일이 C:\doit 디렉터리에 생성된다. 
### 에디터로 b.txt 파일을 열어서 탭이 4개의 공백 문자로 변경되었는지 확인해 보자. 
### 프로그램을 작성할 때 사용하는 에디터는 대부분 탭과 공백 문자를 다르게 표시하므로 눈으로 확인이 가능할 것이다.