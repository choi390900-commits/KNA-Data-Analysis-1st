# 반복문은 동일한 작업을 특정 횟수만큼 반복해야할 때
# 코드를 길게 쓰지 않고 반복시킬 수 있음

# for 변수 in rnage(횟수):
#   반복시킬 코드 (들여쓰기 한 칸 필수)
# 같은 코드를 복사 붙여넣기로 여러번 작성하는 대신
# "N번 실행해라"는 의미

for i in range(3):
  print("안녕하세요!") # range에 전달한 인자 3번 반복
  # i를 쓰지 않아도 됨 -> 목적이 "3번 반복"일 때

# 0부터 10까지의 숫자 자체가 필요하거나 출력할 때
for i in range(11):
  print(i)
  # i는 증가값을 지정하지 않는 이상 반복할 때마다
  # 자동으로 +1이 적용됨

# 0부터 10까지 짝수만 필요할 때
for i in range(0, 11, 2): # range(시작, 끝, 증가값)
  print(i) # 반복할 때마다 i가 2씩 자동으로 증가

# 1부터 10까지 홀수만 출력
for i in range(1, 11, 2):
  print(i)

# 역순으로 출력
for i in range(10, 0, -1):
  print(i)

# 10부터 1까지 역순으로 출력
for i in range(10, 0, -2):
  print(i)

for i in range(0, 10, -2):
  print(i)
# 

# ====================================================

n = int(input("끝 숫자 N을 입력하기: "))
for i in range(1, n, 1):
  print(i)
for i in range(2, n + 1, 2):
  print(i)
for i in range(n, 0, -1):
  print(i)

# =========================================================
lim = int(input("사용자 입력값: "))

for i in range(1, lim + 1):
  if i % 3 == 0:
    if i == 3:
     print(1, end=" ")
    else:
      print(f", {i}", end="")
      
# ===========================================================

dan = int(input("구구단 2의 배수 단만: "))
for dan in range(1, 10):
  # dan이 2의 배수인 경우에만 출력
  if dan % 2 == 0:
    print(f"=== {dan}단 ===")
    for i in range(1, 10):
      print(f"{dan} * {i} = {dan * i}")
    print()