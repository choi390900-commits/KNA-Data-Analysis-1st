# 실습 1번

import pandas as pd

df = pd.read_csv('data/23_cmapss_unit1_timestamp.csv')


print("변환 전 자료형:\n", df.dtypes)
df['시간'] = pd.to_datetime(df['시간'])
print("\n변환 후 자료형:\n", df.dtypes)


df = df.set_index('시간')

print("\n인덱스 설정 후 상위 3행:\n", df.head(3))

day_data = df.loc['2023-10-01']
print(f"\n하루 데이터 행 수: {len(day_data)}행")


three_days_data = df.loc['2023-10-01':'2023-10-03']
print(f"사흘 데이터 행 수: {len(three_days_data)}행")

# ==========================================================
# 실습 2번

import pandas as pd

daily_mean = df.resample('D').mean()
six_hour_mean = df.resample('6H').mean()


print(f"하루 평균 데이터 개수: {len(daily_mean)}개")      # 예상 결과: 8개
print(f"6시간 평균 데이터 개수: {len(six_hour_mean)}개") # 예상 결과: 32개

daily_rolling_mean = daily_mean.rolling(window=3).mean()

print("\n[하루 단위 평균]")
print(daily_mean.head())

print("\n[하루 단위 3일 이동평균 (추세선)]")
print(daily_rolling_mean.head())

# ==========================================================
# 실습 3번

import pandas as pd

sensor_cols = ['sensor1', 'sensor2', 'sensor3']

df_norm = (df[sensor_cols] - df[sensor_cols].min()) / (df[sensor_cols].max() - df[sensor_cols].min())

print("[정규화 후 최솟값]")
print(df_norm.min()) 

print("\n[정규화 후 최댓값]")
print(df_norm.max()) 

df_norm_rolling = df_norm.rolling(window=24).mean()

print("\n[정규화 및 이동평균 적용 후 데이터]")
print(df_norm_rolling.dropna().head())

# ==========================================================
# 실습 4번

import pandas as pd

sensor_cols = ['sensor_1', 'sensor_2', 'sensor_3', 'sensor_4', 'sensor_5', 'sensor_7']

df_norm = (df[sensor_cols] - df[sensor_cols].min()) / (df[sensor_cols].max() - df[sensor_cols].min())
df_ma = df_norm.rolling(window=24).mean().dropna() # 24단위 이동평균 적용 후 결측치 제거

chunk_size = len(df_ma) // 5 

early_mean = df_ma.iloc[:chunk_size].mean()  
late_mean = df_ma.iloc[-chunk_size:].mean()  

diff = late_mean - early_mean

diff_sorted = diff.sort_values(key=abs, ascending=False)

print("[센서별 초반 대비 후반 변화 폭 (정렬)]")
print(diff_sorted)