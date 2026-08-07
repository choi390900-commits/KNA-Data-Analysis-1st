# 실습 1번
# ① try 블록에서 파일을 열어 처리
# ② 처리 도중 오류가 날 수 있음을 가정
# ③ finally 블록에 close를 넣어 오류 여부와 상관없이 닫기
# ④ 일부러 오류를 내도 finally가 실행되는지 확인

try:
  print("1번 파일 열어줘")
  f = open("test.py", "w")

  print("데이터 처리 중 ...")
  raise Exception("의도적으로 발생시킨 오류")

  print("이 코드는 오류로 실행 불가")

except Exception as e:
  print(f"예외발생: {e}")

finally:
  print("finally 블록 실행: 오류발생과 상관없이 안전하게 닫힘")
  f.close()

# ===========================================================================
# 실습 2번
# ① 여러 측정값(일부는 숫자가 아님)을 반복
# ② try에서 float로 변환
# ③ 변환 실패(ValueError) 시 continue로 그 줄만 건너뛰기
# ④ 정상 값만 합계에 더해 출력
# - 소수점 이하의 숫자가 포함된 숫자들을 20개정도 만들어 문자로 배열에 담아주세요 "123.45"
# - 그 사이에 엉뚱한 글자들이 포함된 내용도 포함시켜 주세요. "영크크"
# - 위 리스트 데이터를 사용해서 문제를 풀어주세요

measurements = [
    "124", "457", "영크크", "890", "45", 
    "불량데이터", "679", "12", "75", "===", 
    "50", "90", "62.1", "N/A", "70", 
    "14", "56", "결측치", "92", "346", 
    "70", "에러발생", ".34", "5.18", "92", "36"
]

total_sum = 0.0
valid_count = 0

for item in measurements:
  try:
    value = float(item)
  except ValueError:
    print(f"변환실패 불량 데이터 건더뛰기: {item}")
    continue

  total_sum += value
  valid_count += 1

print("-" * 40)
print(f"처리된 정상 데이터 개수: {valid_count}개")
print(f"정상 값 총합: {total_sum:.2f}")

# ===============================================================================
# 실습 3번
# ① 여러 파일 이름을 반복
# ② try에서 파일을 열어 처리
# ③ 없는 파일(FileNotFoundError) 시 continue로 건너뛰기
# ④ 처리한 파일 수를 세어 출력
# - 다음과 같은 식의 리스트를 만들어 반복문으로 처리해봅시다
# - for문으로 리스트의 문자열을 꺼내어 해당 이름의 파일들을 열어보기 시도하면 됩니다

# file_names = ["08_press.csv", "09_ict.csv","09_ict_dirty.csv"]

file_names = ["08_press.csv", "09_ict.csv","09_ict_dirty.csv", "없는파일.csv"]

processed_count = 0
for file_name in file_names:
  try:
    with open(file_name, "r", encoding="utf-8") as f:
      print(f"[{file_name}] 파일을 성공적으로 열었습니다 데이터를 읽습니다...")

  except FileNotFoundError:
    print(f"에러: [{file_name}] 파일이 존재하지 않아 건너뜁니다")
    continue

  processed_count += 1

print("=" * 40)
print(f"처리를 완료한 총 파일 수: {processed_count}개")

# ===============================================================================
# 종합 실습
# 실습 1단계

import csv

def read_sensor_csv(file_path="data/09_ict_inspection_dirty.csv"):
    header = []
    rows = []
    
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            
            header = next(reader)
            
            for row in reader:
                rows.append(row)
                
        print(f"데이터 행 수: {len(rows)}")
        
    except FileNotFoundError:
        print("안내: 파일을 찾을 수 없습니다. 경로를 다시 확인해 주세요.")
        
    return header, rows

# ============================================================================
# 실습 2단계

def classify_by_equipment(rows):
    by_type = {}
    
    equipment_index = 0 
    
    for row in rows:
        
        if len(row) <= equipment_index:
            continue
            
        equip_name = row[equipment_index]
      
        if equip_name not in by_type:
            by_type[equip_name] = []
            
        by_type[equip_name].append(row)
        
    print("=== 설비별 데이터 개수 ===")
    for name, data_list in by_type.items():
        print(f"부품({name}): {len(data_list)}개")
        
    return by_type

# ===========================================================================
# 실습 3단계

def calculate_statistics(rows, target_index):
    valid_numbers = []
    
    for row in rows:
        if len(row) <= target_index:
            continue
            
        try:
            value = float(row[target_index])
            valid_numbers.append(value)
        except ValueError:
            
            continue
            
    if not valid_numbers:
        return None, None, None, None
        
    count = len(valid_numbers)
    avg = sum(valid_numbers) / count
    min_val = min(valid_numbers)
    max_val = max(valid_numbers)
    
    return count, avg, min_val, max_val

# =========================================================================
# 실습 4단계

def filter_dirty_temperature(rows, temp_index=2, min_temp=0.0, max_temp=100.0):
    valid_rows = []
    bad_logs = []

    for row_num, row in enumerate(rows, start=2):
        try:
            
            if len(row) <= temp_index:
                raise ValueError("데이터 열 누락")

            
            raw_val = row[temp_index]
            try:
                temp_val = float(raw_val)
            except ValueError:
                raise ValueError(f"숫자로 변환할 수 없는 값 ('{raw_val}')")

            if temp_val < min_temp or temp_val > max_temp:
                raise ValueError(f"정상 범위 초과 ({temp_val}℃)")

            valid_rows.append(row)

        except ValueError as e:
            
            bad_logs.append((row_num, str(e)))
            continue

    print(f"=== 불량 데이터 필터링 결과 ===")
    print(f"정상 데이터: {len(valid_rows)}행 / 불량 데이터: {len(bad_logs)}행")
    for line_num, reason in bad_logs:
        print(f"  └ [{line_num}번째 행] 사유: {reason}")

    return valid_rows, bad_logs

# ================================================================================
