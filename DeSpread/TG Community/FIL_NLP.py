# Create a function to do the following for ALL channels:
# 1. 한 사람이 단기간에 여러번 메세지 보내면 합쳐서 문장 혹은 문단으로 변형(?) - 시간 단위 정해서 하면 좋을듯 (시간, 일, 등등)
# 2. 날짜별로 대화 묶음 (associate with news and ANNs) + 기간별로 sentiment score (불장 / 하락장 비교)
# 3. 유저별로 대화 묶음 (2번이랑 통합해도 괜찮고)
# 4. 공지 후 대화량 및 반응 파악(?)

# Sort values reference "https://sparkbyexamples.com/pandas/pandas-sort-by-column-values-in-dataframe/?expand_article=1"
#Drop rows with Nans. Refer to previous projects

#df.dropna(subset = ['message.text'], inplace = True) -- The null entries represent "유저가 입장했습니다"

#파일코인 메세지 추출한 파일 불러오고 DF로 저장

import pandas as pd
from pykospacing import Spacing

df = pd.read_csv('filecoinkorea.csv')

#데이터 구조 확인
df.info()
df.head()

#Fix typo in column
df.rename({" message.date":"message.date"}, axis=1, inplace=True)


# Clean Text
punct = "/-'?!.,#$%\'()*+-/:;<=>@[\\]^_`{|}~" + '""“”’' + '∞θ÷α•à−β∅³π‘₹´°£€\×™√²—–&'
punct_mapping = {"‘": "'", "₹": "e", "´": "'", "°": "", "€": "e", "™": "tm", "√": " sqrt ", "×": "x", "²": "2", "—": "-", "–": "-", "’": "'", "_": "-", "`": "'", '“': '"', '”': '"', '“': '"', "£": "e", '∞': 'infinity', 'θ': 'theta', '÷': '/', 'α': 'alpha', '•': '.', 'à': 'a', '−': '-', 'β': 'beta', '∅': '', '³': '3', 'π': 'pi', } 


def clean(text, punct, mapping):
    for p in mapping:
        text = text.replace(p, mapping[p])
    
    for p in punct:
        text = text.replace(p, f' {p} ')
    
    specials = {'\u200b': ' ', '…': ' ... ', '\ufeff': '', 'करना': '', 'है': ''}
    for s in specials:
        text = text.replace(s, specials[s])
    
    return text.strip()


import re


def clean_str(text):
    pattern = '([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)' # E-mail제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '(http|ftp|https)://(?:[-\w.]|(?:%[\da-fA-F]{2}))+' # URL제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '([ㄱ-ㅎㅏ-ㅣ]+)'  # 한글 자음, 모음 제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '<[^>]*>'         # HTML 태그 제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '[^\w\s\n]'         # 특수기호제거
    text = re.sub(pattern=pattern, repl='', string=text)
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]','', string=text)
    text = re.sub('\n', '.', string=text)
    return text 

j=1
while j < 5:
    for msg in df["message.text"]:
        print(msg)
    j += 1

