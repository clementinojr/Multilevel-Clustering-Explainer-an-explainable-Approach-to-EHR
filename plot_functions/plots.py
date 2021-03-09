    # Example data

import matplotlib.pyplot as plt

    def plot_bar (list_name,list_values,limit,path_complet,title,name_xlabel):
        max_value = max(list_values)
        limit_x = (max_value *0.09)+max_value

        plt.rcdefaults()
        fig, ax = plt.subplots(figsize=(8,6))

        y_pos = np.arange(len(list_name))
        performance = list_values
        error = np.random.rand(len(list_name))
        for i, v in enumerate(list_values):
            text(v+2 , i + .2, str(v), fontweight = 'bold', fontsize = '10')
        xlim(0, max(list_values)+90)
        
        ax.barh(y_pos, performance, xerr=error, align='center',color = 'sienna')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(list_name)
        ax.set_xlim(0,limit_x)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel = name_xlabel
        ax.set_title = title
        #ax.set_xlabel('Number of times the procedure was performed')
        #ax.set_title('Frequency disease occurrence in the Cluster'+"  " +str(num_g) )
        #name_pC = 'BAR_Chart_Global_Grupo_'+ str(num_g) +'.png' 
        #plt.savefig('image_procedimentos/'+ name_pC,dpi=200,bbox_inches='tight')
        plt.savefig(path_complet,dpi=200,bbox_inches='tight')  
        plt.show()

