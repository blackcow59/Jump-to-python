##### sys
### sys 모듈은 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈이다.

## 명령 행에서 인수 전달하기 - sys.argv
# C:/User/home>python test.py abc pey guido
# 명령 프롬프트 창에서 위 예처럼 test.py 뒤에 또 다른 값을 함께 넣어주면 sys.argv 리스트에 그 값이 추가된다.

# C:/Python/doit/mymod 에 저장
# argv_test.py
import sys
print(sys.argv)

# 명령 프롬프트 창에서 Mymod 디렉터리로 들어간 뒤 다음과 같이 실행해 보자.

# C:/doit/Mymod>python argv_test.py you need python
['argv_test.py', 'you', 'need', 'python']


## 강제로 스크립트 종료하기 - sys.exit
sys.exit()


## 자신이 만든 모듈 불러와 사용하기 -sys.path
import sys
sys.path

# path_append.py
import sys
sys.path.append("C:/Python/doit/mymod")

# 위와 같이 파이썬 프로그램 파일에서 sys.path.append를 사용해 경로 이름을 추가할 수 있다. 이렇게 하고 난 후에는 C:/doit/Mymod 디렉터리에 있는 파이썬 모듈을 불러와서 사용할 수 있다.





##### pickle
### pickle은 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈이다. 다음 예는 pickle 모듈의 dump 함수를 사용하여 딕셔너리 객체인 data를 그대로 파일에 저장하는 방법을 보여 준다.

import pickle
f = open("test.txt" ,'wb')
data = {1 : 'python', 2 : 'you need'}
pickle.dump(data, f)
f.close()

# 다음은 pickle.dump로 저장한 파일을 pickle.load를 사용해서 원래 있던 딕셔너리 객체(data) 상태 그대로 불러오는 예이다.
import pickle
f = open("test.txt", 'rb')
data = pickle.load(f)
print(data)



##### os
### OS 모듈은 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈이다.

## 내 시스템의 환경 변수값을 알고 싶을 때 - os.environ

# 시스템은 제각기 다른 환경 변수 값을 가지고 있는데, os.environ은 현재 시스템의 환경 변수 값을 보여 준다.
import os
os.environ

# os.environ은 환경 변수에 대한 정보를 딕셔너리 객체로 돌려준다. 자세히 보면 여러가지 유용한 정보를 찾을 수 있다.

# 돌려받은 객체가 딕셔너리이기 때문에 다음과 같이 호출할 수 있다.
os.environ['PATH']


## 디렉토리 위치 변경하기 -os.chdir
# os.chdir를 사용하면 다음과 같이 현재 디렉토리 위치를 변경할 수 있다.
os.chdir("c:\WINDOWS")


## 디렉토리 위치 돌려받기 -os.getcwd
# os.getcwd는 현재 자신의 디렉토리 위치를 돌려준다.
os.getcwd()


## 시스템 명령어 호출하기 -os.system
# 시스템 자체의 프로그램이나 기타 명령어를 파이썬에서 호출할 수도 있다.
# os.system("명령어")처럼 사용한다. 다음은 현재 디렉터리에서 시스템 명령어 dir을 실행하는 예이다.
os.system("dir")


## 실행한 시스템 명령어의 결괏값 돌려받기 -os.popen
# os.popen은 시스템 명령어를 실행한 결괏값을 읽기 모드 형태의 파일 객체로 돌려준다.
f = os.popen("dir")

# 읽어 들인 파일의 객체 내용을 보기 위해서는 다음과 같이 하면 된다.
print(f.read())


## 기타 유용한 os관련 함수
# os.mkdir(디렉터리) : 디렉터리를 생성한다
# os.rmdir(디렉터리) : 디렉터리를 삭제한다(비어있어야 삭제가능)
# os.unlink(파일) : 파일을 지운다
# os.rename(src, dst) : src라는 이름의 파일을 dst라는 이름으로 바꾼다.





##### shutil
### shutil은 파일을 복사해 주는 파이썬 모듈이다.

# 다음 예시는 src라는 이름의 파일을 dst로 복사한다. 만약 dst가 디렉터리 이름이라면 src라는 파일 이름으로 dst 디렉터리에 복사하고 동일한 파일 이름이 있을 경우에는 덮어쓴다.

import shutil
shutil.copy("src.txt", "dst.txt")





##### glob
### 가끔 파일을 읽고 쓰는 기능이 있는 프로그램을 만들다 보면 특정 디렉터리에 있는 파일 이름 모두를 알아야 할 때가 있다. 이럴 때 사용하는 모듈이 바로 glob이다.

## 디렉터리에 있는 파일들을 리스트로 만들기 - glob(pathname)

# 다음은 C:/Python/doit 디렉터리에 있는 파일 중 이름이 mark로 시작하는 파일을 모두 찾아서 읽어들이는 예이다.
import glob
glob.glob("c:/Python/doit/mark*")





##### tempfile
### 파일을 임시로 만들어서 사용할 때 유용한 모듈이 바로 tempfile이다. 
## tempfile.mkstemp()는 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 돌려준다.

import tempfile
filename = tempfile.mkstemp()
filename


## tempfile.TemporaryFile()은 임시 저장 공간으로 사용할 파일 객체를 돌려준다.
## 이 파일은 기본적으로 바이너리 쓰기 모드(wb)를 갖는다. f.close()가 호출되면 이 파일 객체는 자동으로 사라진다.

import tempfile
f = tempfile.TemporaryFile()
f.close()




##### time
### 시간과 관련된 time 모듈에는 함수가 굉장히 많다. 그중 가장 유용한 몇 가지만 알아보자.


## time.time
# time.time()은 UTC(Universal Time Coordinated 협정 세계 표준시)를 사용하여 현재 시간을 실수 형태로 돌려주는 함수이다.
# 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 돌려준다.
import time
time.time()


## time.localtime
# time.localtime은 time.time()이 돌려준 실수 값을 사용해서 연도, 월, 일, 시, 분, 초, ... 의 형태로 바꾸어 주는 함수이다.
time.localtime(time.time())


## time.asctime
# 위 time.localtime에 의해서 반환된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 돌려주는 함수이다.
time.asctime(time.localtime(time.time()))


## time.ctime
# time.asctime(time.localtime(time.time()))은 time.ctime()을 사용해 간편하게 표시할 수 있다. 
# asctime과 다른 점은 ctime은 항상 현재 시간만을 돌려준다는 점이다.
time.ctime()


## time.strftime
# strftime 함수는 시간에 관계된 것을 세밀하게 표현하는 여러 가지 포맷 코드를 제공한다.
time.strftime('출력할 형식 포맷 코드', time.localtime(time.time()))


# 시간에 관계된 것을 표현하는 포맷 코드

# %a	요일 줄임말 :	Mon
# %A	요일 :	Monday
# %b	달 줄임말 :	Jan
# %B	달 :	January
# %c	날짜와 시간을 출력함 :	06/01/01 17:22:21
# %d	날(day) :	[01,31]
# %H	시간(hour)-24시간 출력 형태 :	[00,23]
# %I	시간(hour)-12시간 출력 형태 :	[01,12]
# %j	1년 중 누적 날짜 :	[001,366]
# %m	달 :	[01,12]
# %M	분 :	[01,59]
# %p	AM or PM :	AM
# %S	초 :	[00,59]
# %U	1년 중 누적 주-일요일을 시작으로 :	[00,53]
# %w	숫자로 된 요일 :	[0(일요일),6]
# %W	1년 중 누적 주-월요일을 시작으로 :	[00,53]
# %x	현재 설정된 로케일에 기반한 날짜 출력 :	06/01/01
# %X	현재 설정된 로케일에 기반한 시간 출력 :	17:22:21
# %Y	년도 출력 :	2001
# %Z	시간대 출력 :	대한민국 표준시
## %%	문자 :	%
# %y	세기부분을 제외한 년도 출력 :	01



# 다음은 time.strftime을 사용하는 예이다.
import time
time.strftime("%x", time.localtime(time.time()))
time.strftime('%c', time.localtime(time.time()))


## time.sleep
# time.sleep 함수는 주로 루프 안에서 많이 사용한다. 이 함수를 사용하면 일정한 시간 간격을 두고 루프를 실행할 수 있다. 다음 예를 보자.
# sleep1.py
import time
for i in range(10) :
    print(i)
    time.sleep(1)





##### calendar
### calendar는 파이썬에서 달력을 볼 수 있게 해주는 모듈이다.

## calendar.calendar(연도)로 사용하면 그해의 전체 달력을 볼 수 있다. 결괏값은 달력이 너무 길어 생략하겠다.
import calendar
print(calendar.calendar(2021))


## calendar.prcal(연도)를 사용해도 위와 똑같은 결괏값을 얻을 수 있다.
calendar.prcal(2021)

# 다음의 예는 2015년 12월의 달력만 보여준다.
calendar.prmonth(2015, 12)


## calendar.weekday
# calendar 모듈의 또 다른 유용한 함수를 보자. 
# weekday(연도, 월, 일) 함수는 그 날짜에 해당하는 요일 정보를 돌려준다. 
# 월요일은 0, 화요일은 1, 수요일은 2, 목요일은 3, 금요일은 4, 토요일은 5, 일요일은 6이라는 값을 돌려준다.
calendar.weekday(2015, 12, 31)


## calendar.monthrange
#  monthrange(연도, 월) 함수는 입력받은 달의 1일이 무슨 요일인지와 그 달이 며칠까지 있는지를 튜플 형태로 돌려준다.
calendar.monthrange(2015, 12)





##### random
### random은 난수(규칙이 없는 임의의 수)를 발생시키는 모듈이다. random과 randint에 대해 알아보자.

# 다음은 0.0 에서 1.0사이의 실수 중에서 난수 값을 돌려주는 예를 보여준다.
import random
random.random()

# 다음 예는 1에서 10사이의 정수 중에서 난수 값을 돌려준다.
random.randint(1, 10)

# 다음 예는 1에서 55 사이의 정수 중에서 난수 값을 돌려준다.
random.randint(1, 55)

# random 모듈을 사용해서 재미있는 함수를 하나 만들어 보자.
# random_pop.py
import random
def random_pop(data) :
    number = random.randint(0, len(data)-1)
    return data.pop(number)

if __name__ == "__main__" :
    data = [1, 2, 3, 4, 5]
    while data : 
        print(random_pop(data))


# 위 random_pop 함수는 리스트의 요소 중에서 무작위로 하나를 선택하여 꺼낸 다음 그 값을 돌려준다. 
# 물론 꺼낸 요소는 pop 메서드에 의해 사라진다.

# random_pop 함수는 random 모듈의 choice 함수를 사용하여 다음과 같이 좀 더 직관적으로 만들 수도 있다.
def random_pop(data) :
    number = random.choice(data)
    data.remove(number)
    return number

# 리스트의 항목을 무작위로 섞고 싶을때는 random.shuffle 함수를 사용하면 된다.
import random
data = [1,2,3,4,5]
random.shuffle(data)
data





##### webbrowser
### webbrowser는 자신의 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈이다. 다음 예제는 웹 브라우저를 자동으로 실행하고 해당 URL인 google.com으로 가게 해 준다.

import webbrowser
webbrowser.open("http://google.com")





[스레드를 다루는 threading 모듈]

# 스레드 프로그래밍은 초보 프로그래머가 구현하기에는 매우 어려운 기술이다. 여기에 잠시 소개했으니 눈으로만 살펴보고 넘어가자.

# 컴퓨터에서 동작하고 있는 프로그램을 프로세스(Process)라고 한다.
# 보통 1개의 프로세스는 한 가지 일만 하지만 스레드(Thread)를 사용하면 한 프로세스 안에서 2가지 또는 그 이상의 일을 동시에 수행할 수 있다.

# 간단한 예제로 설명을 대신하겠다.

# thread_test.py
import time

def long_task():  # 5초의 시간이 걸리는 함수
    for i in range(5):
        time.sleep(1)  # 1초간 대기한다.
        print("working:%s\n" % i)

print("Start")

for i in range(5):  # long_task를 5회 수행한다.
    long_task()

print("End")

# long_task 함수는 수행하는 데 5초의 시간이 걸리는 함수이다.
# 위 프로그램은 이 함수를 총 5번 반복해서 수행하는 프로그램이다.
# 이 프로그램은 5초가 5번 반복되니 총 25초의 시간이 걸린다.

# 하지만 앞에서 설명했듯이 스레드를 사용하면 5초의 시간이 걸리는 long_task 함수를 동시에 실행할 수 있으니 시간을 줄일 수 있다.

# 다음과 같이 프로그램을 수정해 보자.

# thread_test.py
import time
import threading  # 스레드를 생성하기 위해서는 threading 모듈이 필요하다.

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)  # 스레드를 생성한다.
    threads.append(t) 

for t in threads:
    t.start()  # 스레드를 실행한다.

print("End")

# 이와 같이 프로그램을 수정하고 실행해 보면 25초 걸리던 작업이 5초 정도에 수행되는 것을 확인할 수 있다.
# threading.Thread를 사용하여 만든 스레드 객체가 동시 작업을 가능하게 해 주기 때문이다.

# 하지만 위 프로그램을 실행해 보면 "Start"와 "End"가 먼저 출력되고 그 이후에 스레드의 결과가 출력되는 것을 확인할 수 있다.
# 그리고 프로그램이 정상 종료되지 않는다. 우리가 기대하는 것은 "Start"가 출력되고 그다음에 스레드의 결과가 출력된 후 마지막으로 "End"가 출력되는 것이다.

# 이 문제를 해결하기 위해서는 다음과 같이 프로그램을 수정해야 한다.

# thread_test.py
import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()  # join으로 스레드가 종료될때까지 기다린다.

print("End")

# 스레드의 join 함수는 해당 스레드가 종료될 때까지 기다리게 한다. 따라서 위와 같이 수정하면 우리가 원하던 출력을 보게 된다.