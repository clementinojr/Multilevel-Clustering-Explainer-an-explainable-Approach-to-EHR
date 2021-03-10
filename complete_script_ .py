import sys
import os
import inspect
import pandas as pd
import sys 
from pylab import *
import sklearn
import sklearn.datasets
import sklearn.ensemble
import numpy as np
import lime
import lime.lime_tabular
np.random.seed(1)
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import random
import dataframe_image as dfi
from PIL import Image
import os
import six
from bokeh.io import export_png, export_svgs
from bokeh.models import ColumnDataSource, DataTable, TableColumn
from datetime import datetime

color_list =['mediumslateblue',
 'peachpuff',
 'orangered',
 'cyan',
 'deeppink',
 'coral',
 'olivedrab',
 'moccasin',
 'lightgray',
 'greenyellow',
 'rebeccapurple',
 'navajowhite',
 'gainsboro',
 'aliceblue',
 'olive',
 'yellowgreen',
 'darkolivegreen',
 'silver',
 'palevioletred',
 'lightgrey',
 'palegreen',
 'sandybrown',
 'darkblue',
 'honeydew',
 'lightseagreen',
 'lightyellow',
 'moccasin',
 'mediumseagreen',
 'lightseagreen',
 'papayawhip',
 'blanchedalmond',
 'ghostwhite',
 'orangered',
 'indianred',
 'gainsboro',
 'seagreen',
 'gray',
 'darkturquoise',
 'darkgrey',
 'lavenderblush',
 'paleturquoise',
 'khaki',
 'lime',
 'darkslategray',
 'linen',
 'yellowgreen',
 'darkgoldenrod',
 'darkkhaki',
 'sienna',
 'green']
#------------------------------------------------Functions ---------------------#

def read_csv(name_df,path):
    name_df = pd.read_csv(path+".csv")
    return name_df

def personalize_color_pie(names_columns):
    import matplotlib
    list_color = []
    for name, hex in matplotlib.colors.cnames.items():
        #print(name, hex)
        list_color.append(name)

    col = random.sample(list_color, len(names_columns))
    dic_col = dict(zip(names_columns,col))
    
    return dic_col

def get_values_lime(names_attributes,num_att):
    var_names = names_attributes
    features_id = names_attributes
    features_id.insert(0,"target")
    df = pd.DataFrame(columns=features_id)
    
    size_test = int(len(test))

    size_feature = num_att

    for i in range(0,size_test):
        linha = i
        exp = explainer.explain_instance(test[i], rf.predict_proba, num_features=num_att, top_labels=1)
        #exp.show_in_notebook(show_table=True, show_all=False)
        
        re_id = test_aux[i][1]
        re_name_o = test_aux[i][0]
        
        lista_a =exp.available_labels()
        data_e_hora_atuais = datetime.now()
        data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")
       
       
        num_pos_tar= int (exp.available_labels()[0])
        target = lista_a[0]
        target_name = class_name[num_pos_tar]
       
        
    
        for feat_num in range(0,size_feature):
            names_attributes
            lista_value= exp.as_list(target)
            feature_na_linha = lista_value[feat_num]
            name_d_fea = feature_na_linha[0]
            valor_feat = feature_na_linha[1]

            for name in var_names:
                if name in name_d_fea:
                    df.loc[linha,'target'] = target_name
                    df.loc[linha,name] = valor_feat
        
            df.loc[linha,'nome_oco']= re_name_o
            df.loc[linha, 'num_visit']= re_id
               
    return df




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
  
    D = dict(zip(nome_oco, val_oco))
    D =dict(sorted(D.items(), key=lambda x: x[1],reverse=True))

    import json
    import _pickle as pickle
    name_pC = path+'/file' +str(label)+'.txt'
    fout = name_pC
    fo = open(fout, "w")

    res = [(k, v) for k, v in D.items()]
    
    plt.rcdefaults()
    fig, ax = plt.subplots(figsize=(8,6))

    # Example data
    y_pos = np.arange(len(nome_oco))
    performance = val_oco
    error = np.random.rand(len(nome_oco))
    for i, v in enumerate(val_oco):
        text(v+2 , i + .2, str(v), fontweight = 'bold', fontsize = '10')
    xlim(0, limit_x)
    
    ax.barh(y_pos, performance, xerr=error, align='center',color='teal')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(nome_oco)
    ax.set_xlim(0,50)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Number of times the occurrence appears in the Cluster')
    ax.set_title('Frequency disease occurrence in the Cluster '+str(label)) 
    name_pC = path+'/Ocorrências' +str(label)+'.png' 
    plt.savefig(name_pC,dpi=200,bbox_inches='tight') 
    plt.close()
    



def do_boxPlot(df,tittle,add_to_save):
    df.plot.box(figsize=(25,10))
    plt.title(tittle)
    plt.savefig(add_to_save) 
    plt.close()

def transf_value_df_asfloat(df,list_var_names):
    for var in list_var_names:
        df[var] = df[var].astype(float)
        
    return df

def replace_negative_number_zero(df):
    num = df._get_numeric_data()
    num[num < 0] = 0
    
    return df

def check_class(linha_exemplo,df):
    class_number = int(df.iloc[linha_exemplo]['target'])
    
    return class_number

def get_concat_v_blank(im1, im2,im3, color=(255, 255, 255)):
    dst = Image.new('RGB', (max(im1.width, im2.width,im3.width), im1.height + im2.height+im3.height), color)
    dst.paste(im1, (0, 0))
    dst.paste(im3, (450, im1.height))
    dst.paste(im2, (0, im1.height))
 
   
    return dst

def del_target (df):

    delete = list(df.columns)
    tar = "target"
    matches = [match for match in delete if "target" in match]
   
    df=df.drop(matches, axis=1)
    
    
    return df

def sort_df_qnt_att (df, qnt_att):

    
    delete = list(df.columns)
    tar = "target"
    matches = [match for match in delete if "target" in match]

    df=df.drop(matches, axis=1)
 
    

    df= df.T
    size_df = int(df.size)

    
    namec = list(df.columns)
    df =df.sort_values(by=namec[0],ascending = False)
    
      
    
    df_att_p = df.head(qnt_att) 
    
    df_att_u = df.tail(size_df-qnt_att)
    
    num_att_dif = size_df-qnt_att
 
    sum_att_values = df_att_u.sum()

    
    string_outras_oco= "Other procedures" + " : "+ str(num_att_dif)+ " different types"
    
    df_att_p = df_att_p.T
    df_att_p[string_outras_oco] = sum_att_values

    
    return df_att_p



def local_lever_for_all_objects (df,target_attribute,num_att,show_outras_occ):
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")

    path_file = str(sys.path[0])
    dir_name = 'Figures-Locais' 
    os.mkdir(dir_name)

    from matplotlib import pyplot as plt
   
    num_row = int(len(df.index))
    df_rec = df.copy()
    df_aux = df.copy()
    df = df.drop(columns =target_attribute)
    df = df.drop(columns ='nome_oco')
    df = df.drop(columns ='num_visit')

    
    for i in range(0,num_row):
        nome_oco_row = df_rec.iloc[i]['nome_oco']
        nome_vist_row = df_rec.iloc[i]['num_visit']
        
        number_class = check_class(i,df_aux)
            
        p1 = path_file +'/'+dir_name
        p2 = "["+str(number_class)+"]"+"Object-num-" +str(i)
        path = os.path.join(p1, p2)
        os.mkdir(path)
        
        print_name_oc(nome_oco_row,nome_vist_row,path,i)
    
        df_i = df.iloc[i]
        df_i= df_i[df_i!=0]
        df_i = df_i.dropna()
       
        df_i = df_i.to_frame()
        df_i = df_i.T

        df_pos1 = sort_df_qnt_att(df_i,num_att)
        
        names_colu_dict = list(df_pos1.columns)
        coloor = personalize_color_pie(names_colu_dict)
        list_colors = color_list.copy()
        dic_col = dict(zip(names_colu_dict,list_colors))
        
        nome_oco = names_colu_dict[-1]
        
        dic_col[nome_oco] = "whitesmoke"
        
  
        
        df_bar_plot = df_pos1.copy()
        df_bar_plot = df_bar_plot.loc[:, (df_bar_plot != 0).any(axis=0)]
        
        if show_outras_occ == False:
            delete = list(df_bar_plot.columns)
            tar = "Other procedures"
            matches = [match for match in delete if "Other procedures" in match]
            df_bar_plot=df_bar_plot.drop(matches, axis=1)
            
        number_class = check_class(i,df_aux)
        
       
        df_bar_plot.iloc[0].plot.bar(rot=0,  fontsize=10, legend = 3,figsize=(20, 10))
        plt.title('Example row' + str(i) +"BAR Local Class "+ str(number_class))
        name_file = 'Example row' + str(i) +"BAR Local Class "+ str(number_class) + '.png'
        print(type(df_bar_plot))
        plt.savefig(path+"/"+name_file)
        plt.close()
        
        
        from sklearn import preprocessing

        df_normalized= normalize_df(df_pos1)
       

        plot_local = df_normalized.iloc[0].plot.pie(subplots=True, figsize=(20, 10),autopct='%1.1f%%',colors=[dic_col.get(x) for x in df_normalized.columns])
        plt.legend(loc="upper left")
        plt.title('Object row :' + str(i) + " procedures that influenced the Cluster  "+ str(number_class))
        name_file_p = 'Example row ' + str(i) +"PieCHART Local Class "+ str(number_class) + '.png'
        plt.savefig(path+"/"+name_file_p)
        plt.close()
        
        
        name_file_df = 'DFrow' + str(i) + '.png'
        
        df_pos1=df_pos1.iloc[0]

        
        if number_class == 45:
            df_pos1 = df_pos1.rename({'creatinina___soro': 'Creatinine/sorology', 'ureia___soro': 'Urea/sorology',
            'consulta_de_cardiologia': 'Cardiology appointment','sodio___soro': 'Sodium/sorology',
            'hemograma_completo___contagem_de_plaquetas':'Complete blood count + platelet count'})

        df_pos1 = pd.DataFrame({'Attribute Name':df_pos1.index, 'Value':df_pos1.values})
        df_pos1= df_pos1.sort_values(by=['Value'],ascending=False)
        image_df = df_pos1    

        
        ax = render_mpl_table(image_df, header_columns=0, col_width=7.0)
        type(ax)
        plt.savefig(path+"/"+name_file_df)
        plt.close()

        im1 = Image.open(path+"/"+name_file)
        im2 = Image.open(path+"/"+name_file_df)
        im3 = Image.open(path+"/"+name_file_p)
        
        get_concat_v_blank(im1, im2,im3, (255, 255, 255)).save(path+'/----general_imageRow'+str(i)+".png")

from PIL import Image
def join_image(im1, im2, color=(255, 255, 255)):
    dst = Image.new('RGB', (max(im1.width, im2.width), im1.height + im2.height), color)
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))

    return dst




def render_mpl_table(data, col_width=8.0, row_height=0.9, font_size=13,
                     header_color='#76777E', row_colors=['#f1f1f2', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')

    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)

    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in six.iteritems(mpl_table._cells):
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
    return ax

def global_level_for_all_clusters(df_general, target_attribute,df_initial,num_att,show_outras_occ):
    
    df_general = df_general.drop(columns ='nome_oco')
    df_general = df_general.drop(columns ='num_visit')
    
    path_file = str(sys.path[0])
    dir_name = 'Global-Figure' 
    os.mkdir(dir_name)

    list_class = df_general[target_attribute].unique()
    number_class = int(len(list_class))
    df_aux = df_initial.copy()
    df_no_target = df_aux.copy()
    df_no_target = df_no_target.drop(columns =target_attribute)
        
    
    for i in range(0,number_class):
        df_initial = df_aux

        p1 = path_file +'/'+dir_name
        p2 = "Result-Cluster-" +str(list_class[i])
        path = os.path.join(p1, p2)
        os.mkdir(path)


        string_name_class = "df_class"+str(list_class[i])
        string_name_class = pd.DataFrame()
        string_name_class = df_general[df_general.target==list_class[i]]
        
        string_name_class = string_name_class.drop(columns = target_attribute)
        df_initial = df_initial.drop(columns =target_attribute)
       
        string_name_class = del_target(string_name_class)    
        string_name_class = normalize_df(string_name_class)
        print(string_name_class)
   
        string_aux = "c"+str((list_class[i]))
       
        
        string_aux = string_name_class.mean(axis = 0).sort_values(ascending=False)
        
        string_aux = string_aux.to_frame()
        string_aux = string_aux.T
     
        string_aux = string_aux.loc[:, (string_aux != 0).any(axis=0)]
        string_aux = sort_df_qnt_att(string_aux,num_att)
        
        df_plot_bar = string_aux.copy()
        if show_outras_occ == False:
            delete = list(df_plot_bar.columns)
            matches = [match for match in delete if  "Other procedures" in match]
 
            df_plot_bar=df_plot_bar.drop(matches, axis=1)
        
        string_aux = string_aux.iloc[0]
   
        string_df = pd.DataFrame(string_aux).transpose()
        #({'Nome Variavel':df_pos.index, 'Valores':df_pos.values})
        tt = pd.DataFrame({'Attribute Name':string_aux.index, 'Value':string_aux.values})
        name_col = list(tt['Attribute Name'].values)

       
        matches = [match for match in name_col if "Other procedures" in match]
        matches  = str(matches)
    
        del name_col[-1]
       
        plotdf = df_initial[name_col]
        df_plot_bar.plot.bar(rot=0,  fontsize=10, legend = 3,figsize=(10, 8) )
        plt.title('BAR Global Class'+str(list_class[i]))
        name_b= 'BAR_CLass'+ str(list_class[i])+'.png'
        plt.savefig(path+'/'+ name_b)
        plt.close()
        
        
        names_colu_dict = list(string_df.columns)

        coloor = personalize_color_pie(names_colu_dict)
        list_colors = color_list.copy()
        dic_col = dict(zip(names_colu_dict,list_colors))
        
        nome_oco = names_colu_dict[-1]
        
        dic_col[nome_oco] = "whitesmoke"
        
        string_df_aux = string_df
       
        
        #Plot Pie Chart
        print(string_df)
        plot_global = string_df.loc[0].plot.pie(subplots=True, figsize=(15, 10),autopct='%1.1f%%', legend = 2,colors=[dic_col.get(x) for x in string_df.columns])
        #--plot_global = string_df.loc[0].plot.pie(subplots=True, figsize=(15, 10),autopct='%1.1f%%', legend = 1)
        plt.title('Procedures that influenced the Cluster '+ str(list_class[i]))
        name_pC = 'Procedimentos que influênciaram o grupo '+ str(list_class[i]) +'.png' 
        plt.savefig(path+'/'+ name_pC) 
        plt.close()
        
        
        #Plot Box Plot Global 
        plotdf.plot.box(figsize=(25,10))
        plt.title('Box Plot Global Class' + str(list_class[i]) )
        name_boxP = 'BoxPlot_class_'+ str(list_class[i])+'.png'
        plt.savefig(path+'/'+name_boxP)
        plt.close()
        
        return_num_visit (df_oco,list_class[i],path)
        
        image_df = tt
        
        
        
        name_sv_df= "df"+str(list_class[i])+".png"

        ax = render_mpl_table(image_df, header_columns=0, col_width=5.0,header_color='#76777E')
        #fig.savefig('Figure_all_examples_local/'+name_file_df)
        plt.savefig(path+'/'+name_sv_df)
        #dfi.export(image_df,"Figures_Global_Class/"+name_sv_df)
        plt.close()

        im1 = Image.open(path+'/'+name_b)
        im2 = Image.open(path+'/'+name_sv_df)
        im3 = Image.open(path+'/'+name_pC)

        
        get_concat_v_blank(im3, im2,im1, (255, 255, 255)).save(path+'/'+'----general_image_GRUPO_'+str(list_class[i])+".png")

        img2 = Image.open('/image_procedimentos/BAR_Chart_Global_Grupo_'+str(list_class[i])+'.png')
        img1 = Image.open(path+'/'+'----general_image_GRUPO_'+str(list_class[i])+".png")
        
        join_image(img1, img2, (255, 255, 255)).save(path+ '/'+ 'GERAL_GRUPO_'+str(list_class[i])+'.png')

        return_ocorrence_name(df_oco,list_class[i],path)

        Image.open(path+ '/'+ 'GERAL_GRUPO_'+str(list_class[i])+'.png')
        image1 = Image.open(path+'/GERAL_GRUPO_'+str(list_class[i])+'.png')
        image2 = Image.open(path+'/Ocorrências'+str(list_class[i])+'.png')
        
        
        join_image(image1, image2, (255, 255, 255)).save(path+'/Ocorrencias_Grupo '+str(list_class[i])+'.png')



def return_num_visit (df_initial, label, path):
    df_initial = df_initial.query('Labels == @label')
    list_visit = list(df_initial['ID'])
    list_visit_unique =  list(dict.fromkeys(list_visit))
    qnt_int = int(len(list_visit_unique))
    d= {'Cluster Label': [label], 'Quantity of EHR': [qnt_int]}
    df_resut = pd.DataFrame(data=d)
    ax = render_mpl_table(df_resut, header_columns=0, col_width=6.0,font_size=30)
    
    plt.savefig(path+"/"+'qnt_internação '+str(label)+'png')
    plt.close()
    
    return 

def print_name_oc (oco_row,id_row, path,row):
    
    d= {'Hospitalization ID': [id_row], 'Occurrence Name': [oco_row]}
    df_resut = pd.DataFrame(data=d)
    ax = render_mpl_table(df_resut, header_columns=0, col_width=7.5)
    
    plt.savefig(path+"/"+'info_id_inte '+str(row)+'png')
    plt.close()
    
    return 

                
def normalize_df(df_no_target):
    df_no_target =df_no_target.div(df_no_target.sum(axis=1), axis=0)
    df_no_target.mul(100)
    
    return df_no_target

# ----------------------------------------------MAIN ------------------------------------------#

#---Preprocessing DataSet ---#
df_intial = read_csv('df', 'df5')
df_intial= df_intial.drop(columns=['emergency_room_visit', 'outpatient_visit', 'inpatient_visit'])
df = df_intial.copy()
df_oco = df_intial.copy()
df =df.drop_duplicates()
df_new = df.query('Labels == 45 or Labels == 9 or Labels == 7 or Labels == 5')
nunique = df_new.apply(pd.Series.nunique)
cols_to_drop = nunique[nunique == 1].index
df_new=df_new.drop(cols_to_drop, axis=1)
df_new =df_new.reset_index()
df_new = df_new.drop(columns =['index'])
df_new = df_new.rename(columns = {'Labels': 'target'}, inplace = False)
labels = df_new['target'].to_numpy()
df_new_wot = df_new
name_att = list(df_new_wot.columns)
class_name = df_new_wot.target.unique()
df_new_wot = df_new_wot.drop(columns =['target'])
data =df_new_wot.to_numpy()
name_att = list(df_new_wot.columns)
name_att.remove('Nome_Ocorrencia')
name_att.remove('ID')
qnt_d_att = int(len(name_att))




#------ Treining and slip Model ------#
train, test, labels_train, labels_test = sklearn.model_selection.train_test_split(data, labels, train_size=0.7)
test_aux = test
train_aux = train
test = np.delete(test, np.s_[0:2], 1)
train = np.delete(train, np.s_[0:2], 1)
rf = sklearn.ensemble.RandomForestClassifier(n_estimators=500)
rf.fit(train, labels_train)
explainer = lime.lime_tabular.LimeTabularExplainer(train, feature_names=name_att, class_names=class_name, discretize_continuous=True)
sklearn.metrics.accuracy_score(labels_test, rf.predict(test))
rf.predict(test) == labels_test
exp = explainer.explain_instance(test[1], rf.predict_proba, num_features=543, top_labels=1)




#This function is used to extract local values.
     #Passing the name of the attributes and the number of attributes that should return the values as a parameter
     # _- It returns a dataframe with the weights of ALL variables for the classification and the class in which it was classified
df_initial = get_values_lime(name_att,qnt_d_att-2)

#------------------------------------------------------------------------------------------------------------------------------------#
#Writing the result of the previous function in a csv file
df_initial.to_csv('final_ALLFFFF_todas_NEWWWWWWWWWWWWWW.csv', index=False)

#------------------------------------------------------------------------------------------------------------------------------------#

# A partir daqui que leio o Arquivo já gerado pelas possibilidades e tem o meu método e a preparação e plotagem dos gráficos

df_initial =read_csv('df_initial', 'final_ALLFFFF_todas_NEWWWWWWWWWWWWWW')

#------------------------------------------------------------------------------------------------------------------------------------#

#Replacing all NEGATIVE values with 0
df_complete = replace_negative_number_zero(df_initial)

#Function to observe each object by generating an explanation for each of the objects
# Dataframe parameter with all lines and weights, the name of the target variable and the number of attributes to be considered in the plot
local_lever_for_all_objects(df_complete,'target',5,False)

#This function is for GLOBAL observation of the methods separating by CLusters
# The dataframe is again entered as the name of the target variable and the number of attributes that must be returned
global_level_for_all_clusters(df_complete,'target',df_initial,5,False)





