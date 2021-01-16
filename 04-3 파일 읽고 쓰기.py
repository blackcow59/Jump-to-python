##### 파일 생성하기

f = open("새파일.txt", 'w')     # r : 읽기모드, w : 쓰기모드, a : 추가모드
f.close()

# 파일을 쓰기 모드로 열면 해당 파일이 이미 존재할 경우 원래 있던 내용이 모두 사라지고, 해당 파일이 존재하지 않으면 새로운 파일이 생성된다. 

f = open("c:/Python/doit/새파일.py", 'w')
f.close()   #열려있는 파일 객체를 닫아주는 역할(생략해도 된다.)




##### 파일을 쓰기 모드로 열어 출력값 적기

f = open("C:/Python/doit/새파일.txt", 'w')
for i in range(1, 11) :
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

for i in range(1,11) :
    data = "%d번째 줄입니다.\n" % i
    print(data)
    



##### 프로그램의 외부에 저장된 파일을 읽는 여러가지 방법

##### readline() 함수 이용하기

f = open("c:/Python/doit/새파일.txt", 'r')
line = f.readline()
print(line)
f.close()

f = open("c:/Python/doit/새파일.txt", 'r')
while True :
    line = f.readline()
    if not line : break
    print(line)
f.close()

# readline()은 더이상 읽을 줄이 없을 경우 빈 문자열을 리턴한다.

while 1:
    data = input()
    if not data : break
    print(data)




##### readlines 함수 사용하기

f = open("c:/Python/doit/새파일.txt", 'r')
lines = f.readlines()
for line in lines :
    print(line)
f.close()

# readlines 함수는 파일의 모든 줄을 읽어서 각가의 줄을 요소로 갖는 리스트로 돌려준다
lines



##### read 함수 사용하기

f = open("c:/Python/doit/새파일.txt", 'r')
data = f.read()
print(data)
f.close()

# f.read()는 파일 내용 전체를 문자열로 돌려준다.



##### 파일에 새로운 내용 추가하기

f = open("c:/Python/doit/새파일.txt",'a')
for i in range(11,20) :
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()




##### with문과 함께 사용하기

f = open("foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()

# 파일을 열고 닫는것을 자동으로 처리하는 방법 : with문

with open("foo.txt", 'w') as f:
    f.write("Life is too short, you need python")

# with블록을 벗어나는 순간 열린 파일 객체 f가 자동으로 close 되어 편리함



