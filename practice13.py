# 실습1번

from readline import redisplay

import pandas as pd

df = pd.read_csv("data/13_diecasting_shot.csv")
print(df.head())

print("=== 데이터 앞부분 확인 ===")
redisplay(df.head())

print("\n=== 데이터 구조 확인 ===")
df.info()

print("\n=== 설비별 빈도표 ===")
equipment_counts = df['설비'].value_counts()
print(equipment_counts)

print("\n=== 교대별 빈도표 ===")
shift_counts = df['교대'].value_counts()
print(shift_counts)

# =============================================
# 실습2번

import pandas as pd

print("=== 판정별 빈도 (개수) ===")
print(df['판정'].value_counts())

print("\n=== 판정별 비율 ===")
print(df['판정'].value_counts(normalize=True))

print("\n=== 소수점 셋째 자리 정리 비율 ===")
ratio = df['판정'].value_counts(normalize=True).round(3)
print(ratio)

# =================================================================
# 실습3번

import pandas as pd


vib_min = df['진동'].min()
vib_max = df['진동'].max()
print(f"진동 최솟값: {vib_min}, 최댓값: {vib_max}")

vib_band = pd.cut(
    df['진동'], 
    bins=[0, 30, 60, 100], 
    labels=['약함', '보통', '강함']
)

vib_counts = vib_band.value_counts()
print("\n=== 진동 구간별 빈도 ===")
print(vib_counts)