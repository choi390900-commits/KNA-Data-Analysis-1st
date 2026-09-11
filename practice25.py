# 실습 1번

import pandas as pd

df = pd.read_csv("data/mimii_features.csv")

print("데이터 크기 (행, 열):", df.shape)

print("정답 분포:\n", df["label"].value_counts())

# =========================================================
# 실습 2번

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.histplot(
    data=df, 
    x='rms', 
    hue='label', 
    element='step', 
    common_norm=False, 
    palette='Set2'
)

plt.title('RMS Feature Distribution by Label (Normal vs Anomaly)')
plt.xlabel('RMS Value')
plt.ylabel('Count')

plt.show()

# =========================================================
# 실습 3번

import pandas as pd

normal_df = df[df['label'] == 0]

print("정상 데이터 개수:", len(normal_df))

features = ['rms', 'spectral_centroid', 'zero_crossing_rate']

for feat in features:
    mu = normal_df[feat].mean()
    sd = normal_df[feat].std()
    print(f"[{feat}] 평균: {mu:.4f}, 표준편차: {sd:.4f}")

# =========================================================
# 실습 4번

mu_rms = normal_df['rms'].mean()
sd_rms = normal_df['rms'].std()

df['z_rms'] = (df['rms'] - mu_rms) / sd_rms

top_farthest = df.reindex(df['z_rms'].abs().sort_values(ascending=False).index)

print(top_farthest[['rms', 'z_rms', 'label']].head())

# =========================================================
# 실습 5번

df['abs_z_rms'] = df['z_rms'].abs()

df['anomaly_3'] = df['abs_z_rms'] > 3
df['anomaly_2'] = df['abs_z_rms'] > 2

count_3 = df['anomaly_3'].sum()
count_2 = df['anomaly_2'].sum()

print(f"임계값 3 이상 탐지 개수: {count_3}건")
print(f"임계값 2 이상 탐지 개수: {count_2}건")

# =========================================================
# 실습 6번

features = ['rms', 'spectral_centroid', 'zero_crossing_rate']

for feat in features:
    mu = normal_df[feat].mean()
    sd = normal_df[feat].std()
    df[f'z_{feat}'] = (df[feat] - mu) / sd

df['anomaly_combined'] = (
    (df['z_rms'].abs() > 3) | 
    (df['z_spectral_centroid'].abs() > 3) | 
    (df['z_zero_crossing_rate'].abs() > 3)
)

count_rms_only = df['anomaly_3'].sum()
count_combined = df['anomaly_combined'].sum()

print(f"rms 단독 이상 탐지 개수: {count_rms_only}건")
print(f"세 특징 종합 이상 탐지 개수: {count_combined}건")
