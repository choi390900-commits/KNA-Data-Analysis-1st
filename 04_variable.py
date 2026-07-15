# 변수 선언 방법
# 변수 이름 = 값
#오른쪽 값릏 왼쪽 이름에 "저장"하라는 코드
temp = 36 # 숫자로 저장하고 싶다면 따옴표 금지
name = "센서 A]"

print(temp) #36
print("temp")

# =은 
#

# ======================
print("======변수 사용 활용")

x = 5
# 변수를 "재할당"할 때 변수 기존 자신의 값을 활용 할 수 있음
# 변수에 할당할 떄 
x = x + 5 



# ======================
print("==========재활당========")

print("재할당하기 전 temp:", temp)
temp = 15 #
Temp = 150 #
print("temp:", temp,)
print("Temp:", Temp)

# 재할당은 지금까지 실행된 코드 중 가장 마지막으로 저장된 값이 불러옴
# print(score) # NameError 발생
score = 10
print(score) #10
score = 20
score = 30
print(score) #30

# ===========================
print("=======값 복사======")

a = 10
b = a # b변수에는 10이 저장 (저장할 떄의 그 순간의 a 값을 b에 복사)
a = 100 # a 변수를 재할당해도
print(b) # 10 b 변수의 값은 10이 그대로 유지됨

# ============================
print("============ 여러 변수 한 번에 선언 및 할당 =====")

width, heigth = 10, 20 #
print("width:", width, "heigth:", heigth)

x, y, z = 10, 20, 30 # 변수 3개, 값 2개 > ValueError 발생

# ===============================
print("========= 주석으로 변수 설명 =========")
temp = 25 # 온도(섭씨)
count = 3 # 센서 갯수
# temp = 100000000 # 주석처리된 코드은 동작하지 않는다
print(temp) #25

 # 변수 만들고 출력하기
temp = 25
print(temp) #25
name = "센서A"
print(name) #센서A

# 앞 코드 수정하기
temp = 30
print(temp) #30
temperature = 25
print(temperature) # 25

# 직접 변수 만들어 출력하기
my_number = 10
print(my_number) # 10
mood = "퇴근"
print(mood) # 퇴근

# 나이, 점수, 개수 변수로 표현
age = 26
label = "나이"
print(label) # 나이
print(age) # 26

# 변수 값 바꿔가며 추적하기
x = 10
print(x) # 10
x = x +5
print(x) # 15
x = x * 2
print(x) # 30

# 두 변수 값 옮기고 바꾸기
a = 100
b = a
a = 999
print(a) # 999
print(b) # 100

# 일부러 오류 내고 고치기
print(temp)
# print(Score) # 오류발생
temp = 25
print(temp)
score = 90
print(score)

# 주석으로 변수 설명 달기
temp = 25 # 온도(섭씨)
count = 3 # 센서 개수
# temp = 100 # 실행 안 함
print(temp) #25

# 값 예측 미니 퀴즈
x = 5
x = 10
x = x + 1
print(x) # 11

# 정보 카드 만들기 (종합)
name = "구미"
temp = 25
print("경북")
print(name)
print(temp)

# 변수 이름 다듬기
# a = 25, b = 3
device_temp = 25
sensor_count = 3
print(device_temp)
print(sensor_count)

# x, y, z = 1, 2, 3
width, height = 4, 3
print(width) # 4
print(height) # 3




# 변수 한 줄 만들기 도전