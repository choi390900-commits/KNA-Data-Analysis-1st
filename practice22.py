# 실습 1번

import pandas as pd

df = pd.read_csv('data/25_mimii_features.csv')

normal_df = df[df['label'] == '정상']

normal_count = len(normal_df)
normal_mean = normal_df['rms'].mean()
normal_std = normal_df['rms'].std()

print(f"정상 데이터 개수: {normal_count}개")
print(f"평균(중심): 약 {normal_mean:.4f}")
print(f"표준편차(산포): 약 {normal_std:.4f}")

# =========================================================
# 실습 2번

import pandas as pd

df = pd.read_csv('data/25_mimii_features.csv')
normal_df = df[df['label'] == '정상']

normal_mean = normal_df['rms'].mean()
normal_std = normal_df['rms'].std()

lower_bound = normal_mean - (3 * normal_std)
upper_bound = normal_mean + (3 * normal_std)

print(f"정상 범위: 약 {lower_bound:.3f} ~ {upper_bound:.3f}")

anomaly_candidates = df[(df['rms'] < lower_bound) | (df['rms'] > upper_bound)]

print(f"이상 후보 개수: {len(anomaly_candidates)}개")

# =========================================================
# 실습 3번

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.family'] = 'Malgun Gothic' 
plt.rcParams['axes.unicode_minus'] = False


df = pd.read_csv('data/25_mimii_features.csv')

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.histplot(data=df, x='rms', hue='label', bins=30, kde=True, ax=axes[0])
axes[0].set_title('RMS 히스토그램 (분포와 꼬리 관찰)')

sns.boxplot(data=df, x='label', y='rms', ax=axes[1])
axes[1].set_title('RMS 박스플롯 (상자 밖 튀는 점 확인)')

plt.tight_layout()
plt.show()

# =========================================================
# 실습 4번

import pandas as pd

df = pd.read_csv('data/25_mimii_features.csv')

features = ['feature1', 'feature2', 'feature3'] 

mean_comparison = df.groupby('label')[features].mean().T

mean_comparison['차이'] = abs(mean_comparison['이상'] - mean_comparison['정상'])

mean_comparison = mean_comparison.sort_values(by='차이', ascending=False)
print("=== 센서별 정상/이상 평균 비교 ===")
print(mean_comparison)
