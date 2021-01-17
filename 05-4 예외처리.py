##### 오류는 어떤 때 발생하는가?

# 먼저 디렉토리 안에 없는 파일을 열려고 시도했을 때 발생하는 오류
f = open("나 없는파일",'r')

# 0으로 다룬 숫자를 나누는 경우
4 / 0

# 리스트에 없는 값 호출
a = [1,2,3]
a[4]




##### 오류 예외 처리 기법

### try, except문

try :
    ...
except [발생 오류[as 오류 메시지 변수]] :
    ...

# try 블록 수행 중 오류가 발생하면 except 블록이 수행된다. 하지만 try 블록에서 오류가 발생하지 않으면 excepy 블록은 수행되지 않는다.

# 1. try, except만 쓰는 방법
try :
    ...
except :
    ...

# 오류의 종류에 상관없이 오류가 발생하면 except 블록 수행

# 2. 발생 오류만 포함한 except문
try :
    ...
except 발생오류 :
    ...

# 오류가 발생했을 때 except문에 미리 정해놓은 오류 이름과 일치할 때만 except 블록을 수행

# 3. 발생 오류와 오류 메세지 변수까지 포함한 except문
try :
    ...
except 발생오류 as 오류 메시지 변수 :
    ...

# 두 번째 경우에서 오류 메세지의 내용까지 알고 싶을 때 사용하는 방법
# 예시
try :
    4 / 0
except ZeroDivisionError as e :
    print(e)



### try .. finally

# finally절은 try문 수행 도중 예외 발생 여부에 상관없이 항상 수행된다.
# 보통 finally 절은 사용한 리소스를 close해야 할 때에 많이 사용한다.

f = open('foo.txt', 'w')
try :
    # 무언가를 수행한다.
finally :
    f.close()



### 여러개의 오류 처리하기

try :
    ...
except 발생 오류1 :
    ...
except 발생 오류2 :
    ...

# 예시
try :
    a = [1, 2]
    print(a[3])
    4/0
except ZeroDivisionError :
    print("0으로 나눌 수 없습니다.")
except IndexError :
    print("인덱싱 할 수 없습니다.")


try :
    a = [1, 2]
    print(a[3])
    4/0
except ZeroDivisionError as e :
    print(e)
except IndexError as e :
    print(e)


# 2개 이상의 오류를 동일하게 처리
try :
    a = [1, 2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e :
    print (e)





##### 오류 회피하기

try :
    f = open("나 없는 파일", 'r')
except FileNotFoundError :
    pass





##### 오류 일부러 발생시키기

# raise 명령어 사용

# 예를 들어 Bird 클래스를 상속받는 자식 클래스는 반드시 fly라는 함수를 구현하도록 만들고 싶은 경우(강제로 그렇게 하고 싶은 경우)
class Bird :
    def fly(self) :
        raise NotImplementedError       # NotImplementedError는 파이썬 내장 오류로, 꼭 작성해야 하는 부분이 구현되지 않았을 경우 일부러 오류를 일으키기 위해 사용한다.
    
class Eagle(Bird) :
    pass


eagle = Eagle()
eagle.fly()


# NotImplementedError가 발생되지 않게 하려면 다음과 같이 Eagle 클래스에 fly 함수를 반드시 구현해야 한다.
class Eagle(Bird) :
    def fly(self) :
        print("very fast")

eagle = Eagle()
eagle.fly()





##### 예외 만들기

# 프로그램 수행 도중 특수한 경우에만 예외 처리를 하기 위해서 종종 예외를 만들어서 사용한다. 직접 예외를 만들어 보자. 예외는 다음과 같이 파이썬 내장 클래스인 Exception 클래스를 상속하여 만들 수 있다.

class MyError(Exception) :
    pass

# 별명을 출력하는 함수를 다음과 같이 작성
def say_nick(nick) :
    if nick == '바보' :
        raise MyError()
    print(nick)


say_nick('천사')
say_nick('바보')


# 예외 처리 기법을 사용하여 MyError 발생을 예외 처리하기
try :
    say_nick('천사')
    say_nick('바보')
except MyError :
    print('허용되지 않는 별명입니다.')


# 오류 메시지를 사용하고 싶다면 다음처럼 처리
try :
    say_nick("천사")
    say_nick("바보")
except MyError as e :
    print(e)


# 오류 메시지를 출력했을 때 오류 메시지가 보이게 하려면 오류 클래스에 다음과 같은 __str__ 메서드를 구현해야 한다.
# __str__ 메서드는 print(e)처럼 오류 메시지를 print문으로 출력할 경우에 호출되는 메서드이다.

class MyError(Exception) :
    def __str__(self) :
        return "허용되지 않는 별명입니다."


try :
    say_nick("천사")
    say_nick("바보")
except MyError as e :
    print(e)

