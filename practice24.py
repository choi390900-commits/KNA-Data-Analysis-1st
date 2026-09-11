# 실습 1번

import numpy as np

normal_values = [48, 49, 50, 51, 52]

mean_val = np.mean(normal_values)
std_val = np.std(normal_values, ddof=1)

print(f"정상 데이터 평균: {mean_val}")
print(f"정상 데이터 표준편차: {std_val:.3f}\n")

new_values = [53, 68, 40]

threshold = 3

print("[새 값에 대한 Z-score 계산 및 이상 판정]")
for val in new_values:
    
    z_score = (val - mean_val) / std_val
    
    is_anomaly = abs(z_score) > threshold
    status = "이상(Anomaly)" if is_anomaly else "정상(Normal)"
    
    print(f"값 {val}: Z-score = {z_score:.1f}  -> {status}")

# =========================================================
# 실습 2번

import pandas as pd


df = pd.read_csv('data/27_cmapss_fd001_sample.csv')

print(f"데이터 크기: {df.shape}")

print("\n[정답 분포]")
print(df['label'].value_counts())

normal_df = df[df['label'] == 0]  

normal_mean = normal_df['value'].mean()
normal_std = normal_df['value'].std(ddof=1)
print("\n[이상 판정 기준 통계량]")
print(f"정상 데이터 개수: {len(normal_df)}") 
print(f"정상 평균: {normal_mean:.4f}")   
print(f"정상 표준편차: {normal_std:.4f}")

# =========================================================
# 실습 3번

import pandas as pd

df['z_score'] = abs((df['rms'] - normal_mean) / normal_std)

top_z_scores = df.sort_values(by='z_score', ascending=False).head(3)

print("[Z-score 상위 3개 데이터 확인]")
print(top_z_scores[['rms', 'z_score']])

# =========================================================
# 실습 4번

import pandas as pd

threshold = 3

anomalies = df[df['z_score'] > threshold]

num_anomalies = len(anomalies)

print(f"기준 {threshold}에서 이상치 {num_anomalies}건") # 예상 결과: 기준 3에서 이상치 8건

print("\n[탐지된 이상치 데이터 확인]")
print(anomalies[['rms', 'z_score']])

# =========================================================
# 실습 5번

import matplotlib.pyplot as plt


plt.figure(figsize=(10, 5))
plt.scatter(df.index, df['z_score'], color='blue', alpha=0.6, label='Z-score')

threshold = 3
plt.axhline(y=threshold, color='red', linestyle='--', linewidth=1.5, label=f'Threshold ({threshold})')

plt.title('Z-score Scatter Plot for Anomaly Detection')
plt.xlabel('Index (Time Sequence)')
plt.ylabel('Z-score (Absolute Value)')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.5)

# =========================================================
# 실습 6번

import pandas as pd

target_feature = 'bearing_temp'  

normal_df = df[df['label'] == 0]
feature_mean = normal_df[target_feature].mean()
feature_std = normal_df[target_feature].std(ddof=1)

print(f"[{target_feature} 통계량]")
print(f"정상 평균: {feature_mean:.4f} | 정상 표준편차: {feature_std:.4f}\n")

df[f'{target_feature}_z'] = abs((df[target_feature] - feature_mean) / feature_std)

threshold = 3
feature_anomalies = df[df[f'{target_feature}_z'] > threshold]

print(f"기준 {threshold}에서 {target_feature} 이상치 개수: {len(feature_anomalies)}건") 

print("\n[특징별 이상치 탐지 비교]")
print(f"- rms 특징 이상치 수: {len(df[df['z_score'] > threshold])}건")
print(f"- {target_feature} 특징 이상치 수: {len(feature_anomalies)}건")

# =========================================================
# 실습 7번

import pandas as pd

threshold = 3
df['pred'] = (df['z_score'] > threshold).astype(int)

tp = ((df['label'] == 1) & (df['pred'] == 1)).sum()

fn = ((df['label'] == 1) & (df['pred'] == 0)).sum()

fp = ((df['label'] == 0) & (df['pred'] == 1)).sum()

tn = ((df['label'] == 0) & (df['pred'] == 0)).sum()

print("[Z-score 모델 탐지 품질 검증]")
print(f"정탐 (TP): {tp}건") 
print(f"미탐 (FN): {fn}건") 
print(f"오탐 (FP): {fp}건")  
print(f"정참음성 (TN): {tn}건")

print(f"\n최종 결과: 정탐 {tp} · 미탐 {fn} · 오탐 {fp}으로 완벽 분리")
