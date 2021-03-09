def return_ocorrence_name(df_initial_com_nome_d_oco, label,path):
    df = df_initial_com_nome_d_oco
    df = df.query(' Labels== @label')
    df =df.drop_duplicates()
    lista_proteste = df['Nome_Ocorrencia'].value_counts()
    
    df_table = pd.DataFrame({'Occurrence Name':lista_proteste.index, 'Frequency':lista_proteste.values})
    
    nome_oco = lista_proteste.index
    val_oco = lista_proteste.values

    nome_oco =nome_oco[:20]
    val_oco = val_oco[:20]
    max_value = max(val_oco)
    limit_x = (max_value *0.09)+max_value 
    

    return nome_oco,val_oco
