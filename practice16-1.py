# 실습1번

import pandas as pd

df = pd.read_csv('16_diecasting.csv') 
print("=== 데이터 앞부분 확인 ===")
print(df.head())


print("\n=== 데이터 크기(행, 열) ===")
print(df.shape) 

print("\n=== 컬럼 이름 확인 ===")
print(df.columns) 

print("\n=== 데이터 자료형 및 결측치 정보 ===")
df.info()

# 실습2번

min_pressure = df['실린더압력'].min()

max_pressure = df['실린더압력'].max()

range_pressure = max_pressure - min_pressure

print(f"실린더압력 최소 {min_pressure} · 최대 {max_pressure} · 범위 {range_pressure}")

# 실습3번

df_sorted = df.sort_values(by='사이클타임', ascending=False)

print("=== 사이클타임 내림차순 상위 10개 (동떨어진 값 확인) ===")
print(df_sorted['사이클타임'].head(10))

normal_data = df[(df['사이클타임'] >= 20) & (df['사이클타임'] <= 35)]
abnormal_data = df[(df['사이클타임'] < 20) | (df['사이클타임'] > 35)]

print("\n=== 정상 상태 데이터 개수 및 앞부분 ===")
print(f"개수: {len(normal_data)}개")
print(normal_data['사이클타임'].head())

print("\n=== 이상 상태 데이터 (설비 잼 후보 등) 개수 및 앞부분 ===")
print(f"개수: {len(abnormal_data)}개")
print(abnormal_data['사이클타임'].head())

# 실습4번

mean_all = df['사이클타임'].mean()
median_all = df['사이클타임'].median()

print(f"전체 평균 {mean_all:.2f} vs 중앙값 {median_all:.2f}")

normal_df = df[(df['사이클타임'] >= 20) & (df['사이클타임'] <= 35)]

mean_normal = normal_df['사이클타임'].mean()

print(f"정상만 평균 {mean_normal:.2f}")

# 실습5번

q1 = df['실린더압력'].quantile(0.25)

q2 = df['실린더압력'].quantile(0.5)
median_val = df['실린더압력'].median()

q3 = df['실린더압력'].quantile(0.75)

print(f"실린더압력 Q1 {q1} · Q2 {q2} · Q3 {q3}")
print(f"Q2({q2})와 중앙값({median_val})이 같은가? {q2 == median_val}")
