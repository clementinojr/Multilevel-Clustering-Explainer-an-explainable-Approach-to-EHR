import uteis
import plots
import recovery_procedures.py


#---------------------------------------Procedures ---------------------

df_original= uteis.read_csv()
df_clustering= uteis.read_csv()



#Para cada  grupo - qnt_cluster

labels_do_grupo = df_clustering_complete['Labels'].value_counts()
labels_do_grupo = labels_do_grupo.index

qnt_cluster

for i in range(0,qnt_cluster):
    num_g = int(labels_do_grupo[i])
    name_proce,value_proce = preparing_plot(num_g)
    plots(................................)

# ---------------------------------------Occurence ----------------------#


for i in range(0,qnt_cluster):
    num_g = int(labels_do_grupo[i])
    name_proce,value_proce = preparing_plot(df_clustering,num_g, ...........)

    plots(................................)








