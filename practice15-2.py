# 실습1번

import pandas as pd

df = pd.read_csv("15_01_사출성형_공정.csv")

print(f"원본 크기: {df.shape}") 

df_row_drop = df.dropna()
print(f"행 삭제 후 크기: {df_row_drop.shape}") 

df_col_drop = df.dropna(axis=1)
print(f"열 삭제 후 크기: {df_col_drop.shape}") 

# 실습2번

import pandas as pd


df = pd.read_csv("15_01_사출성형_공정.csv")

df_how_all = df.dropna(how='all')
print(f"완전히 빈 행만 삭제 후 크기: {df_how_all.shape}") 

df_thresh = df.dropna(thresh=20)
print(f"임계값 20 적용 후 크기: {df_thresh.shape}") 

df_subset = df.dropna(subset=['불량여부'])
print(f"특정 컬럼 기준 삭제 후 크기: {df_subset.shape}")

# 실습3번

import pandas as pd

df = pd.read_csv("15_01_사출성형_공정.csv")

missing_ratio = df.isna().mean()

drop_cols = missing_ratio[missing_ratio > 0.4].index
print(f"제거 대상 컬럼: {list(drop_cols)}") 

df_dropped = df.drop(columns=drop_cols)
print(f"결측 비율 기준 컬럼 제거 후 크기: {df_dropped.shape}")

# 실습4번

import pandas as pd

df = pd.read_csv("15_01_사출성형_공정.csv")

original_rows = len(df)
dropna_rows = len(df.dropna())
thresh_rows = len(df.dropna(thresh=20))

comparison_df = pd.DataFrame({
    "삭제 방식": ["원본", "기본 행 삭제 (dropna)", "임계값 적용 (thresh=20)"],
    "남는 행 수": [original_rows, dropna_rows, thresh_rows]
})

comparison_df["손실률(%)"] = ((original_rows - comparison_df["남는 행 수"]) / original_rows * 100).round(1)

print(comparison_df)

# 실습5번

import pandas as pd

df = pd.read_csv("15_01_사출성형_공정.csv")

mean_val = df['센서17'].mean()
median_val = df['센서17'].median()

print(f"센서17 평균: {mean_val:.2f}")  
print(f"센서17 중앙값: {median_val:.1f}")

df_mean = df.copy()
df_median = df.copy()

df_mean['센서17'] = df_mean['센서17'].fillna(mean_val)

df_median['센서17'] = df_median['센서17'].fillna(median_val)

print(f"평균 대체 후 남은 결측 개수: {df_mean['센서17'].isna().sum()}")
print(f"중앙값 대체 후 남은 결측 개수: {df_median['센서17'].isna().sum()}")

# 실습6번

import pandas as pd

df = pd.read_csv("15_01_사출성형_공정.csv")

top_facility = df['설비명'].mode()[0] 
df['설비명'] = df['설비명'].fillna(top_facility)

print(f"설비명 결측 대체 값(최빈값): {top_facility}") 

df = df.sort_values('측정시각')

df['온도'] = df['온도'].ffill().bfill()

print(f"설비명 남은 결측: {df['설비명'].isna().sum()}")
print(f"온도 남은 결측: {df['온도'].isna().sum()}")