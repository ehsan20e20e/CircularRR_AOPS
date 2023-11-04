"""
The code for the research presented in the paper titled "A deep learning method for empirical spectral prediction and inverse design of all-optical nonlinear plasmonic ring resonator switches

@authors: Ehsan Adibnia, Majid Ghadrdan and Mohammad Ali Mansouri-Birjandi
Corresponding author: mansouri@ece.usb.ac.ir

This code is corresponding to the Inverse Deep Neural Network (DNN) section of the article.
This code regenerates the legend of Fig 6a,b of the paper.
Please cite the paper in any publication using this code.
"""

import numpy as np
import keras
import pandas as pd 
from sklearn.preprocessing import StandardScaler

result = pd.read_csv("result_H.csv", header=None)
result = result.to_numpy()
result = result.astype(np.float16)

x_train = result[0:result.shape[0],0:1600]
y_train = result[0:result.shape[0],1600:1606]

sc = StandardScaler()
x_train = sc.fit_transform(x_train)

x_test = result[50000:50001,0:1600]
y_test = result[50000:50001,1600:1606]

x_testO = sc.transform(x_test)

result2 = pd.read_csv("CircularRR_AOPS_Figure06_furthest_data.csv", header=None)
result2 = result2.to_numpy()
result2 = result2.astype(np.float16)
x_test2 = result2[:,0:1600]
y_test2 = result2[:,1600:1606]
x_test2 = sc.transform(x_test2)


json_file = open("CircularRR_AOPS_inverse_model.json", "r")
loaded_model_json = json_file.read()
json_file.close()
loaded_model = keras.models.model_from_json(loaded_model_json)
loaded_model.load_weights("CircularRR_AOPS_inverse_model_weights.h5")

loaded_model.summary()
Pre = loaded_model.predict(x_testO)
Pre2 = loaded_model.predict(x_test2)

print(Pre2)
print(y_test2)