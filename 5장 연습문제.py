##### 1. 다음은 Calculator 클래스이다.

class Calculator :
    def __init__(self) :
        self.value = 0

    def add(self, val) : 
        self.value += val


cal = Calculator()
cal.add(10)
cal.add(11)
print(cal.value)

# 위 클래스를 상속하는 UpgradeCalculator를 만들고 값을 뺄 수 있는 minus 메서드를 추가해보자.


# 답
class UpgradeCalculator(Calculator) :
    def minus(self, val) :
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)

# 해설
class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val




##### 2. 객체변수 value가 100이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator 클래스를 만들어 보자.
# 단 1번의 Calculator클래스를 상속해서 만들어야 한다.

# 답
class MaxLimitCalculator(Calculator) :
    cal = MaxLimitCalculator()
    if cal.value >= 100:
        print(100)


cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)

### ???? 도대체 어캐하는걸까
# 해설
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100



##### 3. 다음 결과를 예측해 보자.

all([1, 2, abs(-3)-3]) # False
chr(ord('a')) == 'a' # True





##### 4. filter와 lambda를 사용하여 리스트[1,-2,3,-5,8,-3]에서 음수를 모두 제거해 보자.

# 답
list(filter(lambda x: x > 0, [1,-2,3,-5,8,-3]))


# 해설
list(filter(lambda x:x>0, [1, -2, 3, -5, 8, -3]))





##### 5. 234라는 10진수의 16진수는 다음과 같이 구할 수 있다.
hex(234)
# 반대로 16진수 문자열0xea를 10진수로 변경해 보자

# 답
int(0xea)


# 해설
int('0xea', 16)






##### 6. map과 lambda를 사용하여 [1,2,3,4] 리스트의 각 요솟값에 3이 곱해진 리스트 [3,6,9,12]를 만들어 보자

# 답
list(map(lambda x: x * 3, [1,2,3,4]))


# 해설
list(map(lambda x:x*3, [1,2,3,4]))




##### 7. 다음 리스트의 최댓값과 최솟값의 합을 구해보자
# [-8, 2, 7, 5, -3, 5, 0, 1]

# 답
sum([max([-8, 2, 7, 5, -3, 5, 0, 1]), min([-8, 2, 7, 5, -3, 5, 0, 1])])


# 해설
a = [-8, 2, 7, 5, -3, 5, 0, 1]
max(a) + min(a)







##### 8. 17 / 3의 결과는 다음과 같다.
17/3

# 위 결과값을 소숫점 4자리까지만 반올림하여 표시해 보자

# 답
round(17/3, 4)


# 해설
round(17/3, 4)






##### 9. 다음과 같이 실행할 때 입력값을 모두 더하여 출력하는 스크립트(C:/Pyhton/doit/myargv.py)를 작성해 보자.

# C:\> cd doit
# C:\doit> python myargv.py 1 2 3 4 5 6 7 8 9 10
# 55

# 답
# myargv.py
def add_all(*args):
    sum = 0
    for i in args :
        sum += i
    return sum

import myargv
myargv.add_all(1,2,3,4,5,6,7,8,9,10)

# 해설
import sys

numbers = sys.argv[1:] # 파일 이름을 제외한 명령 행의 모든 입력

result = 0
for number in numbers:
    result += int(number)
print(result)

### ??????






##### 10. os 모듈을 사용하여 다음과 같이 동작하도록 코드를 작성해 보자.
# 1. C:/Python/doit 디렉터리로 이동
# 2. dir 명령을 실행하고 그 결과를 변수에 담는다.
# 3. dir 명령의 결과를 출력한다.

# 답
import os
os.chdir("C:\Python\doit")
os.getcwd()
os.system("dir")

f = os.popen("dir")
print(f.read())


# 해설
import os
os.chdir("C:/Python/doit")
result = os.popen("dir")
print(result.read())







##### 11. glob 모듈을 사용하여 C:\Python\doit 디렉터리의 파일 중 확장자가 .py인 파일만 출력하는 프로그램을 작성해 보자.

# 답
import glob
glob.glob("c:\Python\doit\*.py")

# 해설
import glob
glob.glob("c:/Python/doit/*.py")





##### 12. time 모듈을 사용하여 현재 날짜와 시간을 다음과 같은 형식으로 출력해 보자.

# 답
import time
time.strftime('%x %X', time.localtime(time.time()))
time.strftime('%c', time.localtime(time.time()))
time.strftime('%Y/%m/%d %X', time.localtime(time.time()))


# 해설
import time
time.strftime("%Y/%m/%d %H:%M:%S")





##### 13. random모듈을 사용하여 로또 번호(1~45 사이의 숫자 6개)를 생성해 보자(단 중복된 숫자가 있으면 안 됨)

# 답
import random
random.randint(1, 45)

def random_pop(data) :
    number = random.choice(data)
    data.remove(number)
    return number


random_pop(list(range(1, 46)))


# 해설
import random

result = []
while len(result) < 6:
    num = random.randint(1, 45)   # 1부터 45까지의 난수 발생
    if num not in result:
        result.append(num)

print(result)