# 실습1번

import pandas as pd

df = pd.read_csv("data/01-01_철강_공정_개관_설비태그.csv")

print("전체 행수: ", len(df))

df[["plant", "process", "equip", "umit_no", "measure"]] = df["tag"].str.split("-", expand=True)

PROCESS_MAP = {
                "SNT":"소결",
                "CKO":"코크스",
                "BF":"고로",
                "BOF":"전로",
                "CCM":"연주",
                "HSM":"열간압연",
                "CRM":"냉간압연",
                "UTL":"유틸리티"
}

MEASURE_KR = {
              "VIB": "진동",
              "CUR": "전류",
              "TMP": "온도",
              "PRS": "압력",
              "FLW": "유량",
              "SPD": "속도",
              "LVL": "레벨"
              }

df["tag"] = df["unit"].map(PROCESS_MAP).fillna("미등록")
df["tag"] = df["unit"].map(MEASURE_KR).fillna("미등록")

print(df.head())

def classify_stage(proc):
    if proc in ["SNT", "CKO", "BF"]:
        return "상공정"
    elif proc in ["CCM", "HSM"]:
        return "하공정"
    elif proc == "UTL":
        return "유틸리티"
    else:
        return "미상"

df["상하공정"] = df["unit"].apply(classify_stage)

most_tags_process = df["tag"].value_counts().idxmax()
print(f"가장 태그가 많은 공정: {most_tags_process}")

most_tags_measure = df["note"].value_counts().idxmax()
print(f"가장 태그가 많은 계측 항목: {most_tags_measure}")

# ===============================================================
#실습2번

import pandas as pd

df = pd.read_csv("data/01-02_원료_전처리와_제선_제선조업.csv")

df.columns = df.columns.str.strip()


cols = ["blast_flow_nm3min", "blast_pressure_kpa","blower_vib_mms"]

before = df.iloc[:360]
after = df.iloc[360:]

before_mean = before[cols].mean()
after_mean = after[cols].mean()

comparison_df = pd.DataFrame({
    '앞 6시간 평균': before_mean,
    '뒤 6시간 평균': after_mean,
    '차이 (뒤 - 앞)': after_mean - before_mean
})

comparison_df['변화 방향'] = comparison_df['차이 (뒤 - 앞)'].apply(
    lambda x: '증가' if x > 0 else ('감소' if x < 0 else '동일')
)

print(comparison_df)