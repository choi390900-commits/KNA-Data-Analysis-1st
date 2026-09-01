#실습

import pandas as pd

df = pd.read_csv("data/02-01_측정의_3요소_설비태그목록.csv", parse_dates=['timestamp'])
df = df.sort_values('timestamp')

time_diff = df['timestamp'].diff().mode()[0]
print(f"표의 시각 간격: {time_diff.total_seconds()} 초")

tags = ['MTR_TAG_1', 'HYD_TAG_1', 'FUR_TAG_1'] 

print("\n=== 최솟값, 최댓값, 평균 ===")
stats = df[tags].describe().T[['min', 'max', 'mean']]
print(stats)

print("\n=== 값이 변한 최소 폭 ===")
for tag in tags:
    diffs = df[tag].diff().abs()
    min_step = diffs[diffs > 0].min()
    print(f"{tag}: {min_step}")

import matplotlib.pyplot as plt

df[tags].plot(subplots=True, figsize=(10, 8), drawstyle='steps-post')
plt.suptitle("태그별 데이터 변화 흐름")
plt.show()

# ============================================================================
#실습4번

import pandas as pd

df = pd.read_csv("data/02-01_측정의_3요소_측정샘플.csv", parse_dates=['timestamp'])
df = df.sort_values('timestamp')

time_diff = df['timestamp'].diff().mode()[0]
print(f"표의 시각 간격: {time_diff.total_seconds()} 초")

tags = ['MTR_TAG_1', 'HYD_TAG_1', 'FUR_TAG_1'] 

print("\n=== 최솟값, 최댓값, 평균 ===")
stats = df[tags].describe().T[['min', 'max', 'mean']]
print(stats)

print("\n=== 값이 변한 최소 폭 ===")
for tag in tags:
    diffs = df[tag].diff().abs()
    min_step = diffs[diffs > 0].min()
    print(f"{tag}: {min_step}")

import matplotlib.pyplot as plt

df[tags].plot(subplots=True, figsize=(10, 8), drawstyle='steps-post')
plt.suptitle("태그별 데이터 변화 흐름")
plt.show()

# =========================================================================

import pandas as pd

def get_min_step(series):
  
    diffs = series.diff().abs()
    
    changed_diffs = diffs[diffs > 0]
    
    if not changed_diffs.empty:
        return changed_diffs.min()
    else:
        return 0