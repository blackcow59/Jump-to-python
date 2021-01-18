##### abs
### abs(x)는 어떤 숫자를 입력받았을 때, 그 숫자의 절대값을 돌려주는 함수이다.

abs(3)
abs(-3)
abs(-1.2)



##### all
### all(x)는 반복가능한(iterable) 자료형 x를 입력 인수로 받으며 이 x의 요소가 모두 참이면 True, 하나라도 거짓이면 False를 돌려준다.

all([1,2,3])
all([1,2,3,0])
all([])



##### any
### any(x)는 반복가능한(iterable) 자료형 x를 입력인수로 받으며 이 x의 요소 중 하나라도 참이 있으면 True, x가 모두 거짓이면 False를 돌려준다. all의 반대

any([1,2,3,0])
any([0, ""])
any([])



##### chr
### chr(i)는 아스키(ASCII)코드 값을 입력 받아 그 코드에 해당하는 문자를 출력하는 함수이다.

chr(97)
chr(48)



##### dir
### dir은 객체가 자체적으로 가지고 있는 변수나 함수를 보여 준다. 다음 예는 리스트와 딕셔너리 객체 관련 함수(메서드)를 보여주는 예이다. 
### 우리가 02장에서 살펴본 자료형 관련 함수를 만나 볼 수 있다.

dir([1,2,3])
dir({'1' : 'a'})



##### divmod
### divmod(a, b)는 2개의 숫자를 입력으로 받는다. 그리고 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수이다.

divmod(7, 3)
# 몫을 구하는 연산자 // 와 나머지를 구하는 연산자 % 를 각각 사용한 결과와 비교해 보자.
7//3
7 % 3



##### enumerate
### enumerate는 '열거하다'라는 뜻이다. 
### 이 함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 돌려준다.

# 보통 for문과 함께 자주 사용한다
for i, name in enumerate(['body', 'foo', 'bar']) :
    print(i, name)



##### eval
### eval(expression)은 실행 가능한 문자열(1+2,'hi' + 'a' 같은것)을 입력으로 받아 문자열을 실행한 결과를 돌려주는 함수이다.

eval('1+2')
eval("'hi' + 'a'")
eval('divmod(4, 3)')



##### filter
### filter란 무엇인가를 걸러낸다는 뜻으로 filter 함수도 동일한 의미를 가진다.
### filter 함수는 첫 번째 인수로 함수 이름을, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받는다. 
### 그리고 두 번째 인수인 반복 가능한 자료형 요소가 첫 번째 인수인 함수에 입력되었을 때 반환 값이 참인 것만 묶어서(걸러 내서) 돌려준다.

# positive.py
def positive(l) :
    result = []
    for i in l :
        if i > 0 :
            result.append(i)
    return result

print(positive([1, -3, 2, 0, -5, 6]))

# filter1.py
def positive(x) :
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

# lambda사용시 더욱 간편하게 코드 작성 가능
list(filter(lambda x : x > 0, [1, -3, 2, 0, -5, 6]))



##### hex
### hex(x)는 정수 값을 입력받아 16진수로 변환하여 돌려주는 함수이다.

hex(234)
hex(3)



##### id
### id(object)는 객체를 입력받아 객체의 고유 주소 값(레퍼런스)을 돌려주는 함수이다.

a = 3
id(3)
id(a)
b = a
id(b)
id(4)



##### input
### input([prompt])은 사용자 입력을 받는 함수이다. 매개변수로 문자열을 주면 다음 세번째 예에서 볼 수 있듯이 그 문자열은 프롬프트가 된다.

a = input()
hi
a

b = input("Enter: ")
hi
b



##### int
### int(x)는 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 돌려주는 함수로, 정수를 입력으로 받으면 그대로 돌려준다.

int('3')
int(3.4)

### int(x, radix)는 radix 진수로 표현된 문자열 x를 10진수로 변환하여 돌려준다.

int('11', 2)
int('1A', 16)



##### isinstance
### isinstance(object, class)는 첫 번쨰 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다.
### 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 돌려준다.

class Person : pass

a = Person()
isinstance(a, Person)

b = 3
isinstance(b, Person)



##### len
### len(s)은 입력값 s의 길이(요소의 전체 개수)를 돌려주는 함수이다.

len('python')
len([1,2,3])
len([1, 'a'])



##### list
### list(s)는 반복 가능한 자료형 s를 입력받아 리스트로 만들어 돌려주는 함수이다.

list("python")
list((1,2,3))

a = [1,2,3]
b = list(a)
b



##### map
### map(f, iterable)은 함수(f)와 반복가능한(iterable) 자료형을 입력으로 받는다. map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다.

# two_times.py
def two_times(numberList) :
    result = [ ]
    for number in numberList :
        result.append(number*2)
    return result

result = two_times([1,2,3,4])
print(result)


def two_times(x) :
    return x * 2

list(map(two_times, [1,2,3,4]))

# lambda를 사용해서 더 간결하게
list(map(lambda a : : a * 2, [1,2,3,4]))



##### max
### max(iterable)는 인수로 반복 가능한 자료형을 입력받아 그 최댓값을 돌려주는 함수이다.

max([1,2,3])
max("python")



##### min
### min(iterable)은 max 함수와 반대로, 인수로 반복 가능한 자료형을 입력받아 그 최솟값을 돌려주는 함수이다.

min([1,2,3])
min("python")



##### oct
### oct(x)는 정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려주는 함수이다.

oct(34)
oct(12345)



##### open
### open(filename, [mode])은 "파일 이름"과 "읽기 방법"을 입력받아 파일 객체를 돌려주는 함수이다. 
### 읽기 방법(mode)을 생략하면 기본값인 읽기 전용 모드(r)로 파일 객체를 만들어 돌려준다.

# w : 쓰기모드, r : 읽기모드, a : 추가모드, b : 바이너리모드
# b는 w,r,a와 함께 사용한다
f = open("binary_file", "rb")

# fread와 fread2는 동일한 방법이다.(읽기모드)
fread = open("read_mode.txt", 'r')
fread2 = open("read_mode.txt")

# 추가모드로 파일을 여는 예
fappend = open("append_mode.txt", 'a')



##### ord
### ord(c)는 문자의 아스키 코드 값을 돌려주는 함수이다.

# ord와 chr 함수는 반대이다
ord('a')
ord('0')



##### pow
### pow(x, y)는 x의 y제곱한 결괏값을 돌려주는 함수이다.

pow(2, 4)
pow(3, 3)



##### range
### range([start,] stop [,step] )는 for문과 함께 자주 사용하는 함수이다. 
### 이 함수는 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 돌려준다.

# 인수가 하나일 경우
# 시작 숫자를 지정해 주지 않으면 range 함수는 0부터 시작한다.
list(range(5))

# 인수가 2개일 경우
# 시작과 끝 숫자를 나타낸다. 단 끝 숫자는 해당 범위에 포함되지 않는다.
list(range(5, 10))

# 인수가 3개일 경우
# 세번째 인수는 숫자 사이의 거리를 말한다
list(range(1, 10, 2))
list(range(0, -10, -1))



##### round
### round(number[, ndigits]) 함수는 숫자를 입력받아 반올림해 주는 함수이다.
### [, ndigits]는 ndigits(반올림하여 표시하고 싶은 소수점의 자리수)가 있을 수도 있고 없을 수도 있다는 의미이다.

round(4.6)
round(4.2)

# 소수점 2자리까지만 반올림하여 표시
round(5.678, 2)



##### sorted
### sorted(iterable) 함수는 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수이다.

sorted([3,1,2])
sorted(['a', 'c', 'b'])
sorted("zero")
sorted((3,2,1))



##### str
### str(object)은 문자열 형태로 객체를 변환하여 돌려주는 함수이다.

str(3)
str('hi')
str('hi'.upper())



##### sum
### sum(iterable)은 입력받은 리스트나 튜플의 모든 요소의 합을 돌려주는 함수이다.

sum([1,2,3])
sum((4,5,6))



##### tuple
### tuple(iterable)은 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 돌려주는 함수이다. 만약 튜플이 입력으로 들어오면 그대로 돌려준다.

tuple("abc")
tuple([1,2,3])
tuple((1,2,3))



##### type
### type(object)은 입력값의 자료형이 무엇인지 알려 주는 함수이다.

type('abc')
type([ ])
type(open("test", 'w'))



##### zip
### zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.
### 여기서 사용한 *iterable은 반복 가능(iterable)한 자료형 여러 개를 입력할 수 있다는 의미이다.

list(zip([1,2,3], [4,5,6]))
list(zip([1,2,3], [4,5,6], [7,8,9]))
list(zip("abc", "def"))