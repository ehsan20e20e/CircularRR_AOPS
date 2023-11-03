"""
The code for the research presented in the paper titled "A deep learning method for empirical spectral prediction and inverse design of all-optical nonlinear plasmonic ring resonator switches

@authors: Ehsan Adibnia, Majid Ghadrdan and Mohammad Ali Mansouri-Birjandi
Corresponding author: mansouri@ece.usb.ac.ir

This code is corresponding to the Section S2 (Dataset discussion) of the Supplementary Information of the article.
This code regenerates the Fig S2a and Fig S2b of the Supplementary Information of the paper.
Please cite the paper in any publication using this code.
"""
import numpy as np
import pandas as pd 
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt 
from matplotlib.font_manager import FontProperties

### Load the data from CSV file (the results of FDTD solver)
result1 = pd.read_csv("result_V.csv", header=None)
result1 = result1.to_numpy()
result1 = result1.astype(np.float16)

x = result1[0:result1.shape[0],0:6]
y = result1[0:result1.shape[0],6]

### Feature Scaling
sc = StandardScaler()
x = sc.fit_transform(x)

### plot histogram of input data
data1 = x[0:x.shape[0],1]  
data2 = x[0:x.shape[0],2]   
data3 = x[0:x.shape[0],3]  
data4 = x[0:x.shape[0],4]
data5 = x[0:x.shape[0],5]
plt.hist([data1, data2, data3, data4, data5], linewidth=6)
plt.title('The input dataset used to train the neural network', fontname='Times New Roman', fontsize=16, loc='center')
plt.xlabel('Dataset', fontname='Times New Roman', fontsize=18)
plt.ylabel('Count', fontname='Times New Roman', fontsize=18)
plt.xticks(fontfamily='Times New Roman', fontsize=16)
plt.yticks(fontfamily='Times New Roman', fontsize=16)
font_prop = FontProperties(family="Times New Roman", size=16)
plt.legend(['G1', 'G2', 'G3', 'G4', 'G5'], prop=font_prop,bbox_to_anchor=(1.05, 1))
plt.savefig("figureS2a.eps", format="eps", dpi=300, bbox_inches="tight")
plt.savefig("figureS2a.png", format="png", dpi=300, bbox_inches="tight")
plt.show()

### plot histogram of output data
data6 = result1[0:result1.shape[0],6]   
data7 = abs(result1[0:result1.shape[0],7])
plt.hist([data6, data7],label=['', ''])
plt.title('The input dataset used to train the neural network', fontname='Times New Roman', fontsize=16, loc='center')
plt.xlabel('Dataset', fontname='Times New Roman', fontsize=18)
plt.ylabel('Count', fontname='Times New Roman', fontsize=18)
plt.xticks(fontfamily='Times New Roman', fontsize=16)
plt.yticks(fontfamily='Times New Roman', fontsize=16)
font_prop = FontProperties(family="Times New Roman", size=16)
plt.legend(['Through port','Drop port'], prop=font_prop, loc='upper center')
plt.savefig("figureS2b.eps", format="eps", dpi=300, bbox_inches="tight")
plt.savefig("figureS2b.png", format="png", dpi=300, bbox_inches="tight")
plt.show()