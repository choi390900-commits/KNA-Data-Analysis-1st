# 실습1번

import pandas as pd

df = pd.read_csv("data/13_diecasting_small.csv")

condition = df['실린더압력'] >= 230

true_count = condition.sum()
print(f"조건을 만족하는 참(True) 개수: {true_count}건")

filtered_df = df[condition]

print(f"추출된 데이터프레임 행 수: {len(filtered_df)}건")

filtered_df.head()

# ===================================================================
# 실습2번

condition = df['비스킷두께'] >= 16

filtered_df = df[condition]

result_df = filtered_df[['샷', '비스킷두께']]

print(f"비스킷두께 16 이상인 추출 건수: {len(result_df)}건")

result_df.head()

# ======================================================================
# 실습3번

cond_biscuit = (df['비스킷두께'] >= 16)
cond_cycle = (df['사이클타임'] >= 25)

df_and = df[cond_biscuit & cond_cycle]

df_or = df[cond_biscuit | cond_cycle]

print(f"그리고(&) 조건 만족 건수: {len(df_and)}건")
print(f"또는(|) 조건 만족 건수: {len(df_or)}건")

# ==========================================================================
