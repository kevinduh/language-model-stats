#!/usr/bin/python
# Author: Suzanna Sia

import pandas as pd

df = pd.read_csv('interim/lm_stats.csv')
df['Citation'] = df.apply(lambda  x: f"[{x['Citation'].strip()}]({x['URL']})", axis=1)

for col in ['Training Strategy', 'Data']:
    df[col] = df[col].apply(lambda x: f"<details>{x}</details>" if len(x.split())>10 else x)

    #df['Training Strategy'] = df['Training Strategy'].apply(lambda x: f"<details>{x}</details>" if
    #        len(x.split())>10 else x)

df = df.drop(columns=['URL'])
df.to_csv('interim/lm_stats.csv', index=False)
