# set
# 자동 중복 제거
# 순서가 없음
# 형태는 중괄호로 감쌈

# 빈 set 만들기
empty_list =[]

print(type(empty_list))

empty_set = {}

print(type(empty_list))
# 빈 중괄호는 딕셔너리라는 다른 자료형으로 생성

# 빈 셋은 무조건 set() 내장함수를 사용
real_empty_set = set()
print(type(real_empty_set)) # <class 'set'>

# 값을 포함란 셋 만들기
logs = ["S01", "S02", "S03", "S04", "S05"]
# 리스트를 {}에 감싸

# 복수의 값을 중괄호에 감싸 작성
print("000")
unique = {"S01", "S02", "S03", "S04", "S05"}

# set() 사용
unique = set(logs)
print(type(unique))
print(unique)
# unique 셋에는 기존 중복되었던 so1이 한 번만 들어감
# 지금은 길이가 짧아서 순서대로 정렬된 것처럼 보이지만
# 셋은 순서가 없는 값의 묶음
# print(unique[0])
# set 에서 인덱스 사용시 Error 발생

# set에 바로 여러 값을 작성
unique = set(["S01", "S02", "S03", "S04", "S05"])

print(type(unique))
print(unique)

# set을 사용해서
# 리스트에 들어있는 유니크한 값의 종류 수를 알 수 있음
print(len(unique))

# =========================================================

# 셋에 값 추가하기
# 셋.add(추가할 값)
# 이미 있는 값을 추가할 경우 무시

alerts = {"S01", "S02"}

# 경고 상태인 S03이 추가될 경우
# .add()를 사용햐서 추가
alerts.add("S03")
print(alerts)

# S01에서 또 경고가 발생
# 이미 S01은 경고가 발생한 적이 있고
# alerts라는 셋에는 경고가 발생한 센서만 저장하고 싶음
# 횟수 상관 없이
# 이럴 때 set을 쓰면 편리함
alerts.add("S01")
print(alerts) # {"S03", "S02", "S01"}
# S01이라는 값을 또 넣어도 무시하고 한 번만 저장
# 그래서 독립적인 값을 저장하기에는{"S03", "S02", "S01"} 아주 편리하다

# ==============================================================
# set에 특정 값 포함 여부 확임
# ["S01", "S02", "S03", "S04", "S05"]
# {"S03", "S02", "S01"}
# 리스트와 셋을 비교해보면
# set이 길이가 짧음(중복울 제고하기 때문에)
# set은 인덱스가 없음
# 순회 속도가 리스트보다 훨씬 빠름

# print(alerts in "S01") #True
# 이렇게 출력하기보단 조건문을 활용해서
# 포함 여부 확인 후 특정 동작을 실행시킴

if "S01" in alerts:
  print("S01 정비 필요")

# ============================================================
# WOR_01 * 4, WOR_6 * 2, WOR_3 *1, WOR_5 * 1

sel = ["WOR_01", "WOR_03", "WOR_01", "WOR_05", "WOR_06", "WOR_06", "WOR_01", "WOR_01"]
unique = set(sel)
print(sorted(unique))
print("센서 종류 수:", len(unique))

# =========================================================

# 집합 연산
hour_14 = {"WOR_01", "WOR_06", "WOR_07","WOR_02"}
hour_15 = {"WOR_01", "WOR_07", "WOR_03", "WOR_09", "WOR_11"}

# 합집합
print(hour_14.union(hour_15))
print(hour_15.union(hour_14)) # 동일하다
# {'WOR_01', 'WOR_02', 'WOR_03', 'WOR_06', 'WOR_07', 'WOR_09', 'WOR_11'}
# 짧게 정리: 1, 2, 3, 6, 7, 9, 11
print(hour_14) # .union은 원본 셋에 변화 x

# | 연산자를 활용해 짧게 작성 가능
print(hour_14 | hour_15)

# 교집합
# union이랑 동일하게 똑같은 결과를 출력
# 앞뒤 순서가 결과레 영향을 미치지 않는다
print(hour_14.intersection(hour_15))
print(hour_15.intersection(hour_14)) 

# & 연산자 사용 교집합
print(hour_14 & hour_15)

# 3개의 print문은 공통으로 {'WOR_07', 'WOR_01'}출력

# 차집합
# 순서에 따라 결과가 다름
# 앞에 작성된 셋에서
# difference의 인자로 전달된 셋에 있는 값들을
# 제외한 결과를 출력
print(hour_14.difference(hour_15)) # {'WOR_02', 'WOR_06'}
print(hour_15.difference(hour_14)) # {'WOR_11', 'WOR_03', 'WOR_09'}

# {'WOR_02', 'WOR_06'}
# {'WOR_11', 'WOR_03', 'WOR_09'}

# - 연산자 사용 차집합
print(hour_14 & hour_15)
print(hour_15 & hour_14)
# 차집합은 순서에 따라 결과가 다른 것 유의
# 14-15와 15-14는 다름
# 빼는 방향에 따라 결과가 달라짐
