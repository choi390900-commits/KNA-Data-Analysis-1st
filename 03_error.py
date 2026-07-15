print("=============NameError 만들기=======")

#print(NameError만들기) # NameError 발생 (띄어쓰기가 있어서 변수 2개를 쉼표 없이 작성)
#print(NameError 만들기) # SyntaxError 발생
# 코드는 위에서 아래로 실행되기 때문에 위에서 에러 발생하면 그 이후 코드 실행 X
print("NameError 만들기") #따옴표로 감싸주면 에러 발생 X

# ========================
print("===========SyntaxError 만들기==========")

print("온도") # 따옴표를 안달음
print("진동") # 괄호를 안닫음

print("온도")
print("진동")

# 오류 고치기
print("온도", 75) # 따옴표를 안달아서
print("진동", 2.3) # 괄호를 안닫음
print("압력:", 4.0) # ,를 안달음

print("====", "1번", "설비", "점검")
print("온도(℃):", 82)
print("온도 상승량:", 11)
print("온도 변화량:", 93 - 82)

# if
# for
# def

# if_true

temp = 10
print(temp) #10

a = 10 # a는 10
b = a # a(10)를 복사