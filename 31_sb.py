tag = "PL1-SNT-FAN-01-VIB"
# 공장-공정-설비-일련번호-계측값

parts = tag.split("-")
print(parts)

# -기준으로 나눈 결과 문자열을 변수에 따로 저장
plant = parts[0] # 공장
process = parts[1] # 공정
equip = parts[2] # 설비
umit_no = parts[3] # 
measure = parts[4] #

print(plant, process, equip, umit_no, measure)
PROCESS_KR = { 
              "SNT":"소결",
              "CKO":"코크스",
              "BF":"고로",
              "BOF":"전로",
              "CCM":"연주",
              "HSM":"열간압연",
              "CRM":"냉간압연",
              "UTL":"유틸리티",}

# 전로를 출력하려면? (BOF 키)
print(PROCESS_KR["BOF"])

# 없는 태그를 가져오는 것 방지
print(PROCESS_KR.get("BOF","미등록")) 

# 계측항목 규칙표

MEASURE_KR = {
              "VIB": "진동",
              "CUR": "전류",
              "TMP": "온도",
              "PRS": "압력",
              "FLW": "유량",
              "SPD": "속도",
              "LVL": "레벨"
              }

print(MEASURE_KR.get("PRS", "미등록"))

import pandas as pd

df = pd.read_csv("data/01-01_철강_공정_개관_설비태그.csv")
print(df.shape)
print(df.columns.tolist())

# ===========================================================
import pandas as pd

df = pd.read_csv("data/01-02_원료_전처리와_제선_제선조업.csv")
print(df.shape)
# timestamp열 데이터타임 확인
print("timestamp의 데이터타임: ", df["timestamp"].dtype)
df["timestamp"]=pd.to_datetime(df["timestamp"])
print("timestamp의 데이터타임(2): ", df["timestamp"].dtype)

#### 2. read_csv()의 옵션값 이용
df = pd.read_csv("data/01-02_원료_전처리와_제선_제선조업.csv", parse_dates=["timestamp"])
print("timestamp의 데이터타임(3): ", df["timestamp"].dtype)

# timestamp의 시간 간격
gaps = df["timestamp"].diff().value_counts()
print(gaps)

'''
timestamp
0 days 00:01:00    719
Name: count, dtype: int64
'''

# 송풍량, 송풍압, 송풍기 진동
print(df[["blast_flow_nm3min", "blast_pressure_kpa","blower_vib_mms"]].describe().round(1))

'''
blast_flow_nm3min  blast_pressure_kpa  blower_vib_mms
count              720.0               720.0           720.0
mean              5088.2               388.8             3.4
std                159.6                13.0             0.1
min               4681.8               372.8             3.2
25%               4977.5               379.4             3.3
50%               5180.8               381.7             3.4
75%               5202.5               398.3             3.4
max               5258.2               421.4             3.6
'''

# 이동 평균: N분간의 흔들림을 확인하여 송풍량의 장기적인 방향을 보는 지표
# 통기성이 나빠지면 공기가 원료층을 통과하기 어려워져서 실제 들어가는 풍량이 감소할 수 있습니다

# 15분 간격 이동평균 구하기
df["flow_ma"] = df["blast_flow_nm3min"].rolling(window=15).mean() 
print(df["flow_ma"].head(3).tolist())

print(round(df["flow_ma"].iloc[14], 1), round(df["flow_ma"].iloc[400], 1))

# 이동 표준편차
df["top_sd"]=df["top_pressure_kpa"].rolling(window=30).std()
print(round(df["top_sd"].iloc[200],2), round(df["top_sd"].iloc[560],2))
