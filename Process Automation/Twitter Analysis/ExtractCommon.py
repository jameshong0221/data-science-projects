# This extracts Twitter handles that overlap in twitterfollowers.csv and LaboonCE.csv, i.e. those who have actually followed Laboon's Twitter page.

import pandas as pd

df_twitter = pd.read_csv('twitterfollowers.csv')
df_event = pd.read_csv('LaboonCE.csv')

df_event_users = df_event.iloc[:, [4]]
print(len(df_twitter['Users']))
print(df_event_users.values())
#for i in range(len(df_twitter['Users'])):
for i,x in df_event_users.values():
    print(x[i])
    if x in df_event_users:
#            print(df_event_users.iloc[i])

print(len(df_event_users))
print(len(df_twitter))
print(df_event_users.iloc[1] == df_twitter['Users'][1])
print(df_event_users.iloc[2])
common = df_twitter[df_twitter['Users'].isin(df_event_users)]
print(type(df_twitter['Users']))

common = df_event_users.merge(df_twitter['Users'], how = 'inner')
common = [handle for handle in df_event_users if handle in df_twitter['Users']]

print(common)
print(len(df_event_users))
print(df_event_users.iloc[1]=='@martins385')
