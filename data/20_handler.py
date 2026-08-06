# 트레이스백 에러 읽기

# valueError: 글자를 숫자로 변환 요구 - 당연히 실패
temp = int("스물")

# Traceback (most recent call last):
#   File "c:\Users\user\Desktop\KNA-Data-Analysis-1st\data\20_handler.py", line 4, in <module>
#     temp = int("스물")
#            ~~~^^^^^^^^
# ValueError: invalid literal for int() with base 10: '스물'

# 정상화
temp =int("20")
print(temp)

print("=" * 20)

# zeroDivisionError: division by zero

# 정상화
result = 10 / 3
print(result)

# 정상화
print("Hello")

# ====================================================================
temp1 = -1

try:
  temp1 = int("스물")
except:
  print("해봤는데 안되네요")
  temp = 0 # 문재가 있어도 앞으로 잘 진행되도록 대안/추가 처리 필요

print(temp1)

# ======================================================================
# 실습2번
origin = input("온도: ")

print(f"입력한 온도는 {origin}")

temp = 0

try:
    temp = int(origin)
except:
   print("숫자 아니면 왜 저를 부르셨어요? 0으로 생각할게요")

next_temp = temp + 10
print(f"10도만 더 높으면 {next_temp}")

# ======================================================================
