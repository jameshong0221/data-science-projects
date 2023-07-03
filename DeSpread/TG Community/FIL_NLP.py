import pandas as pd
from pykospacing import Spacing

#파일코인 메세지 추출한 파일 불러오고 DF로 저장
df = pd.read_csv('filecoinkorea.csv')

#데이터 구조 확인
df.info()
df.head()

#Fix typo in column
df.rename({" message.date":"message.date"}, axis=1, inplace=True)

# Create a function to do the following for ALL channels:
# 1. 한 사람이 단기간에 여러번 메세지 보내면 합쳐서 문장 혹은 문단으로 변형(?)
# 2. 날짜별로 대화 묶음 (associate with news and ANNs) + 기간별로 sentiment score (불장 / 하락장 비교)
# 3. 유저별로 대화 묶음

# Sort values reference "https://sparkbyexamples.com/pandas/pandas-sort-by-column-values-in-dataframe/?expand_article=1"
#Drop rows with Nans. Refer to previous projects

