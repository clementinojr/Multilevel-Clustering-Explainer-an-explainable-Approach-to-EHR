#Deletar valores iguais de uma deteminada coluna(subset) e manter a primeira ocorrência
def del_same_values_colum(df, name_colum):
    df = df.drop_duplicates(subset=['ID'], keep='first')
    return df

#Reading file provide SQL
def read_csv(name_df,path):
    name_df = pd.read_csv(path+".csv")
    return name_df

