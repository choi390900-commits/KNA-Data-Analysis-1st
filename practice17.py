# 실습1번

import pandas as pd

df = pd.read_csv("data/14_hydraulic.csv")

print("=== 진짜 결측치(NaN) 개수 ===")
true_missing = df.isna().sum()
print(true_missing)

print("\n=== 위장 결측치 개수 ===")

fake_pressure = (df['압력'] == 0).sum()

fake_vibration = (df['진동'] == -999).sum()

print(f"압력 0 (위장 결측): {fake_pressure}개")
print(f"진동 -999 (위장 결측): {fake_vibration}개")

# ==================================================================
# 실습2번

import pandas as pd

df = pd.read_csv("secom_교육샘플.csv")

print("=== 데이터 크기(shape) 확인 ===")
print(df.shape)  

print("\n=== 데이터 미리보기(head) ===")

print(df.head())  

print("\n=== 데이터 정보(info) 확인 ===")
df.info()

print("\n=== 기초 통계량(describe) 확인 ===")

print(df.describe()) 

# ===================================================================
# 실습3번

import pandas as pd

df_raw = pd.read_csv("secom_교육샘플.csv")

before_nan_count = df_raw.isna().sum().sum()
print(f"=== 변환 전 전체 NaN 개수: {before_nan_count}개 ===")

fake_vibration = df_raw[df_raw['진동'] == -999]
fake_temp = df_raw[df_raw['온도'] == 999]

print("\n[위장 결측치(진동 -999) 포함 행]")
print(fake_vibration)

print("\n[위장 결측치(온도 999) 포함 행]")
print(fake_temp)

df_clean = pd.read_csv("secom_교육샘플.csv", na_values=[-999, 999])

after_nan_count = df_clean.isna().sum().sum()

print("\n=== 변환 전후 결측 개수 비교 ===")
print(f"변환 전 NaN 개수: {before_nan_count}개")
print(f"변환 후 NaN 개수: {after_nan_count}개 (진동 -999, 온도 999 포함)")

# ========================================================================
# 실습4번

import pandas as pd

df = pd.read_csv("secom_교육샘플.csv", na_values=[-999, 999])

missing_count = df.isna().sum()

total_rows = len(df)  # 또는 df.shape[0]
missing_ratio = (missing_count / total_rows) * 100

summary_df = pd.DataFrame({
    '결측_개수': missing_count,
    '결측_비율(%)': missing_ratio.round(1)
})

missing_only = summary_df[summary_df['결측_개수'] > 0]

print("=== 결측이 있는 컬럼 요약 ===")
print(missing_only)
print(f"\n결측이 존재하는 총 컬럼 수: {len(missing_only)}개")