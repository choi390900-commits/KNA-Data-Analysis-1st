# print 함수
print("안녕하세요")

first_name = "KYU"
middle_name = "IN"
last_name = "CHOI"
print(first_name)
print(last_name)
print(first_name, middle_name, last_name)
print(f"{first_name} {last_name}")

# 위와 같이 똑같은 print를 호출에도
# 다양한 방법의 호출리 가능합니다
# 그원리를 알려면
# 우리가 직접 함수들을 만들 수 있어야합니다

# 에러(Error)의 종류
# 1. 실행중에 오류(runtime Eroor) - 작동 중단됨
# 2. 논리적 오류 - 작동은 되는데, 결과적으로 문제가 있어 고쳐야함
# : 우리는 함수 이름에 걸맞는 동작만 잘 되도록 만들어야한다

# 간단한 인사메세지 보여주기 함수를 만들기
# ":"으로  끝나는 줄의 뜻은 "아다음 줄부터 들어쓴 내용은 한 묶음"
def say_hello():
    print("안녕하세요")

# 위에서 만든 함수는 이렇게 호출해야만 실행됩니다
say_hello()

# 함수 안에서 벌어지는 일들은 만륻기
def show_number():
    my_number = 44
    print(f"my_number: {my_number}")

# 위 함수를 실행
show_number() # 44

# 여기서도 my_number 값을 정해보기
# 아랫줄의 my_number는 show_number함수 안의 my_number와 다른 존재
my_number = 24
show_number()

# 그래서 함수안의 my_number 데이터가 영향을 끼치는 범위를
# 전문용어로 스코프(scope)라고 부른다

# 함수는 호출되기 전에 만들어져야 한다
# show_title() # NameError 발생

def show_title():
    print("함수 배우기")

show_title() # 정상 실행

# 실습 1: 답안
def start_checking():
    print("점검을 시작합니다")

start_checking()

# 함수가 호출되면 그 안의 
# def show_counter():
#     print(count)

# show_counter()

# 각 함수의 이름은 이름에 걸맞는 역활만 해줘야 한다

def show_students():
    print("학생1: 짱구")
    print("학생2: 철수")
    print("학생3: 훈이")

def show_teacher():
    print("선생님: 채송화")

def show_classrom():
    show_teacher()
    show_students()

show_classrom()

# ===============================================================

# [상식] 사이드이펙트
# 특정 부분의 코드가 문제 없지만
# 다른 부분과 예상치 못한 영향을 주고받는다면

# 코드 중복과 함수화

print("압축기A 온도 확인 중")
print("결과를 기록합니다")
print("펌프1 온도 확인 중")
print("결과를 기록합니다")

# 위와 같은 식의 코드를 여기저기 복사-붙여넣기 하면
# 언젠가 사람의 실수로 사고가 생길 수 있다

def start_check():
    print("점검을 시작합니다")
    print("안전 장비를 확인하세요")
    print("기록을 준비하세요")

start_check() # 압축기A
start_check() # 펌프1

# =========================================================
# 실습 3

# 함수의 호출 결과 예측
def say_hi():
    print("안녕하세요")

say_hi()
say_hi()

# ======================================================
# 실습 4 : 함수로 설비 점검 자동화하기
# 구분선과 점검안내 2줄이 설비마다 반복 출력
# ①구분선을출력하는함수를정의
# ②점검안내여러줄을출력하는함수를정의
# ③두함수를설비마다순서대로호출
# ④실행해각설비마다같은안내가반복되는지확인
# 예상결과 : 구분선과점검안내2줄이설비마다반복출력
def print_line():
    print("=" * 20)


def print_check():
    print("점검을 시작합니다")
    print("기록을 준비하세요")

# 장비1에 대한 함수 호출
print_line()
print_check()

# 장비2에 대한 함수 호출
print_line()
print_check()

# =================================================================
# 매개변수의 이해
# 인삿말 출력 함수 간단 버전
def say_hello():
    print("안녕하세요")

say_hello()

# 인삿말 출력에 함수를 친근 버전

def say_hello_choi():
    print("안녕하세요, Choi")

def say_hello_tuna():
    print("안녕하세요, Tuna")

say_hello_choi()
say_hello_tuna()

# 인사할 대상이 많아진다고 위 함수들을 더 만드느건 좀 아니지않나?
# 해결책은 하나의 함수에서 저 다양성을 다 대응해주는 것
# 그것이 바로 함수의 매개변수 활용

def say_hi(name):
    print(f"반갑습니다, {name}")


say_hi("Ned")
say_hi("Tuna")
say_hi("Layla")

# 예제코드 : 큭정 장비 이름을 알려주면 해당 장비의 체크를 시작 알림
def check(name):
    print(f"{name} 장비의 점검을 시작합니다")

check("압축기A")
check("펌프B")

# 매개변수가 2개 이상인 예제 - 덧셈
def clac_sum(number_a, number_b):

    total = number_a + number_b
    print(f"{number_a} + {number_b} = {total}")

clac_sum(1, 2)

# 매개변수가 2개 이상인 예제 - 장비 이름과 온도 정보 출력
def report(name, temp):
    # name = "압축기A"
    # temp = 75.3
    print(f"{name}의 온도는 {temp}도 입니다")

report("압축기A", 75.3)
report("펌프B", 85.2)

# 엉뚱한 호출
report(35.2, "보일러C")
# 첫번째 매개변수는 무조건 name이 되고,
# 두번째 매개변수는 무조건 temp가 되니까
# 원하지 않는 결과가 나올 수도 있다

# 매개변수가 부족하거나 더 있으면? -> TyprError 발생
# report("압축기A", 75.3, "가동중")
# report("펌프B")

# ==================================================
# 키워드 인자
def report_keywords(name, temp):
    print(f"{name}의 온도는 {temp}도입니다")

# 키워드 인자 없이 호출
report_keywords("펌프A", 37.4)
report_keywords(37.4, "펌프A")

# 키워드 인자 사용해 호출 : 순서 바꿔 호출해 생기는 문제 근본 차단
report_keywords(name = "펌프A", temp = 37.4)
report_keywords(temp = 37.4, name = "펌프A")

# =============================================================
# 반환값

def add(a, b):
    total = a + b
    return total

print(add(1, 2))
print(add(11, 224))
print(add(13, 20))

# 여러번 같은 결과 호출해야 한다면
# 차라리 변수에 담아서 쓰자
result = add(1, 2)
print(result + 1)
print(result + 2)
print(result + 3)

# ===========================================================

# 평균 내는 함수 만들기
def calc_average(a, b):
    return ( a + b ) / 2

avg = calc_average(75.3, 88.0)
print(f"평균 온도: {avg}")

# 여러 값을 한 번에 반환하기
# 다음의 함수는 배열을 받아서 그 안의 최소값을 동시ㅔㅇ return한다
def calc_min_max(values):
    minimum = min(values)
    maximum = max(values)
    print(minimum, maximum)

target_list = [1,2,3,4,5,6]
result = calc_min_max(target_list)
print(result) # 튜플인 것을 확인

# 반환값을 언패킹으로 받기
# 함수의 결과를 받는 순간에
# 결과 튜플의 내용을 풀어서
# 개별 변수에 담아 사용하기
result_min, result_max = calc_min_max(target_list)
print("최소값" + str(result_min))
print("최대값" + str(result_max))

# return 반환값이 없는 함수를 호출해놓고
# 결과를 어디에 담겠다고 하면,
# 담기는 값은 None이 된다

def say_greet():
    print("만나서 반갑습니다")
    return

greet = say_greet()
print(greet) # None

# 실습 5 (선택문제)
# 내장 함수 min(), max(), sum(), len() 활용

# =====================================================================
# 지금까지 배운 내용을 활용해서
# 재미있는 함수 만들기 예제

import random

groups = ["에스파", "하트2하트", '리센느', "태연", "엔믹스"]

# 랜덤 뽑기
my_group = random.choice(groups)
print(my_group)

def get_random_group():
  group_details = [
    {
        "이름": "에스파",
        "리더": "카리나"
    },
    {
        "이름": "엔믹스",
        "리더": "해원"
    },
    {
        "이름": "리센느",
        "리더": "원이"
    }
]
  
def get_random_groups():

    return my_group.get("이름"), my_group.get("리더")

group_name, group_leader = get_random_group()
print(f"{group_name}의 리더는 {group_leader}입니다")

# 여러분의 활동을 원합니다
# 어제처럼 주변 3~4인과 함께 코드를 만드세요
# 가봤거나, 가보고싶은 여행지 정보를 모아봅시다 (최소 5개 이상)
# 함수를 호출하여 랜덤으로 해당 여행지의 국가이름과 수도
# "환영합니다 000 나라의 수도 000입니다!" 출력

# ==============================================================
# 함수 설계와 활용

# 기본값 인자
# name과 value는 호출할 때 꼭 매개변수를 지정해줘야 하지만
# unit은 지정/언급 안해주면 "도(℃)" 기본값으로 정해진다

def report(name, value, unit = "도(℃)"):
    print(f"{name} : {value}{unit}")
  
report("압축기A", 75.3, "도(℃)")
report("압축기A", 75.3)
report("압축기A", 75.3, "도(℉)")

# 기본값을 덮어쓰기
# 결과가 boolean 타입을 return하는 함수
# 이름이 보통 "is"로 시작한다

def is_over_limit(value, limit):
    if value > limit:
        # 위험 맞음
        return True

    # 그 밖에는 위험 아님
    return False

print(f"위험한가요? {is_over_limit(95)}")
print(f"위험한가요? {is_over_limit(105)}")
# 어쩌다가 다른 기준이 필요할 때만
# 기준을 함께 전달해주면 된다
print(f"위험한가요? {is_over_limit(85, limit = 80)}")

# ========================================================
# 실습 1번
# 기본값이 있는 매개변수를 만들고, 생략하면 기본값.넣으면 덮어쓰기 확인
# ①def 괄호안매개변수에=로기본값을지정
# ②인자를생략하고호출해기본값이쓰이는지확인
# ③인자를넣어호출해기본값을덮어쓰는지확인
# ④필수매개변수는앞, 기본값매개변수는뒤순서규칙확

# 앞선 예제 코드들이 잘 돌아가는지 확인하는 것으로 대체합니다



# ===============================================================

# 02. 지역변수와 범위
# scope!!!
# 코드의 어디부터 어다까지 이 변수 데이터가 살아있을까?

# 바깥동네에 변수를 하나 만들어봅시다
outter = 100
def change_outter():
    # 아래 코드는 함수 내부에서 처음 언급되면서
    # 새롭게 만들어진 내부의 outter이고 (지역변수)
    # 함수가 종료되면 메모리에서 사라진다
    # 함수 바깥의 같은 이름의 존재에는 전혀 영향을 안준다
    outter = 50

change_outter()
print(outter) # 100

# ============================================================
# 실숩2
# 함수 안에서 만든 지역변수