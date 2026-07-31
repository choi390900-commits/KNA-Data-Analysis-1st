# 자료 참고

# ==========================================================
tup = ("normal","noraml", "warning", "normal", "warning")

# 튜플의 길이
print(len(tup)) # 5

# 특정 값의 갯수 세지
print(tup.count("warning")) # 2

# 특정 값이 처음 나온 인덱스 찾기
print(tup.index("warning")) # 2
# 찾고자 하는 값이 없으면 Error 발생
print(tup.index("warning")) # valueError: tuple.index 발생

# ================================================================

# 튜플 리스트
# 리스트 안에 튜플을 담은 것을 표현
# for문으로 리스트를 사용해서 리스트 내부의 튜플에 접근하고
# 튜플에 담긴 값을 사용할 수 있음

# 언패킹을 사용해서 접근한 튜플 내부의 값을 변수에 바로 할당해서 접근

hour_13 = [("모터온도", 77), ("모터진동", 0.2), ("모터압력", 91)]

now = 0

for name, value in hour_13:
  now += 1
  print(now, "번째 반복")
  print("name:", name, "value", value)

# ================================================================

temps_13 = [("qox_001",81)]
temps_13 = [("qox_002",88)]
temps_13 = [("qox_003",95)]
temps_13 = [("qox_004",89)]

Warning = 90

for name, temp in temps_13:
  if temp >= Warning:
    print("경고", name, "설비 온도 이상")

# ======================================================================
# tup_list = [("일", "one", 1, "1"), ("이", "two", 2 "2"),]

# for kor_str
# ======================================================================

# 튜플 리스트 정렬
# sorted()를 사용하여 튜플의  특정값 기준으로 리스트를 정렬

temps_13 = [("qox_001",81), ("qox_002",88), ("qox_003",95), ("qox_004",89)]

# sorted()는 원본 배열을 수정하지 않고 새 리스트를 반환해줌
hot = sorted(temps_13, reverse=True)
print(hot)
print("원본:", temps_13) # 정렬 적용 X
# ======================================================================

st = ("모터온도", 78)
print(st)
print(st[0])
print(st[1])
name, value = st
print(name, value)

# =============================================================

sen = [("모터온도",85), ("모터진동", 0.6), ("펌프압력",70), ("펌프진동",1.2)]
for name, value in sen:
  print(name, value)
limit = 80
for name, value in sen:
  if value > limit:
    print(name, "경고")

# ===================================================================
sen1 = [("모터온도", 85, (3, 5)), ("모터진동", 2.6, (8, 2)), ("펌프압력", 75, (4, 6) ),]

for name, value, pos in sen1:
  x, y = pos
  print(name, "위치:", x, y)
for name, value, pos in sen1:
  x, y = pos
  if x <= 6:
    print(name, "3구역")

# ===============================================================

list_ = []
