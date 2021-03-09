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
    en_lista = ['Congestive heart failure','Atrial fibrillation and flutter','Unstable angina', 'Essential hypertension (primary)',
            'Acute myocardial infarction, unspecified','Syncope and collapse','Bronchopneumonia, unspecified','Dyspnea','Chest pain, unspecified',
            'Precordial pain','Pulmonary edema, not otherwise specified','Urinary tract infection of unspecified location','Secondary hypertension, unspecified',
            'Unspecified myositis','Other forms of acute ischemic heart disease','Diarrhea and gastroenteritis of presumed infectious origin',
           'Other specified cardiac arrhythmias','Malaise, fatigue','Acute infection of upper airways, unspecified','Unspecified anxiety disorder']


    return nome_oco,val_oco
