#!/bin/bash

for f in no_dup*
import pandas as pd
data = pd.read_excel("no_dup_Aberdeenshire.xlsx")
data1 = pd.read_excel("medicinals.xlsx")
pd.DataFrame(data)
df = pd.DataFrame(data)
df1 = pd.DataFrame(data1)

#pd.merge(data, data1, how='inner', on=['species'], left_on=None, right_on=None,left_index=False, right_index=False, sort=True,suffixes=('_x', '_y'), copy=True, indicator=False)
#merged_no_dup_no_dup_Aberdeenshire = pd.merge(data, data1, how='inner', on=['species'], sort=True)
#df_merged = pd.DataFrame(merged_no_dup_no_dup_Aberdeenshire)
#df_merged.to_excel('merged_no_dup_no_dup_Aberdeenshire.xlsx')
merged_no_dup_no_dup_Aberdeenshire = pd.merge(data, data1[['species']], how='inner', on='species') ## Drop columns from data and retaining only 'species' column
df_merged=pd.DataFrame(merged_no_dup_no_dup_Aberdeenshire)
df_merged.to_excel('merged_no_dup_no_dup_Aberdeenshire.xlsx')
