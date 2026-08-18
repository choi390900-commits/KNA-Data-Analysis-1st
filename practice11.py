# 실습1번

import pandas as pd

df = pd.read_csv('sensor_data.csv')

print("=== 데이터 앞 5행 (head) ===")
print(df.head())

print("\n=== 데이터 크기 (shape) ===")
print(df.shape)

print("\n=== 열 이름 목록 (columns) ===")
print(df.columns)

# ===============================================================
# 실습2번

series_col = df['형체력']
print("=== 단일 열 형태 확인 ===")
print(type(series_col))

df_cols = df[['형체력', '실린더압력']]
print("\n=== 복수 열 형태 확인 ===")
print(type(df_cols))

mean_value = series_col.mean()
print("\n=== 형체력 평균 ===")
print(mean_value)

# ==============================================================
# 실습3번

import pandas as pd

df = pd.read_csv('casting_log.csv')

series_col = df['형체력']
print("=== 단일 열(Series) 형태 확인 ===")
print(type(series_col))

df_cols = df[['형체력', '실린더압력', '주조압력']]

print("\n=== 여러 열(DataFrame) 크기 확인 ===")
print(df_cols.shape)

# =============================================================
# 실습4번

import pandas as pd

loc_row = df.loc[0]
print("=== loc 단일 행 선택 (라벨 0) ===")
print("품질등급:", loc_row['품질등급']) 

iloc_row = df.iloc[0]
print("\n=== iloc 단일 행 선택 (위치 0) ===")
print("품질등급:", iloc_row['품질등급'])

loc_range = df.loc[0:2]
iloc_range = df.iloc[0:2]

print("\n=== 범위 선택 줄 수 차이 확인 ===")
print(f"loc[0:2] 줄 수: {len(loc_range)}")   
print(f"iloc[0:2] 줄 수: {len(iloc_range)}")

# =========================================================