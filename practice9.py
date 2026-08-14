# 실습1번

import pandas as pd

df = pd.read_csv("data/13_diecasting_small.csv")

condition = df["실린더압력"] >= 230

print("조건을 만족하는 참(True) 개수:", condition.sum())

filtered_df = df[condition]

print("추출된 행 개수:", len(filtered_df))

print(filtered_df)

# ====================================================================
# 실습2번

import pandas as pd

df = pd.read_csv("data/13_diecasting_small.csv")

condition = df["비스킷두께"] >= 16

filtered_df = df[condition]

result_df = filtered_df[["샷", "비스킷두께"]]

print("추출된 행 개수:", len(result_df))

print(result_df)

# ==================================================================
