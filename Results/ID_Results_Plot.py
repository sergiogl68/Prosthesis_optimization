
# -*- coding: utf-8 -*-
"""
@author: 
"""

#----------------------------------------------------------------------------#
#-----------------------------------------------------------------------------
#                                                                            #
#                              IMPORTS                                       #
#                                                                            #
#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#


from matplotlib import pyplot as plt
import numpy as np



#----------------------------------------------------------------------------#
#-----------------------------------------------------------------------------
#                                                                            #
#                              FUNCTIONS                                     #
#                                                                            #
#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#

                         #______________________#
                         
def readSTO(filename):

    file_id = open(filename, 'r')

    # read header
    next_line = file_id.readline()
    header = [next_line]
    nc = 0
    nr = 0
    while not 'endheader' in next_line:
        if 'datacolumns' in next_line:
            nc = int(next_line[next_line.index(' ') + 1:len(next_line)])
        elif 'datarows' in next_line:
            nr = int(next_line[next_line.index(' ') + 1:len(next_line)])
        elif 'nColumns' in next_line:
            nc = int(next_line[next_line.index('=') + 1:len(next_line)])
        elif 'nRows' in next_line:
            nr = int(next_line[next_line.index('=') + 1:len(next_line)])

        next_line = file_id.readline()
        header.append(next_line)

    # process column labels
    next_line = file_id.readline()
    if next_line.isspace() == True:
        next_line = file_id.readline()

    labels = next_line.split()

    # get data
    data = []
    for i in range(1, nr + 1):
        d = [float(x) for x in file_id.readline().split()]
        data.append(d)

    file_id.close()

    return header, labels, data

                          #______________________#
                          
def var_plot_num(var_plot):  #Change according to the variable you want to observe, 0 is time.
    plt.figure()
    plt.plot(data_f1[0, 0:data_f1.shape[1]],data_f1[var_plot,0:data_f1.shape[1]],label=var2[var_plot]+"_Base")
    plt.plot(data_f2[0, 0:data_f2.shape[1]],data_f2[var_plot,0:data_f2.shape[1]],label=var4[var_plot]+"_Spring")
    plt.xlabel("Time")
    plt.legend()

def var_plot_num_alone(var_plot):  #Change according to the variable you want to observe, 0 is time.
    plt.figure()
    plt.plot(data_f1[0, 0:data_f1.shape[1]],data_f1[var_plot,0:data_f1.shape[1]],label=var2[var_plot]+"_Base")
    plt.xlabel("Time")
    plt.legend()



#----------------------------------------------------------------------------#
#-----------------------------------------------------------------------------
#                                                                            #
#                           SCRIPT START                                     #
#                                                                            #
#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#

#replace with the pathfiles of the conditions you would like to plot/compare

var1, var2, data_f1 = readSTO('C:/Users/sergi/Videos/Modelos/RESPALDO MODELOS/CMC_Spring/Results/Base/ID/inverse_dynamics.sto')
var3, var4, data_f2 = readSTO('C:/Users/sergi/Videos/Modelos/RESPALDO MODELOS/CMC_Spring/Results/Spring/ID/inverse_dynamics.sto')
#var3, var4, data_f2 = readSTO('C:/Users/sergi/Videos/Modelos/RESPALDO MODELOS/CMC_Spring/Results/Base/ID/Ext_rot_Unlocked/inverse_dynamics.sto')

data_f1=np.asarray(data_f1).transpose()
data_f2=np.asarray(data_f2).transpose()

#compare the contents of the files

dif=np.max(data_f1 != data_f2,axis=1)

plt.figure()
plt.plot(dif,var2)

if sum(dif) != 0:
    for i in range(0,len(dif)-1):
        if dif[i] != 0:
            plt.figure()
            plt.plot(data_f1[0, 0:data_f1.shape[1]],data_f1[i,0:data_f1.shape[1]],label=var2[i]+"_Base")
            plt.plot(data_f2[0, 0:data_f2.shape[1]],data_f2[i,0:data_f2.shape[1]],label=var4[i]+"_Spring")
            plt.xlabel("Time")
            plt.legend()
else:
    print("No difference in any variable")


#Plot one variable to compare between conditions   

#var_plot_num(40)

