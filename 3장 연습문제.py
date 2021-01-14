### 1.

a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
### ??? 왜 need는 출력이 안될까? -> 가장먼저 참이되는 조건이 출력된다.



### 2.

i = 0
b = 0
while i <= 1000 :
    i = i + 1
    if i % 3 == 0:
        b = i + b
print(b)
        
### ??? b를 최종적으로 한번만 출력하는 방법이 없을까?


### 3.

a = []
i = 1
while len(a) <= 5 :
    a = ["*"]
    print(a * i)
    i = i + 1
    a = ["*"] * i

### ??? 시발 왜캐어렵노

i = 0
while True:
    i += 1 # while문 수행 시 1씩 증가
    if i > 5: break     # i 값이 5보다 크면 while문을 벗어난다.
    print ('*' * i)     # i 값 개수만큼 *를 출력한다.

i = 0
while i <= 5 :
    i = i + 1
    print('*' * i)
    


### 4.

a = range(101)
for i in a :
    print(i)
    
### ??? 맞나?


### 5.

A = [70,60,55,75,95,90,80,80,85,100]
B = 0
for i in A :
    B = i + B
print(B/len(A))

    
### ??? 맞게한건가
# += : 할당연산자(ex : a += b -> a + b = a)
# 왼쪽 변수에 오른쪽 값을 더하고 그 결과를 왼쪽 변수에 할당.





### 6.
numbers = [1,2,3,4,5]
result = []
for n in numbers : 
    if n % 2 == 1 : 
        result.append(n*2)
print(result)

a = [1,2,3,4,5]
result = [n * 2 for n in a if n % 2 == 1]
print(result)
