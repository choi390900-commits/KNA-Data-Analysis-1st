# 실습1번

import pandas as pd
import numpy as np

df = pd.read_csv("data/14_hydraulic.csv")

vibration_mean = df['진동'].mean()
vibration_var = df['진동'].var()
vibration_std = df['진동'].std()

print(f"전체 평균: {vibration_mean:.2f}")
print(f"전체 분산: {vibration_var:.2f}")
print(f"전체 표준편차: {vibration_std:.2f}")
print("-" * 30)

std_squared = vibration_std ** 2
print(f"표준편차의 제곱: {std_squared:.2f}")
print(f"분산과 같은가?: {np.isclose(vibration_var, std_squared)}")
print("-" * 30)

line_stats = df.groupby('라인')['진동'].agg(['mean', 'std']).round(2)
print("■ 라인별 진동 평균과 표준편차")
print(line_stats)

# ================================================================
# 실습2번
import pandas as pd

target_cols = ['온도', '진동', '압력']

qc_stats = df.groupby('판정')[target_cols].agg(['mean', 'std']).round(2)

print("■ 합격·불합격 그룹별 지표 평균과 표준편차")
print(qc_stats)

# =====================================================================
# 실습3번

import pandas as pd

list_agg = df.groupby('교대')['진동'].agg(['mean', 'std', 'max']).round(2)

print("■ 1. 리스트 방식 결과 표 (교대별 진동 통계)")
print(list_agg)
print("\n" + "="*50 + "\n")

named_agg = df.groupby('설비').agg(
    평균온도=('온도', 'mean'),
    평균진동=('진동', 'mean'),
    측정수=('온도', 'count')
).round(2)

print("■ 2. 이름 붙이기 방식 결과 표 (설비별 종합 요약)")
print(named_agg)

# ============================================================================
# 실습4번

import pandas as pd

diagnosis_table = df.groupby('설비').agg(
    측정수=('온도', 'count'),
    평균온도=('온도', 'mean'),
    온도편차=('온도', 'std'),
    평균진동=('진동', 'mean'),
    평균압력=('압력', 'mean')
).round(2)

diagnosis_sorted = diagnosis_table.sort_values(by='온도편차', ascending=False)

print("■ 설비별 진단표 (온도편차 내림차순)")
print(diagnosis_sorted)