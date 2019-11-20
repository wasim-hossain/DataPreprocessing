#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Wasim H.
"""
from scipy.io import arff
import pandas as pd

def arffToCSV(src, trgt, dataName):
	data = arff.loadarff(src)
	df = pd.DataFrame(data[0])
	df_TA = df[df.columns[len(df.columns)-1]].astype('int')

	TA=[]
	for i in range(len(df)-1):
	    df_data = df.iloc[i,0:len(df.columns)-1]
	    fileName = dataName+'_'+str(i)    
	    df_data = df.iloc[i,0:len(df.columns)-1]
	    df_data.to_csv(trgt+fileName+'.csv', index=None)
	    print(fileName)
	    label = int(df_TA.iloc[[i]])
	    TA.append([fileName,str(label)])
	df_TA_fnl = pd.DataFrame(TA)    
	df_TA_fnl.to_csv(trgt+'TA_'+dataName+'.csv', header=None, index=None)

