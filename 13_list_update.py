# 기존 배열의 모든 요소에 3을 곱하여
temps = [1, 5, 2, 7, 4, 8, 10, 3]
doubled = []

for t in temps:
  doubled.append(t * 3)

print(doubled)

# 조건에 맞는 값으로 새 리스트 만들기

# temps = [1, 5, 2, 7, 4, 8, 10, 3]

high = []
low = []

for t in temps:
  if t < 5:
    low.append(t)
  else:
    high.append(t)

print("high:", high)
print("low:", low)

# 복습) sort(): 원본 배열을 오룸차순으로 정렬해줌
# 하지만 반환해주지 않기 때문에 print로 바로 찍으면 None 출력
print(low.sort)

# ============================================================
temps2 = [25, 26, 30, 31, 29, 28, 32, 27, 33, 35]
li = []
for t in temps2:
  if t >= 30:
    li.append(t)
print(li)
print(len(li))