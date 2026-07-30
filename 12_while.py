# while 반복과 흐름 제어

# while문은 조건이 거짓이 되는 플래그를 꼭 세워야 함
# 무한루프의 강제 종료: ctrl + c

# count = 1
# while count <= 3:
#   print(count)
#   count = count + 1
# 출력: 1, 2, 3

# while문 사용 체크리스트
# 1. 반복 적 변수(시작값) 존재 여부
# 2. 반복을 하다가 언젠가 False가 될 수 있는 종료 조건 포함 여부
# 3. 변수가 거짓 방향으로 값이 변경되는지

# count = 1 # 1번

# while count >= 1: # 2번
#   # count = 0 # 반복문
#   print(count)
#   count += 1

# ===================================================================

ans = 7
guess = 0
while guess != ans:
  guess = int(input("맞혀보세요: "))
print("정답입니다")

# ===================================================================

answer = 8
user_a = 0

while answer != user_a:
    user_a = int(input("1~10 사이의 정답을 맞혀 보세요: "))
print("정답입니다!")

# ====================================================================
print("I" == "i") # python은 대소문자를 항상 다르다고 봄

# break
# 반복을 그만 돌고 싶을 때
# 예시1) [1, 1, 3, 3, 2, 1, 1, 1]
# 위 리스트를 돌면서 10이상이 누적값이 총 15를 넘으면 종료
# break 사용 시 즉시 for문을 나감

input_sum = 0

while True:
   user_input = input("값을 입력하세요. 값의 누적이 15를 넘으면 종료합니다.")
   input_sum += user_input

   if input_sum > 15:
      print("누적 합계:", input_sum, "입력을 종료합니다.")
      break
print("break를 통해 while문을 나가면 이후 코드가 실횅됨")

# 사용자 입력값을 확인만 하고 저장할 필요가 없는 경우
# while True:
#    # 변수 x는 반복을 돌 때마다 재할당되기 때문에 휘밯되지만
#    x = input("입력 ()")
#    if x =="q"


# ================================================================

n = int(input("횟수: "))

for i in range(n):
   v = int(input("측정값: "))

   if v > 80:
      print("이상 발생")
      print("가동 횟수:", n)
      break
   else:
      print("정상 상태")

# ===============================================================

# 실습) up down게임
# 1~50 중 하나의 숫자를 정답으로 저장
# 사용자의 입력값 기준으로 정답이 up인지 down인지 출력
# 정답이 나오면 정답이고, 게임이 종료되었다고 


   import random

ud = random.randint(1, 50) 
print("1~50 사이의 숫자를 맞춰보세요!")

while True:
    guess = int(input("숫자를 입력하세요: "))
    
    if guess < ud:
        print("Up! ⬆️")
    elif guess > ud:
        print("Down! ⬇️")
    else:
        print("정답입니다! 게임이 종료되었습니다.")
        break

# ============================================================
first = int(input("1번째 입력값: "))

# 첫 번째 입력값은 자동으로 최댓값이 됨 (비교할 다른 값이 없기 떄문)
max_value = first

# for문을 사용해서 사용자 입력
# 입력 받은 값 중에서 가장 큰 값을 출력
for i in range(4):
   v = int(input(f"{1 +1}번째 입력: "))

   # max _value에는 현 시점 최댓값
   # v에는 방금 사용자가 입력한 값
   # max_value와 v의 값을 비교해 더 큰 값을 max_value에 재할당
   if v > max_value:
      max_value = v
   print("최댓값:", max_value)

# =================================================================

# 흐름 표를 보고 코드 작성

total = 0

for i in [4, 7, 6]:
   if i > 5:
      total += i
print("합계:", total)

# ===================================================================

a = int(input("횟수: "))
fd = False
for i in range(a):
   b = int(input("측정값: "))
   if b > 80:
      fd = True
      break
if fd:
   print("발견")
else:
   print("없음")

# ==============================================================

temps = [25, 26 , 28, 29, 30, 31, 27, 35]
for t in temps:
   if t >= 30:
      print("고온", t)

# ===================================================


temps1 = [26, 28, 29, 31, 33, 35, 36]
total = 0
count = 0
for t in temps1:
   if t > 30:
      total += t
      count += 1
print("고온 평균:", total / count)