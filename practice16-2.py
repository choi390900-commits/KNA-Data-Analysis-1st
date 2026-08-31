# 실습1번

import pandas as pd

df = pd.read_csv('16_welding.csv')

Q1 = df['cycle_time'].quantile(0.25)
Q3 = df['cycle_time'].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

print(f"사이클타임 IQR: {IQR:.2f}")
print(f"하한: {lower:.1f}")
print(f"상한: {upper:.1f}")

# 실습2번

mask = (df['cycle_time'] < lower) | (df['cycle_time'] > upper)

outliers = df[mask]

outlier_count = mask.sum()
outlier_ratio = mask.mean() * 100

print(f"사이클타임 이상치 {outlier_count}건, 비율 {outlier_ratio:.1f}%")

# 실습4번

df_clean = df[~mask]

original_rows = len(df)
clean_rows = len(df_clean)

clean_mean = df_clean['cycle_time'].mean()

print(f"{original_rows}행 → {clean_rows}행, 제거 후 사이클타임 평균 {clean_mean:.2f}")

# 실습5번

df['cycle_time_clipped'] = df['cycle_time'].clip(lower=lower, upper=upper)

clipped_min = df['cycle_time_clipped'].min()
clipped_max = df['cycle_time_clipped'].max()
clipped_mean = df['cycle_time_clipped'].mean()

print(f"보정 후 최소 {clipped_min:.1f}·최대 {clipped_max:.1f}, 평균 {clipped_mean:.1f}")

# 실습6번

Q1 = df['cylinder_pressure'].quantile(0.25)
Q3 = df['cylinder_pressure'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

mask = (df['cylinder_pressure'] < lower) | (df['cylinder_pressure'] > upper)

mean_original = df['cylinder_pressure'].mean()

mean_removed = df[~mask]['cylinder_pressure'].mean()

mean_clipped = df['cylinder_pressure'].clip(lower=lower, upper=upper).mean()

median_val = df['cylinder_pressure'].median()
mean_imputed = df['cylinder_pressure'].mask(mask).fillna(median_val).mean()

print(f"전 {mean_original:.2f} → 제거 {mean_removed:.2f}·보정 {mean_clipped:.2f}·채움 {mean_imputed:.2f}")

# 실습7번

duplicate_count = df.duplicated().sum()

duplicates = df[df.duplicated()]

all_duplicates_count = df.duplicated(keep=False).sum()
all_duplicates = df[df.duplicated(keep=False)]

print(f"완전 중복 {duplicate_count}건, keep을 끄면 겹친 행 {all_duplicates_count}건 표시")

# 실습8번

df_unique = df.drop_duplicates()

original_rows = len(df)
unique_rows = len(df_unique)
remaining_duplicates = df_unique.duplicated().sum()

print(f"{original_rows}행 → {unique_rows}행, 남은 중복 {remaining_duplicates}")

df_subset = df.drop_duplicates(subset=['기준_컬럼명'])
subset_rows = len(df_subset)

print(f"subset 기준도 {subset_rows}행")