# 파이썬 함수의 구조
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