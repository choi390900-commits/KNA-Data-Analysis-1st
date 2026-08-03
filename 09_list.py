# list는 python의 자룡형 중 하나
# 여러 개의 값을 [대괄호]에 감싸서 순서대로 저장
# 나열된 갑들은 자동으로 각자의 인덱스 번호를 순서대로 가지게 된다

temps = [35, 36, 37, 38] # int 리스트 
float_temps = [36.4, 36.5, 36.6, 36.7] # float 리스트
machines = ["펌프", "압축기", "모터"] # string 리스트

# 자료형이 달라도 한 리스트에 담을 수 있음
mixed = ["펌프", 78, True]

# 리스트에 자동으로 순서 인덱스가 붙는다면?
print(temps[2]) # 37 > 인덱스로 해당 순서에 위치한 요소 뽑아내기 가능

# 리스트 안에 몇 개의 값이 담겼는지 모르지만 마지막 요소를 뽑아내고 싶다면?
print(temps[-1]) # 가장 마지막 요소 출력 된다

# 빈 리스트
empty = [] # 아무 값도 없는 리스트

# 리스트에 담긴 값의 갯수 세기
# len() 내장함수
print(len(temps)) # 4
print(len(empty)) # 0


# 리스트에 담긴 값의 갯수 변수에 저장
temps_length = len(temps) # 변수에 4라는 값이 할당
print(temps_length) # 4

# ===================================================
# 리스트의 인덱스
print(temps[0], temps[-1]) # 가장 첫 번째 요소, 가장 마지맏 요소
# -1을 사용하는 이유는 최신 값은 대체로 뒤에 추각 됨
# 가장 최신 값은 결국 마지막 인덱스의 요소
# len 함수를 사용해서 리스트 길이 -1 로 게산이 가능하지만
# 이 작업이 번거로워 -1을 가장 많이 사용

# 없는 인덱스 호출
# temps 리스트는 길이가 5
# print(temps[5]) # indexError: list index out of range
# 인덱스 법위를 벗어나지 않도록 유의

# 리스트의 자료형
print("=== 리스트의 자료형 ===")

# temps라는 리스트 자체
print(f"temps[0]: {temps}") # [35, 36, 37, 38]
print(f"type(temps): {type(temps)}") # <class 'list'>

# temps라는 리스트의 0번째 인덱스 요소
print(f"temps[0]: {temps[0]}") # 35
print(f"type(temps[0]): {type(temps[0])}") # <class 'int'>

# 다른 자료형의 값이 들어있는 리스트의 요소 타입
# float 값 들어있는 float_temps 리스트의 0번째 요소
print(type(float_temps[0]))
print(type(machines[0])) # <class 'srt'>

# 퀴즈
# mixed = ["펌프", 78, True]

print(type(mixed[1])) # <class 'int>
print(type(mixed[-1])) # <class 'bool'>
print(type(mixed))  # <class 'list'>

# 다른
# ==============================================

li = [32, 33, 34, 35, 36]
print(li)
print(len(li)) # 5
st = []
print(st)
print(len(st)) # 0

# ===============================================

# 리스트의 인덱스
print(temps[0], temps[-1]) # 가장 첫 번째 요소, 가장 마지막 요소 출력
# -1을 사용하는 이유는 최신 값은 대체로 뒤에 추가가 됨
# 가장 최신 값은 결국 마지막 인덱스의 요소
# len 함수를 사용해서 리스트 길이 -1 로 계산이 가능 하지만
# 이 작업이 번거로워 -1을 가장 많이 사용

# 없는 인덱스 호출
# temps 리스트는 길이가 5
# print(temps[5]) # IndexError: list index out of range
# 인덱스 범위를 벗어나지 않도록 유의

# ================================================

temps1 = [32, 33, 34, 35, 36, 37]
print(temps1[3])
print(temps1[2])
print(temps1[-1])

ts = [110, 120, 130, 140, 150]
fs = ts[1] # 120
sl = ts[-1] # 150
print(fs + sl) # 120 + 150 = 270
print((fs + sl) / 2) # 135.0

# ================================================
print("===== 리스트의 자료형 =====")

# temps라는 리스트 자료 지체
print(f"temps: {temps}")
print(f"temps: {temps}")

# temps라는 리스트dml 0번째 인덱스 요소
print(f"temps[0]: {temps[0]}")
print(f"type(temps[0]): {temps[0]}")

# 다른 자료형의 값이 들어있는 리스트의 요소 타입
# float 값이
print(type(float_temps[0])) # float
print(type(machines[0])) # str

# ===============================================
# 리스트 슬라이싱
# 리스트명 [시작:끝:간격]
# 시작, 끝, 간격 인덱스는 모두 생략이 가능하다(문자열과 동일)

# temps = [35, 36, 37, 38]
print(temps[1:3]) # [36, 37] > 1번 인덱스부터 3번 인덱스 전까지
print(temps[1:2]) # [36]
print(temps[:2]) # [35, 36]
print(temps[:2], temps[3:5]) # [35, 36] [38]
print(temps[::1]) # [35, 36, 37, 38] > 처음부터 끝까지 1칸씩
print(temps[::3]) # [35, 38] > 처음부터 끝까지 3칸씩
# print(temps[100:999]) # [] > 범위를 벗어나면 빈 리스트 반환

# 인덱싱 vs 슬라이싱
# 인덱싱 temps[0]은 값 하나(35)
# temps[999]와 같이 없는 인덱싱 사용 시 에러


# 슬라이싱 temps[0:2]은 리스트([35,36])
# 슬라이싱은 역영을 잘라내는 역활이기 때문에 리스트를 반환하는 것
# temps[100:999] 에러 발생하지 않음
# 슬라이싱은 범위를 벗어나면 빈 리스트를 반환

# ================================================

temps3 =[31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
print(temps3[:3]) # [31, 32, 33]
print(temps3[-3:]) # [38, 39, 40]
print(len(temps3[:3])) # 3

ho = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
fi = ho[:6]
sh = ho[6:]
print(fi)
print(sh)
print(len(fi), len(sh)) # 6 6

# ===============================================

# 인덱스로 특정 값 바꾸기 > 문자열과 다름
# temps = [35, 36, 37, 38]

print("원본:", temps)
temps[2] = 999
print("2번 인덱스 값 변경 결과:", temps)

# in (존재 확인)
# machines = ["펌프", "압축기", "모터"]
print("펌프" in machines) # True
print("펌프" not in machines) # False

print("프레스" in machines) # False

# 특정 값의 인덱스 찾기
# machines = ["펌프", "압축기", "모터"]

i = machines.index("압축기") # 1
print(i)

# .index() 메서드는 이스트에서 가장 처음 등장하는 인덱스만 반환
machines = ["펌프", "압축기", "모터", "펌프"]

# ===============================================

temps5 = [35, 36, 240, 37, 38]
print(240 in temps5)
i = temps5.index(240)
temps5[i] = 34
print(temps5) # [35, 36, 34, 37, 38]
print(240 in temps5) # False

# ===============================================

# 리스트 값 추가
# .append(추가 할당)
# 리스트의 가장 마지막에 값 추가
# 리스트 원본이 수정(재할당 필요 X)

nums = [1, 2, 3, 4 ,5]

nums.append(999)
print(nums)

# 만약 원본 리스트와 특정 값을 추가한 리스트 둘 다 필요하다면
# 원본 리스트를 복사해서 리스트 수정 진행
# nums = [1, 2, 3, 4, 5, 999] > 기존 리스트는 원본으로 둠

new_nums = nums  
print (new_nums) # [1, 2, 3, 4, 5, 999]

new_nums.append(111)
print("원본 nums 리스트:", nums)
# 기대 결과: [1, 2, 3, 4, 5, 999]
# 실제 결과: [1, 2, 3, 4 5, 999, 111]
# 복사한 메모리 주소에 append를 했기 때문에 뭔본까지 영향을 받음

# 이를 해결하기 위해서 .copy()라는 메서드를 사용
# new_nums는 새로운 메모리에 nums 배열을 새로 저장
new_nums2 = nums.copy()
new_nums2.append(222) # nums 배열에 영향을 미치지 않고 사용
print("원본 nums 리스트:", nums)
print("복사본 new_nums에 222 append 결과:", new_nums) 

# .insert(위치, 값)
# 리스트에서 원하는 위치에 값을 삽입
# 원본 배열에 바로 삽입
# 기존 배열에서 삭제는 되지 않고, 해당하는 인덱스 값이 삽입(뒤에 요소 삽입)
nums.insert(3, 333)
print(nums)

# ========================================
# extend()
# 리스트 연결
# 다른 리스트의 값들을 "풀어서" 이어붙임
data = [1, 2, 3]
new_data = [4, 5, 6]
data.extend(new_data)
print(data)

# 함수의 반환 개념을 안 뒤에 확인할 내용
print(data.extend(new_data))
# 기대 결과: [1, 2, 3, 4, 5, 6]
# 실제 결과: None
# extnd() 메서드는 data라는 리스트를 "수정" 이를 변환하지 않음
# 반환값이 없어서 print를 할 값이 없는 것
print(data) # [1, 2, 3, 4, 5, 6]

# 리스트를 수정하는 메서드는 모두 반환값이 없는가
print(data.append(123)) # None
print(data.insert(0, 123)) # None
print(data.extend(new_data)) # None
# 일단 현재 배운 메서드는 반환값이 없음

# 정리
# 오늘 꼭 알아야 하는 리스트 수정 메서드와 개념
# .append(추가할값): 리스트의 가장 마지막에 값을 추가
# .insert(위치, 값): 첫 번째 인자인 위치 인덱스에 값을 저장
# .extend(합칠리스트): 두 리스트를 하나의 리스트로 합체
# 위 세 가지 메서드들은 원본

# ==================================

list =[10, 20, 30, 40, 50, 60]

list = []
list.append(35)
print(list)
list.insert(0, 5)
print(list)
list.extend([10, 20, 30, 40, 50, 60])
print(list)

# ============================================

# 리슽에서 요소 삭제하기
# .remove(값): 위치는 모르고 삭제할 '값' 만 알 때 사용하는 요소 삭제
list1 = ["딸기", "사과", "배","포도", "수박" , "망고"]
list1.remove("수박")
print(list1)

# .pop(인덱스)
# 삭제한 인덱스의 값을 반환
list1.pop(0)
print(list1)
print(list1.pop(2)) # 삭제한 인덱스 2번의 값인 포도 출력
# 삭제도 하고, 삭제한 인덱스 값도 출력
print(list1)

# 없는 인덱스 값도 삭제 불가 > Error 발생

# del: 인덱스로 리스트의 요소 삭제 (슬라이싱으로 영역 삭제 가능)
del list1[0]
print(list1)

del list1[:]
print(list1) # [] > 빈 리스트가 됨

# =================================================

tt = [25, 26, 999, 27, 28, 26]
tt.remove(999)
print(tt)
y = tt.pop(1)
print(tt)
print(y)
del tt[0]
print(tt)

# =========================================================

# 리스트 정렬하기
# 리스트.sort()
# 데이터를 정렬하는 친구
# 기본적으로 오름차순(작은 숫자부터 큰 숫자까지)
# 내림차순으로 정렬하고 싶은 겅우에는 .sort(reverse=True)

n = [37, 2, 8, 109, 1004, -1, 22]
print("n 리스트 원본:", n)

# 오름차순 정렬
n.sort() # 원본 리스트 순서 정렬
print("n 리스트 오름차순 정렬 결과:", n)

# 내림차순 정렬
n.sort(reverse=True)
print("n 리스트 내림차순 정렬 결과", n)

# 리스트 순서 뒤집기
# .reverse()
# 값의 크기대로 정렬하지 않는다
# 정렬은 해주지 않음
# 뒤로 게속 쌓인 결과(최신)를 앞에서부터 보고싶을 때 사용

n = [37, 2, 8, 109, 1004, -1, 22]
print("n 리스트 원본:", n)

n.reverse()
print("n 리스트 순서 뒤집기 결과:", n)

# 리스트 안 값의 갯수 구하기
# .count(찾을 값)

f = ["텀블러", "일회용컵", "일회용컵", "일회용컵", "텀블러", "텀블러", "일회용컵"]
print(f.count("일회용컵"))
print(f) # 원본 배열에 변화 없음

# 특정 값의 위치 찾기
# .index(위치를 찾을 값)
# 리스트에서 가장 첫 위치만 찾아줌
print(f.index("일회용컵")) # 1
print(f) # 원본 배열에 변화 없음

# ===========================================================

ondo = [29, 30, 34, 32, 33, 31, 30]
ondo.sort()
print(ondo)
ondo.reverse()
print(ondo)
print(ondo.count(30))
print(ondo.index(30))
# ==========================================================
# 복습

# [] 리스트 만들기
# temps = [1, 2, 3, 4, 5, 6]
# print(temps) > [1, 2, 3, 4, 5, 6]

# [] > 여러 값을 한꺼번에 모아서 리스트를 만듬

mac = ["설비", "모터", "펌프", "압축기"]
print(mac) # ['설비', '모터', '펌프', '압축기']로 출력됨

choi = [] # 빈 리스트 > [괄호] 안이 비어있음 
print(len(choi)) # 0

# 빈 리스트 와 길이 len() 확인

print(len(mac)) # 4(담긴 값의 갯수

# 인덱스(index)는 0부터 시작한다
# test = [1, 2, 3, 4, 5, 6]
#         0  1  2  3  4  5
# print(test[0]) > 1 (첫 번째가 출력됨)
# print(test[4]) > 5 (네 번째가 출력됨)
# print(test[-1]) > 6 (마지막 값이 출력됨)

# test = [1, 2, 3, 4, 5, 6]
#        -6 -5 -4 -3 -2 -1

# print(test[-1]) > 6 (7 - 1 = 6으로 마지막 인덱스 값이 계산 되서 출력)
# print(test[-2]) > 5 (6 - 2 = 5으로 계산 되서 출력)

# ============================================================
