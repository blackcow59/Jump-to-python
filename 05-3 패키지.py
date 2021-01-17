##### 패키지란 무엇인가?
# 패키지(Packages)는 도트(.)를 사용하여 파이썬 모듈을 계층적(디렉토리 구조)으로 관리할 수 있게 해준다.
# 예를 들어 모듈 이름이 A.B인 경우에 A는 패키지 이름이 되고 B는 A패키지의 B모듈이 된다.

# 가상의 game 패키지 예

game/
    __init__.py
    sound/
        __init__.py
        echo.py
        wav.py
    graphic/
        __init__.py
        screen.py
        render.py
    play/
        __init__.py
        run.py
        test.py


# game, sound, ggraphic, play는 디렉토리 이름이고 확장자가 .py인 파일은 파이썬 모듈이다.
# game 디렉토리가 이 패키지의 루트 디렉토리이고 sound, graphic, play는 서브 디렉토리이다.




##### 패키지 만들기

### 패키지 기본 구성 요소 준비하기

# 1.C:/Python/doit 디렉토리 밑에 game 및 기타 서브 디렉토리를 생성하고 .py파일들을 다음과 같이 만들어 보자

C:/doit/game/__init__.py
C:/doit/game/sound/__init__.py
C:/doit/game/sound/echo.py
C:/doit/game/graphic/__init__.py
C:/doit/game/graphic/render.py

# 2. 각 디렉토리에 __init__.py 파일을 만들어 놓기만 하고 내용은 일단 비워 둔다.

# 3. ehco.py 파일은 다음과 같이 만든다
def echo_test() :
    print("echo")


# 4. render.py 파일은 다음과 같이 만든다.
def render_test() :
    print("render")


# 5. 다음 예제를 수행하기 전에 우리가 만든 game 패키지를 참조할 수 있도록 명령 프롬프트 창에서 set명령어로 PYTHONPATH 환경 변수에 
# c:/Python/doit 디렉토리를 추가한다. 그리고 파이썬 인터프리터를 실행한다.

# set PYTHONPATH = c:/Python/doit
# python





##### 패키지 안의 함수 실행하기
# 반드시 명령프롬프트에서 파이썬 인터프리터를 실행하여 진행하기
# 하나의 예제를 실행하고 나서 다음 예제를 실행할 때에는 반드시 인터프리터를 종료하고 다시 실행해야 한다.

# 첫 번째는 echo 모듈을 import하여 실행하는 방법
import game.sound.echo
game.sound.echo.echo_test()


# 두 번째는 echo 모듈이 있는 디렉토리까지를 from ... import 하여 실행하는 방법
from game.sound import echo
echo.echo_test()


# 세 번째는 echo 모듈의 echo_test 함수를 직접 import 하여 실행하는 방법.
from game.sound.echo import echo_test
echo_test

# 하지만 다음과 같이 echo_test 함수를 사용하는것은 불가능하다.

import game
game.sound.echo.echo_test()
# import game을 수행하면 game 디렉토리의 모듈 또는 game 디렉토리의 __init__.py에 정의한 것만 참조할 수 있다.

import game.sound.echo.echo_test
# 도트 연산자(.)를 사용해서 import a.b.c처럼 import할 때 가장 마지막 항목인 c는 반드시 모듈 또는 패키지여야만 한다.





###### __init__.py 의 용도

# __init__.py 파일은 해당 디렉토리가 패키지의 일부임을 알려주는 역할을 한다. 
# 만약 game, sound, graphic 등 패키지에 포함된 디렉토리에 __init__.py 파일이 없다면 패키지로 인식되지 않는다.
# (python3.3 버전부터는 없어도 인식가능)


from game.sound import *
echo.echo_test()

# 특정 디렉토리의 모듈을 *를 사용하여 import할 때에는 다음과 같이 해당 디렉토리의 __init__.py 파일에 __all__변수를 설정하고 
# import할 수 있는 모듈을 정의해 주어야 한다.
# C:/doit/game/sound/__init__.py
__all__ = ['echo']

from game.sound import *
echo.echo_test()




##### relative 패키지

# 만약 graphic 디렉토리의 render.py 모듈이 sound 디렉터리의 echo.py 모듈을 사용하고 싶다면 어떻게 해야 할까? 다음과 같이 render.py를 수정하면 가능하다.
# render.py
from game.sound.echo import echo_test
def render_test() :
    print ("render")
    echo_test()

from game.graphic.render import render_test
render_test()

# 다음과 같이 relative 하게 import하는 것도 가능하다.
# render.py
from ..sound.echo import echo_test

def render_test():
    print ("render")
    echo_test()


# 여기에서 ..은 부모 디렉터리를 의미한다
# relative한 접근자에는 다음과 같은 것이 있다.
# .. -부모 디렉토리
# . -현재 디렉토리

