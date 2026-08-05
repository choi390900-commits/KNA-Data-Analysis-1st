# 실습1번
# ① import 모듈명으로 통째로 가져와 모듈명.기능() 으로 사용
# ② from 모듈 import 기능 으로 일부만 가져와 모듈명 없이 사용
# ③ import 모듈 as 별명 으로 별명.기능() 으로 사용
# ④ 세 방식의 출력이 같은지 확

from calendar import c
import math
result1 = math.sqrt(16)
print(f"1번 방식: {result1}")

from math import sqrt
result2 = sqrt(16)
print(f"2번 방식: {result2}")

import math as mt
result3 = mt.sqrt(16)
print(f"3번 방식: {result3}")

# ==========================================================================
# 실습2번
# ① random 모듈을 import
# ② randint로 무작위 센서값을 만들어 출력
# ③ math 모듈로 그 값을 가공(제곱근)
# ④ 다시 실행하면 값이 달라지는지 확인

import random
import math

sensor_value = random.randint(1, 100)
print(f"무작위 센서값: {sensor_value}")

processed_value = math.sqrt(sensor_value)
print(f"가공한 센서값(제곱근): {processed_value:.2f}")

# =========================================================================
# 실습4번
# ① os를 import
# ② path.join으로 폴더와 파일 이름을 이어 경로를 만들기
# ③ path.exists로 그 경로가 있는지 참·거짓 확인
# ④ if로 있으면·없으면 다른 메시지 출력

import os

folder_name = "data_folder"
file_name = "sensor_log.txt"

file_path = os.path.join(folder_name, file_name)
print(f"생성 파일 경로: {file_name}")

is_exist = os.path.exists(file_path)
print(f"경로 존재 여부: {is_exist}")

if is_exist:
  print("결과: 파일리 존재함 (True)")

else:
  print("결과: 파일이 존재하지 않음 (False)")

# ====================================================================
# 실습5번
# ① os와 datetime을 import
# ② listdir로 폴더 파일 수를 구하기
# ③ datetime.now로 현재 시각을 담기
# ④ f-string으로 파일 수와 시각을 한 문장으로 출력

import os
from datetime import datetime

folder_path = r"c: \Users\user\Desktop\data"

file_list = os.listdir(folder_path)
file_count = len(file_list)

current_time = datetime.now()

print(f"파일 {file_count}개, 점검 시각{current_time.strftime()}")