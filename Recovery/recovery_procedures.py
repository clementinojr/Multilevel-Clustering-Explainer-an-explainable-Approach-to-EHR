from pylab import *
import json
import collections
import numpy as np
import pandas as pd
import uteis
import plots 


def count_proce (df_current_label, df_original):
    df_current_label = df_current_label [['ID']]
    df_current_label = df_current_label.rename(columns={'ID': 'visit_id'})
    new_df = df_current_label.merge(df_original, on='visit_id', how='left').drop_duplicates()
    print(new_df)
    count =0 
    #Agora buscar as contagens
    arr = []
    arr_t=[]

    lista_proce = []
    for i, row in new_df.iterrows():
        obj = json.loads(row['internacao_json'])
        string_concept = ''
        #arr_t.append(obj['visit_concept_name'])
        string_concept+=obj['visit_concept_name']+'&'
        if(obj['procedimentos'] != None):
            for procedure_name in obj['procedimentos']:
                nome_do_procedimento = str(procedure_name['procedure_ocurrence_concept_name'])
                string_concept += nome_do_procedimento + "&"
                arr_t.append(nome_do_procedimento)
        else:
            print('')
            
        arr.append(string_concept)
        
    c = collections.Counter(arr_t)
    df_final_show = pd.DataFrame.from_dict(c, orient='index').reset_index()
    df_final_show = df_final_show.rename(columns={'index':'nome_pro', 0:'contagem'})
    
    return  df_final_show    


def preparing_plot(df_clustering_complete,label)
    #creating dataframes 
    num_g = int (label)
    
    nome_df = "DfGrup "+str(lista[i])
    nome_df =  df_clustering_complete.query('Labels == @num_g')

    df = del_same_values_colum(nome_df, "ID")
    df = count_proce(df,df_json)
    
    
    df=df.sort_values(by=['contagem'],ascending=False)
    df = df.head(30) #Number of proccedure most frequents to show 
    print(df)
    
    lista_pro =[]
    lista_v  = []

    lista_pro = list(df['nome_pro'].values)
    lista_v = list(df['contagem'].values)
    

    return [lista_pro,lista_v]

   
   