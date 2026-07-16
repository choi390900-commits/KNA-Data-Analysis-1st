# 산술연산자
# + - * / //(몫) %(나머지) **(거듭제곱)
print(3 + 5) # 8
print(10 - 5) # 5
print(4 * 5) # 20
print(20 / 5) # 4.0 (나눗셈 결과는 항상float)
print(7 // 3) # 2
# 7개의 음료수를 3봉투에 나눠 담으면, 2봉투와 1개의 음료수가 나옴
print(7 % 3) # 1 (나눗셈 결과의 나머지)
print(2 ** 5) #32 (2의 5제곱)

# ========================
# 연산 우선순위와 우선순위 지정
# **(거듭제곱) > *(곱하기) /(나누기) //(몫) %(나머지) > +(더하기) -(빼기)
print(2 + 8 * 3) # 8*3 연산 후 그 결과를 2와 더함
print((2 + 8) * 3) # 괄호 안의 연산을 먼저한 뒤 곱하기 계산

# =======================
# 복합연산자

result = 3 * 5
print(result) # 15

# +=: 기존 값에서 오른쪽 값을 더한 뒤 재할당
# -=: 기존 값에서 오른쪽 값을 뺸 뒤 재할당
# *=: 기존 값에서 오른쪽 값을 곱한 뒤 재할당
# /=: 기존 값에서 오른쪽 값을 나눈 뒤 재할당

result += 10
print(result)

# result -= 






# ===========
# 문자열 연산
print("안녕" + "하세요") # 안녕하세요

# 만약 "안녕"과 "하세요" 사이에 공백을 1개 넣고 싶다면
# 방법 1) , 사용

# 방법 2) 안녕 뒤에 공백 추가

# 방법 3) 공백만 있는 문자열 더하기

print("안녕", "하세요")
print("안녕" + "하세요")
print("안녕" + " " + "하세요")

# 문자열 곱하기
print("안녕" * 5) # 안녕안녕안녕안녕안녕

# 문자열에 연산자를 사용할 경우 모두 이어져서 나옴

# ===========================
print("====== 비교연산자 =====")

# <(미만), >(초과), <=(이하), >=(이상), ==(같다), !=(다르다)
# 비교 결과는 무조건 True or false (bool)

print(7 < 16) #True
print(7 > 16)
print(7 <= 7)
print(7 >= 7)
print(7 == 7)
print(7 != 7) # False

# 비교연산자는 문자열 비교도 가능

# 1. 대소문자 구분
print("hrllo" == "Hello") #False

# 2. 공백이 있어도 다르다고 판단
print("정상" =="정상 ") #False

# 부정연산자 != (not)
# 두 값이 동일한데 !로 인해서 값이 반대로 출력됨
print("hello" != "hello") # False
print("hello" != "hello ") # True
print("hello" != "Hello") # True

# 변수에 문자열을 할당하고, 변수로 문자열 비교

hi = "안녕"
hello = "hi" # paint(hello) > 안녕

print(hello == "hi")
# 위 비교에서 hello는 따옴표로 감싸지지 않아서 "변수"로 취급
# 만약 hello를 "hello"와 같이 따옴표로 감싸면
# string으로 인식해서 변수 취급을 하지 않음
# ex) "hello"와 "hi"를 비교하는 것

# 질문 1) hello 변수에 할당하는 값을 따옴표로 감싸지 않고 비교
# print("=== 질문 1) hello 변수에 할당하는 값을 따옴표로 감싸지 않고 비교 ===")
# hello = hi
# print(hello == hi)  # NameError(선언하지 않은 이름 호출했을 때)
# hi는 따옴표에 감싸져있지 않기 때문에 변수로 취급됨
# 그런데 우리는 hi 변수를 선언한 적이 없기 때문에 에러

# 질문 1) 해결방법
# print("=== 질문 1) 해결 방법 ===")
hi = "안녕"  # hello 변수에 hi 변수를 할당하기 전 hi 변수 선언
hello = hi  # print(hello) > 안녕
print("=== 변수 hello(안녕)와 변수 hi(안녕) 비교 ===")
print(hello == hi)  # True

#변수로 비교연산자 사용
num1 = 123
num2 = 456

print(num1 >= num2) # False
# print(num >= "num2") # TyoeError 발생

# =========================

# and / or / not - 논리연산자
# and: 둘 다 True여야 True를 반한
print(5 == 5 and 7 == 7) # True + True = True
# and는 첫 번째 조건이 False라면 뒤에 조건은 확인 안함
print(5 == 7 and 7 == 7) # False + True = False
print(5 == 5 and 7 != 7) # True + False = False
#위 코드는 가능하다면 7 != 7 and 5 == 5 순서로 작성

# or: 하나라도 True라면 True 반환
print(5 == 5 or 7 == 7) # True + True = True
print(5 == 7 or 7 == 7) # 첫 번째 조전이 False라면 뒤에 조건은 확인 안함
# or는 첫 번째 조건이 True라면 뒤에 조건은 확인 안함
print(5 == 5 or 7 != 7) # True + False = True

# not: 값을 반대로 뒤집음
print(not True) # False
print(not 5 == 5) # False
# 5 == 5를 연산하여 True를 반환
# not True로 동작해서 True를 뒤집어 False 반환
