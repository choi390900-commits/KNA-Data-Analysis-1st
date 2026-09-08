# 실습 1번

import pandas as pd

df = pd.read_csv('data/25_mimii_features.csv')

y = df['target']

X = df[['feature1', 'feature2', 'feature3']]

print("X의 모양:", X.shape)
print("y의 모양:", y.shape)

print("X에 정답 열 포함 여부:", 'target' in X.columns)

# ===========================================================
# 실습 2번

import pandas as pd

y = df['고장_임박_여부']

X = df[['회차', '센서']]

print("X의 모양:", X.shape)  
print(y.value_counts())   

print("\n[점검] X에 정답 열 포함 여부:", '고장_임박_여부' in X.columns)
print("[점검] X에 RUL 열 포함 여부:", 'RUL' in X.columns)
