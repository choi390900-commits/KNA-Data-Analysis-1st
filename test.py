count = 1 # int
temp = 26.5 # float
name = "Choi" # str
me = True # bool

# print(count, temp, name, me)
print(count)
print(temp)
print(name)
print(me)

# ===================

print(type(count))
print(type(temp))
print(type(name))
print(type(me))

# =========================

print(type(100)) # <calss 'int'>
print(type(100.0)) # <class 'fioat'>
print(type("100")) # <class 'str'>

# ===========================

print(6 + 2) # 8
print("6" + "2") # 62
print("62" + "39") # 6239

# =================
print(3 > 2) # True
print(5 == 5) # True
print(type(3 > 2)) # <class 'bool'>

# =====================
count = 3
print(count, type(count))

count = 3.0
print(count, type(count))

count = "3"
print(count, type(count))

# ======================

device_temp = 26.5 # floar
check_count = 26 # int
device_anme = "수업S" # str
is_normal = True # bool

# ========================
# 연산자

a = 17
b = 5
print(a + b) # 22
print(a - b) # 12
print(a * b) # 85
print(a // b) # 3
print(a % b) # 2
print(a ** b) # 1419857

# =====================

x = 60
y = 70
z = 80
print((x + y + z) / 3)
side = 6
print(side ** 2)
print(3 * 4 * 5) 

user_input = int(input("사용자 입력값: "))

result = []

# 2. for문을 사용하여 1부터 입력받은 값까지 반복합니다.
for i in range(1, user_input + 1):
    # 3. if문과 나머지 연산자(%)를 사용하여 3의 배수인지 확인합니다.
    if i % 3 == 0:
        # 3의 배수인 경우, 문자열로 변환하여 리스트에 추가합니다.
        result.append(str(i))

# 4. 쉼표(,)로 리스트의 요소들을 연결하여 출력합니다.
print(f"출력값: {', '.join(result)}")


# ============================================================
user_input = int(input("사용자 입력값: "))

print("출력값: ", end="")

# 1부터 입력값까지 반복
for i in range(1, user_input + 1):
    # 3의 배수인지 확인
    if i % 3 == 0:
        if i == 3:
            print(i, end="")         # 첫 번째 3의 배수는 쉼표 없이 출력
        else:
            print(f", {i}", end="")