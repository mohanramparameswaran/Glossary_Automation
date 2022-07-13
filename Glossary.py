# -*- coding: utf-8 -*-

import pandas as pd

df1=pd.read_excel("D:\Python_auto\old_glos.xlsx",skiprows=1)
df2=pd.read_excel("D:\Python_auto\Latest.xlsx",skiprows=1)
df3=pd.DataFrame()





old_glossary_row_count=len(df1)
new_glossary_row_count=len(df2)


###logic to find the new DFS for an existing entity
for i in range(0,new_glossary_row_count):
    new_df_id=0
    new_glossary_entity_name=df2["Interface Name"][i]
    new_glossary_df_id=df2["DF_ID"][i]
    for j in range(0,old_glossary_row_count):
        old_glossary_entity_name=df1["Interface Name"][j]
        old_glossary_df_id=df1["DF_ID"][j]
        if ((new_glossary_entity_name == old_glossary_entity_name) and (new_glossary_df_id == old_glossary_df_id)):
            new_df_id=1
            break
        else:
            continue
   
    if (new_df_id==0):

        ##print(df2.iloc[i])
        df3=df3.append(df2.iloc[i])
        
        
print(df3)
df3.to_excel("D:\Python_auto\output.xlsx",sheet_name='New_DFs')
            
            
            
   
