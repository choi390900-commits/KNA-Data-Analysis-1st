# 실습5번

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

engine1 = pd.read_csv('21_cmapss_fd001_sample.csv')

plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(engine1['cycle'], engine1['s_3'], label='원본 데이터')
plt.axvline(x=187, color='red', linestyle='--', label='변화점')
plt.axvspan(180, 192, color='red', alpha=0.15, label='이상 의심 구간')
plt.title('센서 3 추세 및 의심 구간')
plt.legend()

plt.subplot(2, 1, 2)

plt.plot(engine1['cycle'], engine1['s_3'].rolling(window=20).std(), color='orange', label='이동표준편차')
plt.axvspan(180, 192, color='red', alpha=0.15)
plt.title('센서 3 변동성(이동표준편차)')
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
sensors = ['s_2', 's_3', 's_4', 's_7', 's_11']
corr = engine1[sensors].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('다중 센서 상관관계 Heatmap')
plt.show()