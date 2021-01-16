##### 클래스는 왜 필요한가?

# 계산기의 "더하기" 기능을 구현한 코드

result = 0

def add(num) :
    global result
    result += num
    return result

print(add(3))
print(add(4))

# 계산기가 2대 필요한 상황

result1 = 0
result2 = 0

def add1(num) :
    global result1
    result1 += num
    return result1

def add2(num) :
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))



class Calculator :
    def __init__(self) :
        self.result = 0
        
    def add(self, num) :
        self.result += num
        return self.result


cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

# 위의 예처럼 크레스를 사용하면 계산기 대수가 늘어나더라도 객체를 생서만 하면 되기 때문에 함수를 사용하는 경우와 달리 매우 간단해진다.

# 만약 빼기 기능을 더하려면 Calculator 클래스에 다음과 같은 빼기 기능 함수를 추가해 주면 된다.

def sub(self, num) :
    self.result -= num
    return self.result





##### 클래스와 객체

# 클래스(class)란 똑같은 무엇인가를 계속해서 만들어 낼 수 있는 설계 도면이고
# 객체(object)란 클래스로 만들 피조물을 뜻한다.

class Cookie:
    pass

a = Cookie()
b = Cookie()





##### 사칙연산 클래스 만들기

### 클래스를 어떻게 만들지 먼저 구상하기

# 사칙연산을 가능하게 하는 FourCal 클래스가 다음처럼 동작한다고 가정해 보자.

# 먼저 a = FourCal()를 입력해서 a라는 객체를 만든다
a = FourCal()

# 그런다음 a.setdata(4,2)처럼 입력해서 숫자 4와 2를 a에 지정해 주고
a.setdata(4, 2)

# a.add()를 수행하면 두 수를 합한 결과(4+2)를 돌려주고
print(a.add())

# a.mul()을 수행하면 두 수를 곱한 결과(4 * 2)를 돌려주고
print(a.mul())

# a.sub()를 수행하면 두 수를 뺀 결과 (4 - 2)를 돌려주고
print(a.sub())

# a.div()를 수행하면 두 수를 나눈 결과(4 / 2)를 돌려준다.
print(a.div())

# 이렇게 동작하는 FourCal 클래스를 만드는 것이 바로 우리의 목표이다.



### 클래스 구조 만들기

class FourCal :
    pass

a = FourCal()
type(a)



### 객체에 숫자 지정할 수 있게 만들기


class FourCal :
    def setdata(self, first, second) :
        self.first = first
        self.second = second


# 클래스 안에 구현된 함수 : 메서드(method)
# 메서드의 첫 번째 매개변수(self)는 메서드를 호출한 객체가 자동으로 전달된다.

# 매서드의 또 다른 호출 방법

a = FourCal()
FourCal.setdata(a, 4, 2)


a = FourCal()
a.setdata(4, 2)
print(a.first)
print(a.second)



a = FourCal()
b = FourCal()

a.setdata(4,2)
print(a.first)

b.setdata(3,7)
print(b.second)



### 더하기 기능 만들기

class FourCal :
    def setdata(self, first, second) :
        self.first = first
        self.second = second
    def add(self) :
        result = self.first + self.second
        return result


a = FourCal()
a.setdata(4, 2)
print(a.add())




### 곱하기, 빼기, 나누기 기능 만들기

class FourCal :
    def setdata(self, first, second) :
        self.first = first
        self.second = second
    def add(self) :
        result = self.first + self.second
        return result
    def mul(self) :
        result = self.first * self.second
        return result
    def sub(self) :
        result = self.first - self.second
        return result
    def div(self) : 
        result = self.first / self.second
        return result


a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 8)
a.add()
a.mul()
a.sub()
a.div()
b.add()
b.mul()
b.sub()
b.div()




##### 생성자 (Constructor)

a = FourCal()
a.add()

# 객체에 초깃값을 설정해야 할 필요가 있을 때는 setdata와 같은 메서드를 호출 하여 초깃값을 설정하기보다는 생성자를 구현하는 것이 안전한 방법이다.
# 생성자란 객체가 생성될 때 자동으로 호출되는 메서드를 의미한다.

class FourCal:
     def __init__(self, first, second):
         self.first = first
         self.second = second
     def setdata(self, first, second):
         self.first = first
         self.second = second
     def add(self):
         result = self.first + self.second
         return result
     def mul(self):
         result = self.first * self.second
         return result
     def sub(self):
         result = self.first - self.second
         return result
     def div(self):
         result = self.first / self.second
         return result


# __init__ 메서드는 setdata 메서드와 이름만 다르고 모든 게 동일하다. 단 메서드 이름을 __init__으로 했기 때문에 
# 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출되는 차이가 있다.

a = FourCal()    # 오류발생
a = FourCal(4, 2)    # 이와 같이 first와 second에 해당되는 값을 전달하여 객체를 생성해야 한다.

a.add()
a.div()




##### 클래스의 상속

# 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것

# FourCal클래스에 제곱의 기능을 추해보자

class MoreFourCal(FourCal) :    # class 클래스이름(상속할 클래스 이름)
    pass

a = MoreFourCal(4,2)
a.add()
a.mul()
a.sub()
a.div()

class MoreFourCal(FourCal) :
    def pow(self) :
        result = self.first ** self.second
        return result


a = MoreFourCal(4, 2)
a.pow()




##### 매서드 오버라이딩

a = FourCal(4, 0)
a.div()

# 0으로 나눌때도 오류가아닌 0을 돌려주도록 만들고 싶다면?

class SafeFourCal(FourCal) :
    def div(self) :
        if self.second == 0 :
            return 0
        else :
            return self.first / self.second


# 이렇게 부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것을 메서드 오버라이딩(덮어쓰기)이라고 한다.

a = SafeFourCal(4, 0)
a.div()





##### 클래스 변수

class Family :
    lastname = "김" # lastname이 바로 클래스 변수이다.


print(Family.lastname)

a = Family()
b = Family()
print(a.lastname)
print(b.lastname)

Family.lastname = '박' # Family 클래스의 lastname을 바꾸면 클래스로 만들 객체의 lastname 값도 모두 변경된다.

print(a.lastname)
print(b.lastname)