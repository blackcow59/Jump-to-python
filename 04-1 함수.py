##### 파이썬 함수의 구조
# def 함수명(매개변수) :
#     <수행할 문장1>
#     <수행할 문장2>
#     ...


def add (a, b) :
    return a + b

a = 3
b = 4
c = add(a,b)
print(c)

def add (a,b) :     # a, b는 매개변수
    return a + b

print(add(3,4))     # 3, 4는 인수






# 일반적인 함수
# def 함수이름(매개변수) : 
#   <수행할 문장>
#   ...
#   return 결과값


def add(a, b):
    result = a + b
    return result

a = add(3, 4)
print(a)



##### 입력값이 없는 함수


def say() :
    return 'Hi'
    

a = say()
print(a)


##### 결과값이 없는 함수
# 결과값은 오직 return 명령어로만 돌려받을 수 있다.

def add(a, b) :
    print("%d, %d의 합은 %d입니다." % (a, b, a + b))
    

add(3, 4)

a = add(3,4)
print(a)



##### 입력값도 결괏값도 없는 함수

def say() :
    print('Hi')
    
say()


##### 매개변수 지정하여 호출하기

def add(a, b) :
    return a + b

result = add(a = 3, b = 7) # a에 3 b에 7을 전달
print(result)

result = add(b = 5, a = 3) # b에 5, a에 3을 전달
print(result)


##### 입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?

# def 함수이름(*매개변수) :
#   <수행할 문장>
#   ...


def add_many(*args) :
    result = 0
    for i in args :
        result = result + i
    return result

result = add_many(1,2,3)
print(result)

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)



def add_mul(choice, *args) :
    if choice == "add" :
        result = 0
        for i in args :
            result = result + i
    elif choice == "mul" :
        result = 1
        for i in args :
            result = result * i
    return result

result = add_mul('add', 1,2,3,4,5)
print(result)

result = add_mul('mul', 1,2,3,4,5)
print(result)


##### 키워드 파라미터 kwargs

def print_kwargs(**kwargs) :
    print(kwargs)

    
print_kwargs(a = 1)

print_kwargs(names = 'foo', age = 3)


##### 함수의 결괏값은 언제나 하나이다

def add_and_mul(a,b) :
    return a + b, a * b

result = add_and_mul(3,4)
print(result)

result1, result2 = add_and_mul(3,4)


def add_and_mul(a, b) :
    return a + b
    return a * b    # 두번째 return 은 실행되지 않음

result = add_and_mul(2,3)
print(result)

# 함수는 retrun문을 만나는 순간 결괏값을 돌려준 다음 함수를 빠져나가게 된다.



# return의 또 다른 쓰임새
# 특별 상황에서 함수를 빠져나가고 싶을때

def say_nick(nick) :
    if nick == "바보" :
        return
    print("나의 별명은 %s 입니다." % nick)
    
    
say_nick('야호')
say_nick('바보')



##### 매개변수에 초기값(default) 미리 설정하기

def say_myself(name, old, man = True):
    print("나의 이름은 %s 입니다." % name)
    print('나이는 %d살 입니다.' % old)
    if man :
        print('남자입니다.')
    else :
        print('여자입니다.')

say_myself('최호진', 25)

say_myself('최호진', 25, True)

say_myself('최희진', 27, False)


def say_myself(name, man = True, old) : # 초기값을 설정해 놓은 매개변수 뒤에 초기값을 설정해 놓지 않은 매개변수는 사용할 수 없다.
    print('나의 이름은 %s 입니다.' % name)
    print('나이는 %d살 입니다.' % old)
    if man :
        print('남자입니다.')
    else :
        print('여자입니다.')

# 초기값을 설정할 매개변수는 항상 뒤쪽에 놓는것을 잊지말자



##### 함수 안에서 선언한 변수의 효력 범위

a = 1
def vartest(a) :
    a = a + 1
    
vartest(a)
print(a)

# 함수 안에서 새로 만든 매개변수는 함수 안에서만 사용하는 "함수만의 변수"이다.

def vartest(a) :
    a = a + 1

vartest(3)
print(a)
# a라는 변수는 함수 안에서만 선언되었기에 print(a)에서 a라는 변수를 찾을 수 없다.



##### 함수 안에서 함수 밖의 변수를 변경하는 방법

# 1. return 사용하기

a = 1
def vartest(a) :
    a = a + 1
    return a

a = vartest(a)
print(a)


# 2. global 명령어 사용하기

a = 1
def vartest() :
    global a
    a = a + 1
    
vartest()
print(a)

# global a 문장은 함수 안에서 함수 밖의 a 변수를 직접 사용하겠다는 뜻
# global 명령어는 지양하는것이 좋다.





##### lambda
# def대신 함수를 한줄로 간결하게 만들때 사용

add = lambda a, b : a + b
result = add(3, 4)
print(result)

# 위와 동일한 def함수

def add(a, b):
    return a + b

result = add(3, 4)
print(result)

# lambda예약어로 만든 함수는 retrun명령어가 없어도 결괏값을 돌려준다.