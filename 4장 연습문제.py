### 1. 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.

# 내 답
def is_odd(a):
    if a % 2 == 0 :
        print('not odd')
    else : print('odd')

is_odd(3)
is_odd(30)


# 해설
def is_odd(number):
     if number % 2 == 1:   # 2로 나누었을 때 나머지가 1이면 홀수이다.
         return True
     else:
         return False

is_odd(3)
is_odd(4)


# 람다와 조건부 표현식을 사용하면 다음과 같이 간단하게도 만들 수 있다.
is_odd = lambda x : True if x % 2 == 1 else False
is_odd(3)

### 2. 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자.(단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)

# 내 답
def mean(*args ):
    sum = 0
    for i in args :
        sum = sum + i
    return(sum/len(args))

mean(50, 30, 40)

# 해설
def avg_numbers(*args):   # 입력 개수에 상관없이 사용하기 위해 *args를 사용
     result = 0
     for i in args:
         result += i
     return result / len(args)

avg_numbers(1, 2)
avg_numbers(1,2,3,4,5)


### 3. 다음은 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다.

input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = input1 + input2
print('두 수의 합은 %s 입니다' % total)

# 첫번째 숫자 : 3, 두번째 숫자 : 6을 입력하면 9가 아닌 36이라는 결괏값을 돌려준다. 이 프로그램의 오류를 수정해 보자.

# 내 답
input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

total = input1 + input2
print('두수의 합은 %d 입니다.' % total)

# 해설
input1 = input("첫 번째 숫자를 입력하세요:")
input2 = input("두 번째 숫자를 입력하세요:")

total = int(input1) + int(input2)      # 입력은 항상 문자열이므로 숫자로 바꾸어 주어야 한다.
print("두수의 합은 %s 입니다" % total)

### 4. 다음 중 출력 결과가 다른 것 한 개를 골라 보자.

print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))

# 내 답
# 3번


### 5. 다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.

f1 = open("test.txt", 'w')
f1.write("life is too short")

f2 = open("test.txt", 'r')
print(f2.read())

# 이 프로그램은 우리가 예상한 "Life is too short"라는 문장을 출력하지 않는다. 우리가 예상한 값을 출력할 수 있도록 프로그램을 수정해 보자.

# 내 답
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
line = f2.readline()
print(line)
f2.close()

# 해설
# 문제의 예와 같이 파일을 닫지 않은 상태에서 다시 열면 파일에 저장한 데이터를 읽을 수 없다. 따라서 열린 파일 객체를 close로 닫아준 후 
# 다시 열어서 파일의 내용을 읽어야 한다.
f1 = open("test.txt", 'w')
f1.write("Life is too short!")
f1.close() # 열린 파일 객체를 닫는다.

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()

# 또는 다음과 같이 close를 명시적으로 할 필요가 없는 with구문을 사용한다.
with open("test.txt", 'w') as f1:
    f1.write("Life is too short! ")

with open("test.txt", 'r') as f2:
    print(f2.read())




### 6. 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자.(단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 
# 새로 입력한 내용을 추가해야 한다.)

# 내 답

def inputsave(data):
    f = open("test.txt", 'a')
    f.write(data)
    f.close()

inputsave("R is better than Python")

# 해설
# 기존 내용을 유지하고 새로운 내용을 덧붙이기 위해서 다음과 같이 'a' 모드를 사용해야 한다.
user_input = input("저장할 내용을 입력하세요:")
f = open('test.txt', 'a')   # 내용을 추가하기 위해서 'a'를 사용
f.write(user_input)
f.write("\n")               # 입력된 내용을 줄 단위로 구분하기 위해 줄 바꿈 문자 삽입
f.close()



### 7. 다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.

# 내 답
f = open("test.txt", 'w')
f.write("Life is too short\n you need java")
f.close()

f1 = open("test.txt", 'r')
line = f1.read()
print(line)
f1.close()

f2 = open("test.txt", 'w')
f2.write(line.replace('java', 'python'))
f2.close()

# 해설
# 파일을 모두 읽은 후에 문자열의 replace 함수를 사용하여 java라는 문자열을 python으로 변경한 다음 저장한다.
f = open('test.txt', 'r')
body = f.read()
f.close()

body = body.replace('java', 'python')

f = open('test.txt', 'w')
f.write(body)
f.close()
