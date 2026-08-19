# 실습4번

import pandas as pd

df = pd.read_csv("data/14_hydraulic.csv")

df.groupby("라인")["압력"].mean().round(3)

df.groupby("설비")["온도"].max().round(3)

df.groupby("교대").size().round(3)

# ===========================================================
# 실습5번

df.groupby('설비')['진동'].mean().round(3).sort_values(ascending=False)

# ==============================================================
# 실습6번

df.groupby(['라인', '교대'])['진동'].mean().round(3)

df.groupby(['라인', '교대']).size().round(3)

# ===================================================================