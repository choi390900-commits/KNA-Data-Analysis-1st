# 단일 컬럼(col) 선택

import pandas as pd

df = pd.read_csv("data/13_diecasting_small.csv")
df.info()

# 데이터 프레임(2차원)에서 컬럼 한개를 도려내보면 시리즈(1차원)가 된다
s = df["형체력"]
s.info()


#  ==========================================================================

import pandas as pd

df = pd.read_csv("data/13_diecasting_small.csv")
df.info()

df["형체력"].info()
df[["형체력", "실린더입력"]].info

# ====================================================================

import pandas as pd

df = pd.read_csv('data/13_diecasting_small.csv')
df.info()

print("-" * 40)

s = df.loc[0]
s.info() # Series

# 행(row) 언급 서브 DF 만들기
df_sub = df.loc[0:2] # DataFrame
df_sub.info()
print(df_sub)

# 행(row)과 열(col) 언급 서브 DF 만들기
df_sub2 = df.loc[0:2, ['품질등급', '형체력']]
df_sub2.info()
print(df_sub2)