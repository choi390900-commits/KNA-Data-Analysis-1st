# 실습5번

import pandas as pd

df = pd.read_csv("data/13_diecasting_shot.csv", encoding="utf-8")
print(df.shape)
df.info()
print(df.head(3))

print(df.sort_values("비스킷두께", ascending=False).head(5))

print("===========================")

df_multi = df.sort_values(["품질등급", "형체력"], ascending=[True, False])
print(df_multi.head(5))

# =======================================================================
# 실습6번

import pandas as pd

df = pd.read_csv("data/13_diecasting_shot.csv", encoding="utf-8")
df.info()
print(df.tail(5))

df_bad = df[ df["품질등급"] == "불량" ]
print(len(df_bad)) # 20
print(df_bad.head())

df_filtered = df[ df["품질등급"] == "불량" ].sort_values("비스킷두께", ascending=False).head(5)
print(df_filtered)
