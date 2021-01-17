##### 모듈 만들기
def add(a, b) :
    return a + b

def sub(a, b) : 
    return a - b

# 위와 같은 내용을 mod1.py로 만들고 디렉토리에 저장하면 mod1.py파일이 바로 모듈이다.




##### 모듈 불러오기

# import 모듈이름
# from 모듈이름 import 모듈함수

# 먼저 명령 프롬프트 창을 열고 mod1.py를 저장한 디렉터리로 이동한 다음 대화형 인터프리터를 실행한다.

import mod1
print(mod1.add(3, 4))
print(mod1.sub(4, 2))

from mod1 import add
add(3, 4)

from mod1 import add, sub
sub(4, 2)

from mod1 import *      # *문자는 모든 것 이라는 뜻의 정규표현식





##### if __name__ == "__main__":의 의미

f = open("mod1.py", 'a')
f.write("\nprint(add(1, 4)) \nprint(sub(4, 2))")
f.close()

import mod1
# 명령 프롬프트 창에서 import mod1을 실행하면 위에서 적은 결과값인 5와 2가 출력된다.
# 이러한 문제를 방지하기 위해서는 mod1.py 파일을 다음처럼 변경해야한다.

# mod1.py
def add(a, b): 
    return a+b

def sub(a, b): 
    return a-b

if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))


import mod1


# __name__ 변수란?
# 파이썬의 __name__변수는 파이썬이 내부적으로 사용하는 특별한 변수 이름이다.
# 만약 C:/Python/doit> python mod1.py 처럼 직접 mod1.py파일을 실행할 경우 mod1.py의 __name__변수에는 __main__ 값이 저장된다.
# 하지만 파이썬 셸이나 다른 파이썬 모듈에서 mod1을 import할 경우에는 mod1.py의 __name__변수에는 mod1.py의 모듈 이름 값 mod1이 저장된다.




##### 클래스나 변수 등을 포함한 모듈

# mod2.py
PI = 3.141592

class Math :
    def solv(self, r) :
        return PI * (r ** 2)

def add(a, b) :
    return a + b

import mod2
print(mod2.PI)

a = mod2.Math()
print(a.solv(2))




##### 다른 파일에서 모듈 불러오기
# 다른 파이썬 파일에서 이전에 만들어 놓은 모듈을 불러와서 사용하는 방법


# modtest.py
import mod2
result = mod2.add(3, 4)
print(result)

import modtest


### 모듈을 불러오는 또 다른 방법
# 모듈을 저장한 디렉토리로 이동하지 않고 모듈을 불러와서 사용하는 방법

# 명령프롬프트창에 입력
# cd c:\Python\doit
# mkdir mymod
# move mod2.py mymod


## 1. sys.path.appendO(모듈을 저장한 디렉토리)사용하기

import sys

sys.path
# sys.path는 파이썬 라이브러리가 설치되어 있는 디렉토리를 보여 준다. 만약 파이썬 모듈이 디렉터리에 들어 있다면 모듈이 저장된 디렉토리를 이동할 필요 없이 바로 불러서 사용할 수 있다.
# 그렇다면 sys.path에 c:\Python\doit\mymod 디렉토리를 추가하면 아무 곳에서나 불러 사용할 수 있지 않을까?

sys.path.append("C:/Python/doit/mymod")
sys.path

import mod2
print(mod2.add(3, 4))

## 2. PYTHONPATH 환경 변수 사용하기

# 명령프롬프트창에 입력
# set PYTHONPATH = c:\Python\doit\mymod
# python

import mod2
print(mod2.add(3, 4))