#!/usr/bin/python
# Author: Suzanna Sia

import pandas as pd

df = pd.read_csv('interim/lm_stats.csv')
df['Citation'] = df.apply(lambda  x: f"[{x['Citation'].strip()}]({x['URL']})", axis=1)

for col in ['Training Strategy', 'Data']:
    df[col] = df[col].apply(lambda x: f"<details>{x}</details>" if len(x.split())>10 else x)

    #df['Training Strategy'] = df['Training Strategy'].apply(lambda x: f"<details>{x}</details>" if
    #        len(x.split())>10 else x)

df_mono = df[df['Languages']=="en"]
df_multi = df[df['Languages']=="ml"]

df_mono = df_mono.drop(columns=['URL', 'Languages'])
df_multi = df_multi.drop(columns=['URL', 'Languages'])

df_mono.to_csv('interim/lm_stats_mono.csv', index=False)
df_multi.to_csv('interim/lm_stats_multi.csv', index=False)
