# input - 사용자 입력

print("출력")
print(5)
# 어쨌든 터미널에서 보이는 출력된 값은 "글자"와 같이 보임
# input을 사용해서 값을 받는 곳도 터미널
# input을 통해 사용자에게 값을 입력받는 경우는 무조건 "str 타입"

# python은 1번 줄부터 코드가 실행되다가 onput을 만나면
# 사용자가 입력할 때까지 실행을 멈춤
# 사용자가 값을 입력하고 enter를 누르면 이후 코드가 실행됨
# input()
# input의 괄호 안에 아무것도 작성하지 않은 경우 그냥 입력창이 보임
# 사용자는 뭘 입력해야하는지 모르는 상황이 됨
# 이를 해결하기 위해 "가이드 문구"를 출력해줘야 함
# 방법: input

print("이름: ") #

print("이름: ", "성별: ") #





# 시도 2. input() 두 번 작성
# input("성별: ")
# input("이름: ")
# 값을 여러 개 받아야 할 때응 input을 필요한 수 만큼 작성

# 시도 3. 가이드 문구에 규칙과 함께 입력받아야 하는 값들을 출력
input("이름, 나이를 입력해주세요. (ex. choi, 26): ")

# ================================
# input으로 받은 값은 변수에 저장하지 않으면 휘발됨
#

name = input("이름(변수 할당 ver): ")
age = input("나이(변수 할당 ver): ")
print("입력받은 이름은", name, "입니다")
print("입력받은 나이는", age, "세 입니다")

# input으로 받은 값은 무조건 str으로 저장됨
print(type(name))
print(type(age))
# 사용자가 숫자로 입력했어도
# 컴퓨터는 입력받은 값이
# 글자로 쓰고싶은건지 숫자로 쓰고싶은건지 알 수 없음
# ex. 사용자 입력값이 True일 때
# 우연히 True를 입력했는지
# 컴푸터는 알 수 없음
# 그래서 input으로 입력받은 값은 무조건 str으로 저장

# =========================

# 사용자에게 입력받은 값을 반 번에 출력하기
print("이름 ;",name, ",나이:", "님!")

# ========================
# int() - 문자열을 int(정수형)으로 변환
# int(변환하고자 하는 문자열)

age = int("26")
# 문자열 20을 매개변수로 받은 int 함수를 통해
# int(정수형)으로 자료형이 바뀜
# 그 다음에 age라는 
print("int로 변환한 age 변수의 자료형: ", type(age))

age = int(input("나이(형변환 ver): "))
# input을 통해 사용자 입력값으로 받은 문자열을 
# 매개변수로 받은 int 
#
#
print("사용자 입력값을 int로 변환한 age 변수의 자료형:")
print("당신은 곧", age + 1, "세가 됩니다.")

# 사용자 입력을 int로 변환하지 못하는 값을 입력항 경우
print(int("123"))
# print(int("010-1234-4567")) # Error
# -는 숫자가 아니기 때문에 int로  변환


minutes = 500
print(minutes // 60)
print(minutes % 60)

# ===================================
name = input("이름: ")
print("안녕하세요" + name + "님!")

# ==================================

birth_year = int(input("태어난 해: "))
age = 2026 - birth_year + 1
print("나이:" + str(age) + "세")

# =======================
#float() - 실수로 작성된 문자열을 float
print("======= 형변환 - float =====")

print(float(12.5))
print(float("12.5"))
print(float(12)) # int 12를 float 12.5으로 변환

# 사용자 입력값 float으로 변환
tall = float(input("키: "))
print


# print("당신의 현재 나이는" + str(2026 - year + 1) + "세 입니다")
#
#

# ==============================

a = input("진동값: ")
print("현재 입력받은 진동값은" + a)
# 값의 형태가  + 
#
#

# ==============================

# int, float, boo;은 str으로 변환 가능
b = str(123)
c = str(123.4)
d = str(True)
#e = str("str")
#f = str(False)
#f = str(false)

# =======================

name = input("성함: ")
city = input("도시 ")
print(name, city)

# =====================
a = int(input("수1: "))
b = int(input("수2: "))
print("합: ", a + b)
print("나눗셈:", a / b)

# ===========================

temp = int(input("온도: "))
print("80 초과", temp > 80,"0도 이상", temp >= 0)

# =======================
x = int(input("점수1: "))
y = int(input("점수2: "))
avg = (x + y) / 2
print("60 평균", avg >= 60)