# 실습1번
# ① open으로 파일을 읽기 모드 r, utf-8로 열기
# ② read로 전체를 한 문자열로 읽어 출력
# ③ readlines로 줄 리스트로 읽어 출력
# ④ 두 방식의 결과 차이를 비교하고 파일을 close

f = open('sample.txt', 'r', encoding='utf-8')


print("=== read() 결과 ===")
read_data = f.read()
print(read_data)
print(f"데이터 타입: {type(read_data)}")

f.seek(0) 

print("\n=== readlines() 결과 ===")
readlines_data = f.readlines()
print(readlines_data)
print(f"데이터 타입: {type(readlines_data)}")

f.close()

# =====================================================
# 실습4번
# ① csv 모듈을 import
# ② with open으로 CSV를 읽기 모드 utf-8로 열기
# ③ csv.reader로 reader 객체를 만들기
# ④ for로 각 행(리스트)을 하나씩 꺼내 출력

import csv

with open('data/08_press.csv', 'r', encoding='utf-8') as f:
    
    reader = csv.reader(f)
    
    for row in reader:
        print(row)

# ==============================================================
# 실습5번
# ① csv를 import
# ② with open으로 w·utf-8·newline 옵션으로 열기
# ③ csv.writer로 writer 객체를 만들기
# ④ writerow로 헤더와 각 데이터 행을 쓰기

import csv

with open('result.csv', 'w', encoding='utf-8', newline='') as f:
    
    writer = csv.writer(f)
    
    writer.writerow(['시각', '설비'])
    writer.writerow(['09:00', 'PUMP-01'])

# ==============================================================
# 실습6번
# ① csv를 import
# ② csv.reader로 읽고 첫 줄 헤더는 건너뛰기
# ③ 값을 float로 변환해 기준(90) 초과 행만 리스트에 모으기
# ④ csv.writer로 모은 행들을 새 CSV에 저장

import csv

filtered_rows = []

with open('data/08_press.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    filtered_rows.append(header)

    for row in reader:
        val = float(row[2])
        if val > 90:
            filtered_rows.append(row)
with open("filtered_result.csv", "w", encoding="utf-8", newline="") as f:
    writer.writerows(filtered_rows)

# =============================================================================
# 실습2번
# ① with open으로 파일을 쓰기 모드 w, utf-8로 열기
# ② write로 내용을 쓰기(줄을 나눌 땐 줄바꿈 기호)
# ③ with 블록이 끝나면 파일이 자동으로 닫힘
# ④ r 모드로 다시 열어 쓴 내용을 확인

origin = input("온도: ")

print(f"입력한 온도는 {origin}")

temp = 0

try:
    temp = int(origin)
except:
   print("숫자 아니면 왜 저를 부르셨어요? 0으로 생각할게요")

next_temp = temp + 10
print(f"10도만 더 높으면 {next_temp}")

# ===============================================================================
# 실습2번
# ① with open으로 파일을 쓰기 모드 w, utf-8로 열기
# ② write로 내용을 쓰기(줄을 나눌 땐 줄바꿈 기호)
# ③ with 블록이 끝나면 파일이 자동으로 닫힘
# ④ r 모드로 다시 열어 쓴 내용을 확인

with open("practice.txt", "w", encoding="utf-8") as f:
    f.write("안녕하세요\n")
    f.write("python 파일 입출력\n")

with open("practice.txt", "r", encoding="utf-8") as f:
    content = f.read()

    print("=== 파일 내용 확인 ===")
    print(content)

# ======================================================================
# 실습3번
# ① with open으로 파일을 추가 모드 a로 열기
# ② write로 새 기록 문장을 쓰기
# ③ w 모드와 달리 기존 내용이 보존됨을 확인
# ④ r 모드로 열어 전체가 쌓였는지 확인

with open("practice.txt", "a", encoding="utf-8") as f:
    f.write("a 모드를 사용하여 새로운 줄을 추가\n")
    f.write("기존 내용이 지워지지 않고 보존\n")

with open("practice.txt", "r", encoding="utf-8") as f:
    content = f.read()

    print("=== 누적된 파일 내용 확인 ===")
    print(content)

# ====================================================================
# 실습4번
# ① csv 모듈을 import
# ② with open으로 CSV를 읽기 모드 utf-8로 열기
# ③ csv.reader로 reader 객체를 만들기
# ④ for로 각 행(리스트)을 하나씩 꺼내 출력

import csv

with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)

# =====================================================================
# 실습5번
# ① csv를 import
# ② with open으로 w·utf-8·newline 옵션으로 열기
# ③ csv.writer로 writer 객체를 만들기
# ④ writerow로 헤더와 각 데이터 행을 쓰기

import csv

with open("output.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["이름", "나이", "직업"])
    writer.writerow(["철수", 25, "개발자"])
    writer.writerow(["영희", 30, "디자이너"])

# ========================================================================