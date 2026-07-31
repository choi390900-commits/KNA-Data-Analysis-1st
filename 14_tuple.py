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


# ===============================================================

temps = [25, 32, 28, 36, 27, 31, 24]
total = 0
count = 0
for t in temps:
 if t > 30:
  total += t
 count += 1
print("고온 평균:", total / count)

# ====================================================================

temps1 = [25, 26, 24, 28, 27]
fahrenheit = []
for t in temps1:
 fahrenheit.append(t * 1.8 + 32)
print(fahrenheit)

# ==================================================================

temps = [25, 32, 28, 35, 27, 31, 24, 33, 29, 36]
total = 0
for t in temps:
 total += t
print("전체 평균:", total / len(temps))
hot = []
for t in temps:
 if t > 30:
  hot.append(t)
hot_total = 0
for h in hot:
 hot_total += h
print("고온 개수:", len(hot))
print("고온평균", hot_total / len(hot))

# ===================================================== 

sensor = ("모터온도", 78)
print("원본 튜플:", sensor)

name, value = sensor

print("=== 언패킹 결과 ===")
print("센서 이름:", name)
print("센서 값:", value)

a =10
b =20
print(f"=== 교환전: a={a}, b={b} ===")

a, b = b, a

print(f"=== 교환 후: a={a}, b={b} ===")

# ============================================================

line_a = {"S01", "S02", "S03", "S05"}
line_b = {"S03", "S04", "S05"}

print(line_a.union(line_b))
print(line_a.intersection(line_b))
print(line_a.difference(line_b))
print(line_b.difference(line_a))

# =============================================================


y_day = {"S01", "S02", "S03"}
today = {"S02", "S03", "S05"}

print(today.difference(y_day))
print(today.intersection(y_day))

# ============================================================

sensors = [
    ("컨베이어_01", 78, 2.1),
    ("용접기_02", 92, 5.4),
    ("절단기_03", 85, 3.2),
    ("건조로_04", 101, 6.8),
    ("냉각탑_05", 67, 1.5),
    ("도장부스_06", 88, 4.1),
    ("성형기_07", 90, 2.9),
]

count_normal = 0
count_warning = 0
count_danger = 0

total_temp = 0
max_temp = 0
max_name = ""

danger_list = []

print("--- 1. 설비 상태 판정 리포트 ---")
for i, data in enumerate(sensors):
    name, temp, vib = data      
    if temp > 90 or vib > 5.0:
          status = "위험"
    count_danger += 1         
    danger_list.append(name)

   # elif temp >= 80 or vib >= 3.0:
    status = "주의"
    count_warning += 1
    #else:
    status = "정상"
    count_normal += 1        

    
    print(f"[{i + 1}] {name} (온도: {temp}, 진동: {vib}) ➔ 상태: {status}")
    

    total_temp += temp
    if temp > max_temp:
        max_temp = temp
        max_name = name


print("\n--- 2. 상태별 설비 대수 ---")
print(f"정상: {count_normal}대 | 주의: {count_warning}대 | 위험: {count_danger}대")


print("\n--- 3. 이상 설비 비율 ---")
total_count = len(sensors)
abnormal_count = count_warning + count_danger
abnormal_ratio = (abnormal_count / total_count) * 100
print(f"이상 설비 비율: {round(abnormal_ratio, 1)}%")


print("\n--- 4. 평균 온도 ---")
avg_temp = total_temp / total_count
print(f"전체 평균 온도: {round(avg_temp, 1)}도")


print("\n--- 5. 최고 온도 설비 ---")

print(f"설비명: {max_name} (온도: {max_temp}도)")


print("\n--- 6. 위험 설비 목록 ---")
danger_list.sort()  
print(danger_list)


print("\n--- 도전! 최종 알림 ---")
if count_danger > 0:
    print("⚠ 즉시 점검 요망")
else:
    print("✅ 전 설비 안정")