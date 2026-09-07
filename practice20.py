#실습 1번

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/23_전기Panel.csv')

print(f"전체 데이터 크기: {df.shape}")
engine_list = df['unit_number'].unique()
print(f"엔진 목록: {engine_list}")
print(f"전체 엔진 대수: {len(engine_list)}대")

engine_2 = df[df['unit_number'] == 2].copy()
engine_2 = engine_2.sort_values(by='time_in_cycles')
print(f"2번 엔진 데이터 행 수: {len(engine_2)}행")

plt.figure(figsize=(10, 5))
plt.plot(engine_2['time_in_cycles'], engine_2['sensor_2'], marker='o', markersize=3, label='Sensor 2')

plt.title('2번 엔진 가동 회차별 센서 변화')
plt.xlabel('가동 회차 (Cycles)')
plt.ylabel('센서 측정값')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()

# ==================================================================
# 실습 2번

import matplotlib.pyplot as plt

unit2 = df[df['unit_number'] == 2].copy()
unit2 = unit2.sort_values(by='시퀀스')
unit2['컨베이어전류_MA10'] = unit2['컨베이어전류'].rolling(window=10).mean()

plt.figure(figsize=(10, 5))

plt.plot(unit2['시퀀스'], unit2['컨베이어전류'], 
         label='원본', color='gray', alpha=0.4)

plt.plot(unit2['시퀀스'], unit2['컨베이어전류_MA10'], 
         label='이동평균 (Window=10)', color='red', linewidth=2)

plt.title('설비 2 - 컨베이어전류 이동평균 추세 추적')
plt.xlabel('시퀀스')
plt.ylabel('컨베이어전류')
plt.legend()

plt.show()

# ==================================================================
# 실습 3번

import matplotlib.pyplot as plt

unit2['MA_5'] = unit2['컨베이어전류'].rolling(window=5).mean()
unit2['MA_10'] = unit2['컨베이어전류'].rolling(window=10).mean()
unit2['MA_30'] = unit2['컨베이어전류'].rolling(window=30).mean()

plt.figure(figsize=(12, 6))

plt.plot(unit2['시퀀스'], unit2['컨베이어전류'], 
         label='원본', color='gray', alpha=0.2)

plt.plot(unit2['시퀀스'], unit2['MA_5'], label='Window 5 (빠른 반응)', color='orange', linewidth=1.5)
plt.plot(unit2['시퀀스'], unit2['MA_10'], label='Window 10 (중간)', color='green', linewidth=2)
plt.plot(unit2['시퀀스'], unit2['MA_30'], label='Window 30 (매끄러움)', color='blue', linewidth=2.5)

plt.title('설비 2 - 창 크기에 따른 이동평균 비교')
plt.xlabel('시퀀스')
plt.ylabel('컨베이어전류')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()

# ==================================================================
# 실습 4번

import matplotlib.pyplot as plt

window_size = 10
unit2['MA_10'] = unit2['컨베이어전류'].rolling(window=window_size).mean()
unit2['STD_10'] = unit2['컨베이어전류'].rolling(window=window_size).std()

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 8), sharex=True)

axes[0].plot(unit2['시퀀스'], unit2['컨베이어전류'], label='원본', color='gray', alpha=0.4)
axes[0].plot(unit2['시퀀스'], unit2['MA_10'], label='이동평균 (추세)', color='blue', linewidth=2)
axes[0].set_title('설비 2 - 이동평균(추세) 및 이동표준편차(변동성) 동시 추적')
axes[0].set_ylabel('컨베이어전류')
axes[0].legend()
axes[0].grid(True, linestyle='--', alpha=0.5)

axes[1].plot(unit2['시퀀스'], unit2['STD_10'], label='이동표준편차 (변동성)', color='red', linewidth=2)
axes[1].set_xlabel('시퀀스')
axes[1].set_ylabel('표준편차 (변동폭)')
axes[1].legend()
axes[1].grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()

mid_point = len(unit2) // 2

early_volatility = unit2['STD_10'].iloc[:mid_point].mean()
late_volatility = unit2['STD_10'].iloc[mid_point:].mean()

print("=== 변동성(이동표준편차) 비교 ===")
print(f"초반 변동성 평균: {early_volatility:.2f}")
print(f"후반 변동성 평균: {late_volatility:.2f}")
print(f"-> 예상 결과 확인: 후반 변동성이 초반 대비 약 {late_volatility / early_volatility:.1f}배 수준으로 커짐을 알 수 있습니다.")

# ==================================================================
# 실습 5번

import matplotlib.pyplot as plt

unit2['변화량'] = unit2['컨베이어전류'].diff()
unit2['변화율'] = unit2['컨베이어전류'].pct_change()

print("=== 앞부분 데이터 확인 ===")
print(unit2[['시퀀스', '컨베이어전류', '변화량', '변화율']].head())
print("\n💡 첫 번째 값이 NaN(빈 값)인 이유:")
print("-> 변화량/변화율은 '직전 값'과 비교하여 계산되는데, 첫 번째 데이터는 이전 데이터가 존재하지 않기 때문입니다.")

window_size = 10
unit2['MA_10'] = unit2['컨베이어전류'].rolling(window=window_size).mean()
unit2['MA_10_변화량'] = unit2['MA_10'].diff()

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 8), sharex=True)

axes[0].plot(unit2['시퀀스'], unit2['변화량'], color='gray', alpha=0.7, label='원본 변화량')
axes[0].set_title('설비 2 - 원본 변화량 vs 이동평균(Window=10) 적용 후 변화량')
axes[0].set_ylabel('원본 변화량')
axes[0].legend()
axes[0].grid(True, linestyle='--', alpha=0.5)

axes[1].plot(unit2['시퀀스'], unit2['MA_10_변화량'], color='blue', linewidth=2, label='이동평균 후 변화량')
axes[1].set_xlabel('시퀀스')
axes[1].set_ylabel('MA_10 변화량')
axes[1].legend()
axes[1].grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()

# ==================================================================
# 실습 6번

import matplotlib.pyplot as plt

unit2['잔차'] = unit2['컨베이어전류'] - unit2['MA_10']

threshold = 2 * unit2['잔차'].std()
print(f"임계값: {threshold:.2f}")

unit2['변화점'] = unit2['잔차'].abs() > threshold
print(f"탐지된 변화점 개수: {unit2['변화점'].sum()}개")

plt.figure(figsize=(12, 6))
plt.plot(unit2['시퀀스'], unit2['컨베이어전류'], label='원본', color='gray', alpha=0.4)
plt.plot(unit2['시퀀스'], unit2['MA_10'], label='이동평균 (MA_10)', color='blue', linewidth=2)

change_x = unit2[unit2['변화점']]['시퀀스']
for idx, x_val in enumerate(change_x):
    if idx == 0:
        plt.axvline(x=x_val, color='red', linestyle='--', alpha=0.7, label='변화점 (임계값 초과)')
    else:
        plt.axvline(x=x_val, color='red', linestyle='--', alpha=0.7)

plt.title('설비 2 - 잔차 임계값 기반 변화점 탐지 및 구간 표시')
plt.xlabel('시퀀스')
plt.ylabel('컨베이어전류')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()