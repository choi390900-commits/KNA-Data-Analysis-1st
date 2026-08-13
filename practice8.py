# 실습1번

import pandas as pd

df = pd.read_csv("data/13_diecasting_small.csv")

print(df.head())
print(df.shape)

print(df.columns)

# =================================================================
# 실습2번

import pandas as pd

df = pd.read_csv('data/13_diecasting_small.csv')

single_col = df['형체력']
print("=== 단일 열 (Series) ===")
print(single_col.head())
print("자료형:", type(single_col))

multi_cols = df[['형체력', '실린더압력']]
print("\n=== 복수 열 (DataFrame) ===")
print(multi_cols.head())
print("자료형:", type(multi_cols))

clamping_force_mean = df['형체력'].mean()
print("\n=== 형체력 평균 ===")
print(clamping_force_mean)

# ======================================================================
# 실습3번

import pandas as pd

df = pd.read_csv('data/13_diecasting.csv')

single_sensor = df['형체력']
print("=== 단일 센서 열 ===")
print("자료형:", type(single_sensor))

multi_features = df[['형체력', '실린더압력', '주조압력']]
print("\n=== 여러 feature 열 ===")
print("형태(shape):", multi_features.shape)

# =====================================================================
# 실습4번


# =================================================================

import pandas as pd

df = pd.read_csv('data/13_diecasting_small.csv')

loc_single = df.loc[0, '품질등급']
print("품질등급 값:", loc_single)

iloc_single = df.iloc[0]

loc_range = df.loc[0:2]
iloc_range = df.iloc[0:2]

print("loc 범위 줄 수:", len(loc_range))
print("iloc 범위 줄 수:", len(iloc_range))

# ===================================================================
