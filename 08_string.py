

notice = """ 설비 점검 안내



print(notice)
# 설비 점검 안내
# 1. 전원 확인
# 2. 센서 점검




# 탭
notice = """ 

print(notice)

tab = "이름\t상태"
# print(tap)
print("이름 상태")

backslash = "이름\\상태"
print(backslash) # 이름\상태 > 첫번째 \는 이스케이프 문자라는 것을 알리는 용도


quotes = 'Tt\'s me' # 감싸는 따옴표와 str 내부 따옴표의 종류가 같을 때는 \를 사용
print(quotes)

# 빈 문자열와 공백 문자열의 차이 
# "" 따옴표로 감싸겠지만 아무것도 작성되지 않았다면 "빈 문자열"
# 빈 문자열은 굴자 수 0, 길이 0
# " " 따옴표 안에 공백(스페이스바)이 있는 경우는 "공백 문자열"
# 공백(스페이스바)의 수 만큼 굴자가 있고,길이가 세어짐
# 빈 문자열과 공백 문자열은 컴퓨터에게 다른 값으로 인식됨 
print("" == "  ") # False

# ===========================
code = "PUMP_A"
state = "정상"
hours = 1200
day = "2026-07-16"
s_card = "설비: " + code + "\n상태: " + state + "\n가동: " + str(hours) + "시간\n점검:" + day
print(s_card)
# 예상 결과
# 설비: PUMP_A
# 상태: 정상
# 가동: 1200시간
# 점검:2026-07-16

# ==================================
# 인덱싱 - 위치 번호로 글자를 하나 꺼내기
# 문자열 [인덱스 번호]
# 문자열의 첫 글자 인덱스는 무조건 0부터 시작

word = "PYTHON"
print(word[0], word[3], word[5]) # P H N

# print(word[100]) # IndexError
# word 변수에 저장된 문자열의 길이보다 큰 인덱스를 호출했기 때문

abc = "abcdefghijklnmopqrstuvwxyz"
# 자기 이름 출력하기 (성빼고)
print(abc[10], abc[24], abc[20], abc[8], abc[12])

# 음수 인덱스는 뒤에서부터 역순으로 순서가 붙음
# 주의사항은 음수 인덱스는 가장 마지막 글자가 -1부터 시작

# ===========================================
print("======= 슬라이싱 ======")

# 슬라이싱 - 구간으로 잘라내기
# 문자열 [시작: 끌]
# 시작 인덱스 글자는 포함해서 출력
# 끝 인덱스 글자는 제외하고 출력

print(word[3:5]) # HO
print(word[3:6]) # HON
#슬라이싱은 end가 포함되지 않고 출력하기 때문에 없는 인덱스인 6도 사용할 수 있음

# print(word[6]) # 인덱싱은 정확하게 마지막 인덱스까지만 쓸 수 있고, 넘치면 Error
 # 슬라이싱 - start 생량
 # 처음부터 특정 인덱스까지 구간을 뽑아내고 싶을 때 사용
print(word[:4]) # print(word[:4])와 동일한 동작

# 슬라이싱 - ned 생략
# 특정 인덱스부터 끝까지 구간을 뽑아내고 싶을 때 사용
print(word[2:]) # 2번 인덱스부터 끝따지 출력
# print(word[2:6])과 동일한 동작

# 슬라이싱 - 전체 생략
print(word[:]) # print(word[:])와 동일한 동작
# :을 사용하고 start와 end를 모두 생략하면 모든 인덱스의 구간을 뽑아냄

# 슬라이싱 - 음수 인덱스 사용
print(word[-3:]) # HON
# 음수 인덱스 작성 시 그냥 그 인덱스부터 정방향으로 출력함
print(word[:-1]) # PYTHON
# 처음부터 -1(5)를 제외한 구간을 뽑아냄
# 역순 아님 주의
# 음수 인덱스 사용 시 컴퓨터가 알아서 정수 인덱스 찾아 치환해서 동작

# step으로 건너뛰기
# 문자열[시작:끝:간격(step) 
print(word[0:6:2]) # PTO
# PYTHON에서 첫 번째 글자는 명시했으니 거기서부터 출력
# step이 2이기 때문에 Y 뛰고, T(두번째 점프) 출력
# # H 뛰고, O(두번째 점프) 출력
# N 뛰고 끝
# 두 글자를 뛰는게 아니라 두 "번" 뛰는 것 (뛴 그 자리 글자를 출력한다)

print(word[0:6:1]) # PYTHON

# start와 end를 생략하고 step만 입력
print(word[::2])
# word 변수의 모든 글자를 두 칸씩 뛰면서 출력

# 순서 뒤집기
print(word[::-1])
# step은 인덱스가 아니고, 음수 입력 시 


# ==============================
word = "temp_sensor"
print(word[:4])

print(word[5:])

word = "sensor_01"
print(word[-2:])

word ="PYTHON"
print(word[::2])

print(word[::-1])

# 슬라이싱은 범위를 벗어나도 오류가 발생하지 않음
print("범위를 벗어난 슬라이싱", word[0:100]) # PYTHON으로 정상 출력
# =========================
# ien() - 문자열을 길이 반환
# ien(문자열)

print(len("hello world!")) # 12 (공백도 모두 글자 취급)
print(len("")) # 0(빈 문자열 0 출력)

var = "여러분 한시간만 더 하면 됩니다! 조그만 더 힘을 내주세요!"
print(len(var)) # 변수에 담긴 문자얄의 길이 출력도 가능 

# print(len("이것도")) - len("가능할까?")
# len()은 int를 반환하기 때문에 연산 가능

print("abc 변수의 길이:",len(abc), " / 마지막 인덱스 번호:", len(abc))

# 음수 인덱스를 사용하지 않고 마지막 인덱스 문자를 뽑고 싶을 때
print(abc[len(abc) - 1])

phone = "01012345678"
print(len(phone))

# ===================
print("==== in 활용 ====")

# in - 특정 문자가 문자열에 포함되었는지 여부 확인
# "여부"를 확인하기 때문에 True 또는 False (bool)으로 결과 반환
# 찾을 문자열 in 문자열
print("고장" in "설비 고장 발생") # True
print("정상" in "설비 고장 잘생") # False
print("설비에서 고장" in "설비 고장 발생") # False
print("설비에서 고장" in "설비에서 고장이 났습니다") # True

print("고장" not in "설비 고장 발생") # False
print("정상" not in "설비 고장 잘생") # True
print("설비에서 고장" not in "설비 고장 발생") # True
print("설비에서 고장" not in "설비에서 고장이 났습니다") # False

print("" in "설비 고장 발생") # True
# 따옴표로 감싼 공백(스페이스바)는 정말 한

# =================================
print("=== count() ===")
# .count() - 문자열에 특정 글자의 수(int)를 반환
# 문자열의 .count("찾을 글자")
print("banana".count("a")) # 3
print("010-1234-5678".count("-")) # 2
print("layla@spreatics.com".count("@")) # 1

# =======================================
print("a,b,c,d".count(",")) # 3

print("==== find() ===")
# 전달받은 글자가 "첫 번째"로 나오는 위치 인덱스 반환
# 찾는 글자가 없다면 -1을 반환

email ="hong@company.com"
at = email.find("@") # @ 위치를 인덱스인 4가 할당
uesr_id = email[:at] # hong


print("a,b,c,d".find(","))
print("a,b,c,d".find("s"))

# SQE-00Q8이라는 설비의 SQE만 뽑아내기 (find와 슬라이싱 사용)
sqe = "SQE-00Q8"

sqe_index = sqe.find("SQE")
print(sqe_index) # 0

sqe_index = sqe.find("-")
print(sqe_index) #3
sqe_fin = sqe[:sqe_index] # aqe[0:3] > SQE
print(sqe_fin) # 



# ============================================
print("=== index() ===")

# 특정 문자열의 위치(인덱스 번호)를 반환
# 앞에서부터 가장 처음 나오는 인덱스 번호만 반환
# 찾는 문자열이 없으면 error가 발생한다

email = "choi390900@gmail.com"
at = email.index("@") # 10
print(email[0:at]) # choi390900
print(email[:at]) # 시작 번호가 0이라면 start 생략가능
print(email[at:]) # 끝까지 출력하고 싶고, 뒤에 몇 글자가 있는지 모르니 생략
# 위처럼 시작하면 5번 인덱스부터 출력하기 떄문에 @을 포함
print(email[at+1:]) # at +1을 하면 @을 포함하지 않고 출력

# find에서 했던 SQE 뽑아내기 index 사용해서 바꾸기
# sqe = "SQE-00Q8"
# sqe_index = sqe.index("/")
# print(sqe_index)
# sqe_fin = sqe[:sqe_index]
# print(sqe_fin)
# ====================================================
print("=== count() ===")

# 문자열에서 특정 문자열의 갯수 세기

# str = "a, b, c, d, e, a, a"

# a의 갯수 세기
# print(str.count("a")) # 3

# ,의 갯수 세기
# print(str.count(",")) # 6

# print(str.count(", ")) # 

# ================pr==============
print(" === startswith() ===")

# 특정 문자열로 시작하는지 검사
# true/false (불리언)

# EQP로 시작하는지 검사하기
print("EQP-001".startswith("EQP"))

# 변수 활용
eqp = "EQP"
print("EQP-001".startswith)
# 주위사항) 변수명

# =================================
print("=== endswith() ===")

# 특정 분자열로 끝나는지 확인
# true/false로 반환

str2 = "월요일이네! 시간아 빨리가라!"

print(str2.endswith("!")) # True
print(str2.endswith("네!")) # True
print(str2.endswith("라!")) # True
print(str2.endswith("월요일이네! 시간아 빨리가라!")) # True
print(str2.endswith("월요일이네! 시간아      빨리가라!")) # False
print(str2.endswith("월요일이네! 시간아 빨리가라! ")) # False
print(str2.endswith(" 월요일이네! 시간아 빨리가라! ")) # False

# ===========================================

fname = "senscr_log.csv"
print(fname.startswith("senscr"))
print(fname.endswith(".csv"))

# =================================
print("=== 값은 객체다 ===")

print(type("잊어먹으면 안돼"))
print(len("사용방법"))
# endswith와 len의 차이는
# endswith는 .으로 연결
 # .으로 연결하는 이런 도구들은 "메서드"
 # 문자열이나 int, float처럼 특정 자료형(객체) 내부에 포함된 기능
 # len 은 . 사용 안함
 # () -> 함수
 # len과 같이 개발자가 직접 선언하지 않은 기본 제공 함수 "내장함수"

"str".startswith("s")
# 123.startswith(1)
# .으로 사용하는 메서드들은 특정 자료형(객체 타입)마다 다름
# 


# =================================
# 재할당 복습

num = 1
num = num + 1 # 2
num += 1 # 3
# += 은 복합할당연산자 원래 내 자신의 값에 다음 오는 연산자와 값을 적용해서 재할당

# ===========================
print("====== .upper() ======")

str3 = "abcdef"
print(str3) # abcdef

str3.upper # ABCDEF > 반환은 대문자인데 값에 재할당은X
print(str3) # abcdef > 기존 str3의 값인 소분자를 그대로 출력

# 앞으로 게속 대문자로 변환한 값으 사용하고 싶다면
# 변수에 재할당
# 변수 재할당에서 변수 스스로 값을 부르려면 무조건 "재할당"이여야 함
# str3 = str.upper()

# 최초 변수 할당 세에는 저장된 값이 없어서
# 변수 스스로 값을 불러와 할당 불가능
# 

# =============================

a = "ready"
dee = a.upper()
print(dee)

w = "WARNING"
bee = w.lower()
print(bee)

user_name = "choi kyu in"
# 첫번째 문자를 대문자로 변경
print(user_name.capitalize())

# 띄어쓰기 마다 첫번째 문자를 대문자로 변경
print(user_name.title())

#'를 사용한 경우 다른 단어로 인식
print("i'm full".title())
print('i\'m full'.title())

# ====================================

# 소문자 대문자 구분
print("ABC".isupper())
print("abc".islower())
print("ABc".islower())

#
tname = "sensor_LOg.csv"
low = tname.lower()
#print(low.startswith())
#print(low.endswith())
#print(tname.endswith())

# ===================================
print("=== strip ===")

# 공백 제거
# .strip(): 앞과 뒤에 모든 공백 제거 (중간에 띄어쓰기는 그대로 유지)
# .lstrip(): left(왼쪽) 공백만 제거
# .rstrip(): right(오른쪽) 공백만 제거
raw = "   정상     "
print(raw.strip())
print(raw.lstrip())
print(raw.rstrip())

# 문자열의 가운데 공백은 strip을 지우지 못함
print("   정    상   ".strip())
print(raw)
# strip은 재할당이나 새 변수에 할당하지 않는 이상 휘발

# strip으로 문자 제거
str4 = "===정상==="
print(str4.strip("="))
# 인자로 전달한 양 끝의 =이 모두 지워짐

str5 = "==정상======="
print(str5.strip("="))
# 갯수 상관 없이 인자로 전달한 문자를 주조건 삭제
print(str5.strip("= "))
# strip 자체가 공백을 지우는 것이기 때문에
# 공백 상관없이 양 끝의 해당 문자열 삭제

str6 = "==정==상===="
print(str6.strip("="))
#

r = " 가동중 "
run = r.strip()
print("[" + run + "]")

# =============================
print("==== 체이닝 =====")

raw = "    NORMAL    "
step1 = raw.strip()
step2 = step1.lower()


raw = raw.strip()
raw = raw.lower()


# 체이닝
chain = raw.strip().lower()


raw = raw.strip().lower()

# ===================================
print("=== 실습 ====")

str = "    Warning    "
str.strip()
print("[" + str + "]")
str = str.strip()
print("[" + str + "]")

# ==================================
print("=== replace ===")

# 특정 문자열을 제거하거나 치환할 때 사용
# 제거할 때는 인자의 두 번째를 ""(빈문자열)로 작성
# .replace("바꾸고싶은 문자열", "바꿀문자열")
# 저거할 때는 인자의 두 번째를 ""(빈문자열)로 작성
print("정 상 가 동".replace(" ",""))
print("정        상 가 동".replace(" ",""))
print("정        상 가 동".replace("  ",""))

# 글자 치환
print("고장".replace("고장","fault")) # fault
print("고장".replace("고","fault")) # fault장

# 단어 치환
str9 = "설비 정상 가동"
print(str9.replace("정상","점검")) # 설비 점검 가동

# replace() 체이닝
num = "   010-1234-5678   "
num = num.replace(" ","").replace("-", "") # 01012345678

# ============================================
print("====== split =======")
# 문자열 자르기
# 결과는 대괄호에 감싸진 "리스트" 자료형
# 리스트는 순서가 있기 때문에 왼쪽에서부터 0으로 시작하는 인덱스가 자동 생성

drinks = "에스프레소 아메리카노 카페라떼" 
print(drinks.split()) # 인자를 보내지 않음
# ['에스프레소', '아메리카노', '카페라떼']
# "띄어쓰기"를 기준으로 나뉘어진 세 개의 문자열을 대괄호에 감싸서

# 구분자를 특정하고 싶은 경우
fruits = "딸기,거봉,키위,사쿠란보"
print(fruits.split(",")) # 문자열 콤마를 기준으로 분할

fruits2 = "딸기, 거봉, 키위, 사쿠란보"
print(fruits.split(",")) #  문자열 콤마를 기준으로 분할


print(fruits.split(", ")) #  문자열 콤마 + 공백 1칸을 기준으로 분할

# 리스트의 인덱스
fruits_list = fruits.split(",")
print(fruits_list)

# 거봉만 출력하기
# 출력하고자 하는 요소의 인덱스를 대괄호로 감싸서 호출
print(fruits_list[1]) # 거봉
print(fruits_list[3]) # 사쿠란보
print(fruits_list[-1]) # 사쿠란보
# split 횟수 제한
num = "010-1234-5678"
# ["010", "1234-5678"]
print(num.split("-", 1))

# ==========================

a = "a,b,c,d"
print(a.split(","))

# ===================================
print("==== join() =====")
# 리스트를 하니의 문자열로 합침
# "구분자".join(리스트)
# 모든 요소가 합쳐져서 하나의 문자열로 반환

fruits_list = ['딸기', '거봉', '키위', '사쿠란보']

"-".join(fruits_list) # "딸기-거봉-키위-사쿠란보"
",".join(fruits_list) # "딸기,거봉,키위,사쿠란보"
", ".join(fruits_list) # "딸기, 거봉, 키우, 사쿠란보"

# ===================================
num = ["2025", "01", "15"]
print("-".join(num))

# =================
# 실습 python을 pyThon으로 바꾸기
# 잘 모르는 부분
py = "python"
print(py[:2] + py.strip("py").capitalize())

print(py.replace("t",'T'))

print(py[:2] + py[2].upper() + py[3] + py[4] + py[5])

print(py[:2] + py[2].upper() + py[3:])

# ================================================
print("==== print 함수의 sep, end ====")

print("2026", "07", "27") # 2026 07 27 (기본으로는 공백 1칸)

# sep 속성을 사용하면 구분을 공백이 아닌 특정 문자열로 가능
print("2026", "07", "27", sep = "사랑해")
# 공백 대신 sep 속성에 전달된 문자열이 삽입되어 이어짐

print("안녕", "하세")
print("안녕", "하세", end ="요")
# end 속성 사용 시 출력은 마지막에 해당 문자열리 붙어 삽입

print("안녕", "하세", end="요")

# print("안녕", "히세", end="요", "ㅎㅎ") # end 속정 뒤에 또 인자

# print 함수 + 사용 시 sep과 end
print("안녕", "하세", end="요" + "이렇게?!") # 정상 작동 (사용은 자제 하자)

# 기본적으로 print문에는 sep으로 공백 한 칸
# end로 \n(줄바꿈)
#
#
print("이런식으로 쓰죠?", "근데 안보이는 기본값이 있어요", sep=" ", end="\n")

# =============================

w = "2026/07/27"
p = w.split("/")
print("-".join(p))

# ====================================

a = "1, NORMAL, 25.3"
s = a.split(",")
c = s[1].strip().lower()
print(c)

# ====================================

name = "PUMP_A"
temp = 87
print(f"설비{name}, 온도{temp}도")
# 출력 값: 설비 PUMP_A, 온도87도

# print("설비 " + name + ", 온도 " + str(temp) + "도")
# ====================================
print("=== f-string() ===")
# f-string - 문자열 안에 변수값을 바로 넣을 수 있는 기능

hour = 8

# 우리는 하루에 8시간 수업을 듣고, 이는 480분 입니다
print(f"우리는 하루에 {hour}시간 수업을 듣고, 이는 {hour * 60}분 입니다")

# ============================================
a = 100
b = 80
c = 75
print(f"평균 {(a+ b+ c) / 3}")

rt = 87.456
print(f"측정값 {rt}")
print(f"측정값 {rt:.1f}")
print(f"측정값 {rt:.2f}")

# =====================================

ra = " 5 , sensor_2 , WARNING , 0.78912"
pa = ra.strip().split(",")
si = pa[1].strip()
st = pa[2].strip().lower()
rr = float(pa[3].strip())
print(f"[센서: {si}], 상태: {st}, 측정값: {rr:.2f}")

# =====================================

print("=== 리스트 ===")

