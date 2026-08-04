# 실습 2번
# ① def 괄호 안에 매개변수 두 개를 쉼표로 정의
# ② 함수 안에서 두 매개변수를 함께 활용
# ③ 인자 두 개를 순서대로 전달해 호출
# ④ 인자 순서를 바꾸면 결과가 어떻게 달라지는지 확인

def sensor_data(name, value):

  print(f"{name} {value} 도")

sensor_data("모터",78)
sensor_data("펌프",92)

sensor_data(78, "모터")

# ============================================================

# 실습 3번
# ① 매개변수 두 개를 가진 함수를 정의
# ② 호출할 때 매개변수 이름을 지정해 값을 전달
# ③ 키워드로 전달하면 순서를 바꿔도 같은 결과인지 확인
# ④ 위치 인자와 키워드 인자를 섞을 때는 위치가 먼저임을 확인

def sensor_data(name, value):
  print(f"{name} {value}")

  print("==== 설비 데이터 확인 ====")
  sensor_data(name = "모터", value = 78)

  print("==== 데이터 순서 변경 ====")
  sensor_data(value = 78, name = "모터")

  print("==== 데이터 위치 인자 + 키워드 인자 혼합")
  sensor_data("펌프", value = 92)

# =================================================================
# 실습 4번
# ① 값을 받아 계산하는 함수를 정의
# ② 계산 결과를 print가 아니라 return으로 돌려주기
# ③ 호출 결과를 변수에 담기
# ④ 담은 값을 다음 계산·출력에 이어 쓰기

def calculate_avg(va11, va12):
  result = (va11 + va12) / 2
  return result

sensor_avg = calculate_avg(80, 90)
print(sensor_avg)

new_avg = sensor_avg + 5.0
print(f"{new_avg}")
