# -*- coding: utf-8 -*-
"""
Created on Tue May 25 19:41:02 2021

@author: osman

"""

import pandas as pd
import numpy as np

data = pd.read_csv('./clean_data.csv')


# calculate euclidean distance
def euclidean_distance(a, b):
	return np.sqrt(sum((e1-e2)**2 for e1, e2 in zip(a,b)))

# define data
row1 = [10, 20, 15, 10, 5]
row2 = [12, 24, 18, 8, 7]
# calculate distance
dist = euclidean_distance(row1, row2)
print(dist)

def search(act,v,cp):
    # filtrage du dataset selon les criteres données 
    filter_cap = (data['capital'] >= cp-1000.0) & (data['capital'] <= cp+1000.0)
    df = data[filter_cap]  
    df = df[df['secteur_d_activite'] == act]
    
    return list(df['denomination'].unique())

    
    