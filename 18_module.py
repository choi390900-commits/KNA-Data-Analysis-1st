# 복습
# 함수의 기본 예제
def say_hello():
  pass # 아무일도 안하는 코드

def say_hi():
  print("안녕하세요")

# 함수는 선언된(def) 후에 호출되어야 한다
say_hi()

# 매개변수를 사용하면 더 다양한 일을 할 수 있다
def show_hello(name):
  # name = Choi
  print("안녕하세요, {name}")

show_hello("Ned")
show_hello("Tuna")
show_hello("Layla")

# 매개변수는 여러 값을 받을 수 있다
def show_hi(name, message):
  print(f"{message}, {name}")

show_hi("Ned", "안녕하세요")
show_hi("Tuna", "반갑습니다")

# 매개변수에는 따로 안알려주면 기본값을 적용할 수도 있습니다
def show_greeting(name, message = "안녕하세요"):
  print(f"{message}, {name}")

show_greeting("Tuna")
show_greeting("Tuna")

# =====================================================
# 수학 관련 모듈을 불러옵니다
import math

# 해당 모듈이름.함수() 식으로 호출해야한다
result = math.sqrt(16)
print(result)

# =======================================================
# 수학 관련 모듈에서 sqrt 기능만 불러옵니다
from math import sqrt

# 이젠 sqrt만 불러도 됩니다
result = sqrt(16)
print(result)

# =====================================================
# math라는 모듈 이름 다 쓰기 귀찮아서 줄여봅시다
import math as mt

# 별칭으로 가져올 모듈 이름을 언급하기
result = mt.sqrt(16)
print(result)

# datetime 모듈을 가져오기
import datetime as dt

# datetime의 now()는 현재의 지역 날씨와 시간을 반환합니다
now = dt.datetime.now()
print(now) # 2026-08-05 11:19:59.839168
print(type(now)) # <class 'datetime.datetime'>

# =============================================================
# 표준 라이브러리 math모듈
import math

print(math.sqrt(9)) # 제곱근값 3.0
print(math.ceil(4.2)) # 올림값 5
print(2 ** 3) # 2의 2승 = 2 * 2 * 2 = 8 math와 무관

# math에서 sqrt,ceil 두개만 사용된다면 이렇게 써도 됩니다
from math import sqrt, ceil

# 위에서 가져온 math 함수들 사용 예제입니다
print(sqrt(9))
print(ceil(4.2))

print("=" * 20)

# 표준 라이브러리의 random 모듈
import random

print(random.randint(1, 10)) # 1~10 중 무작위 함수
print(random.choice(["정상", "경고", "위험"])) # 셋 중 무작위

# ===============================================================
# 표준 라이브러리의 datetime 모듈
import datetime

# datetime 모듈 안의 datetime 클래스에서 지원하는 now() 함수 호출
now = datetime.datetime.now()
print(now) # 2026-08-05 13:19:37.414356

# =================================================================
# 모듈 도움말 보기 : 참고만 하고 구글링한 웹사이트에서 보기
# dir(math)
# help(math.sqrt)

# ==================================================================
# 절대경로와 상대경로
# 절대경로의 예 : C:\Users\user\Desktop\KNA-Data-Analysis-1st

# 만약 C:\Users\user\Desktop\KNA-Data-Analysis-1st 폴더에 터미널을 연 상태에서
# code.py 코드를 실행하고 싶다면
# python code.py

# 위 code.py 언급부분은 사실 상대경로를 의미한다
# 그래서 절대경로로 지정해줘도 똑같이 실행될 것이다
# pythom C:\Users\user\Desktop\KNA-Data-Analysis-1st

# 현재 경로에 있는 해당 파일이란걸 더 강조하는 상대경로 지정으로 써도 된다
# python ./code.py

# 만약 C:\Users\user\Desktop\KNA-Data-Analysis-1st 아닌
# C:\Users\user\Desktop\KNA-Data-Analysis-1st 폴더 경로에서 위 코드를 실행하고 싶다면
# 절대경로 : python C:\Users\user\Desktop\KNA-Data-Analysis-1st
# 상대경로 : python ..\sampe\code.

# =================================================================

# 표준 라이브러리의 os 모듈 활용
import os
current_working_directory = os.getcwd()
print(current_working_directory)

# 현재 작업디렉토리의 파일 목록 가져오기
file_list = os.listdir()
for file_name in file_list:
  print(file_name)

# =========================================================
# 파일이 존재하는지 알아봅시다
# 운용체제(윈도/맥/리눅스)마다 경로를 나타내는 방법이 달라서
# 상황에 맞게 경로문자열을 만들어주는 os의 함수를 사용
path = os.path.join("data", "08_press.csv")
print(path)

# 실제로 경로문자열을 따라서 찾아가면
# 해당 파일이 있는지 알아봅시다: True/False
if os.path.exists(path):
  print(f"파일 있음: {path}")

# =========================================================
