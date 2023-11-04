"""
The code for the research presented in the paper titled "A deep learning method for empirical spectral prediction and inverse design of all-optical nonlinear plasmonic ring resonator switches

@authors: Ehsan Adibnia, Majid Ghadrdan and Mohammad Ali Mansouri-Birjandi
Corresponding author: mansouri@ece.usb.ac.ir

This code is corresponding to the Forward Deep Neural Network (DNN) section of the article.
This code regenerates the Fig 3b and 3c of the paper.
Please cite the paper in any publication using this code.
"""
import numpy as np
import keras
import pandas as pd 
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt 
from matplotlib.font_manager import FontProperties
result1 = pd.read_csv("result_V.csv", header=None)
result1 = result1.to_numpy()
result1 = result1.astype(np.float16)

x_train = result1[0:result1.shape[0],0:6]
y_train = result1[0:result1.shape[0],6]

sc = StandardScaler()
x_train = sc.fit_transform(x_train)

# load the seved forward model
json_file = open("CircularRR_AOPS_forward_model.json", "r")
loaded_model_json = json_file.read()
json_file.close()
loaded_model = keras.models.model_from_json(loaded_model_json)
loaded_model.load_weights("CircularRR_AOPS_forward_model_weights.h5")
loaded_model.summary()

# Lower sample
result3 = pd.read_csv("CircularRR_AOPS_Fig_03bc_Lower_sample.csv", header=None)
result3 = result3.to_numpy()
result3 = result3.astype(np.float16)
x_test3 = result3[:,0:6]
y_test3 = result3[:,6]
x_test3 = sc.transform(x_test3)

# FDTD origin
result4 = pd.read_csv("CircularRR_AOPS_Fig_03bc_FDTD_origin.csv", header=None)
result4 = result4.to_numpy()
result4 = result4.astype(np.float16)
x_test4 = result4[:,0:6]
y_test4 = result4[:,6]
x_test4 = sc.transform(x_test4)
# Higher sample
result5 = pd.read_csv("CircularRR_AOPS_Fig_03bc_Higher_sample.csv", header=None)
result5 = result5.to_numpy()
result5 = result5.astype(np.float16)
x_test5 = result5[:,0:6]
y_test5 = result5[:,6]
x_test5 = sc.transform(x_test5)

# DL prediction
Pre4 = loaded_model.predict(x_test4)

# Plot all 4 curve
X= result4[:,0]
plt.plot(X, result4[:,6], linewidth=2, linestyle='-.', color=((255/255, 127/255, 14/255))) #DFTD
plt.plot(X,Pre4[:,0], linewidth=2, linestyle='--', color=((0/255, 114/255, 189/255)))      #DL
plt.plot(X,result3[:,6], linewidth=2, color=((126/255, 47/255, 142/255)))                  #Lower sample
plt.plot(X,result5[:,6], linewidth=2, linestyle=':', color=((119/255, 172/255, 48/255)))   #Higher sample
plt.xlabel('Wavelength(nm)', fontname='Times New Roman', fontsize=18)
plt.ylabel('Transmission', fontname='Times New Roman', fontsize=18)
plt.xticks(fontfamily='Times New Roman', fontsize=14)
plt.yticks(fontfamily='Times New Roman', fontsize=14)
plt.title('Comparing DL to FDTD for through port', loc='center', fontname='Times New Roman', fontsize=18)
font_prop = FontProperties(family="Times New Roman", size=16)
plt.legend(['FDTD', 'DL', 'Low Near', 'High Near'], prop=font_prop)
plt.show()