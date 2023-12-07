# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 14:37:49 2023

@author: mimounid
"""

import pandas as pd

df = pd.read_csv('followers.csv')
df2 = pd.read_csv('followings.csv')

print(
      df.groupby(['date']).size().reset_index(name='count'), '\n',
      df2.groupby(['date']).size().reset_index(name='count')

      )