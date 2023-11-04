# -*- coding: utf-8 -*-
"""
The code for the research presented in the paper titled "A deep learning method for empirical spectral prediction and inverse design of all-optical nonlinear plasmonic ring resonator switches

@authors: Ehsan Adibnia, Majid Ghadrdan and Mohammad Ali Mansouri-Birjandi
Corresponding author: mansouri@ece.usb.ac.ir

This code is corresponding to the Inverse Deep Neural Network (DNN) section of the article.
Please cite the paper in any publication using this code.
"""
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import csv
from keras.models import Sequential 
from keras.layers import Dense
from keras.layers import LeakyReLU
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.optimizers import Adadelta

### Load the data from CSV file (the results of FDTD solver)
result = pd.read_csv("result_H.csv", header=None)
result = result.to_numpy()
result=result.astype(np.float16)

x = abs(result[0:result.shape[0],0:1600])
y = result[0:result.shape[0],1600:1606]

# Allocation of 70% of the total data to the training data
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.30, shuffle='true')
# Allocation of 50% of the remaining data to the validateion data and 50% to the test data (15% validation and 15% test of total)
x_test, x_val, y_test, y_val = train_test_split(x_val, y_val, test_size=0.50, shuffle='true')

### Feature Scaling
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_val = sc.transform(x_val)
x_test = sc.transform(x_test)

### Defining the Layers of the deep neural network (DNN)
# 6 hidden layer and 60 neurons in each layer
# Slope of 0.2 has been set for the Leaky ReLU
# Input consist of 1600 point of transmission spectrum (800 point for through port and 800 point for drop port)
# Output consist of 5 geometric parameter of all-optical plasmonic switch (AOPS)
Model = Sequential()
Model.add(Dense(60, input_dim=1600))
Model.add((LeakyReLU(alpha=0.2)))
Model.add(Dense(60))
Model.add((LeakyReLU(alpha=0.2)))
Model.add(Dense(60))
Model.add((LeakyReLU(alpha=0.2)))
Model.add(Dense(60))
Model.add((LeakyReLU(alpha=0.2)))
Model.add(Dense(60))
Model.add((LeakyReLU(alpha=0.2)))
Model.add(Dense(60))
Model.add((LeakyReLU(alpha=0.2)))
Model.add(Dense(5))
Model.summary()

### Configuring the settings of the training procedure 
# Mean Squared Logarithmic Error (MSLE) function has been used for loss estimation
# AdaDelta Optimizer has been used and learning rate of 0.1 has been set 
Model.compile(loss='mean_squared_logarithmic_error',
              optimizer= Adadelta(learning_rate=0.1))

### Training Model 
# batch size of 80 was set and 5000 epochs were performed
history = Model.fit(x_train, y_train, epochs=5000,
          batch_size = 80, validation_data=(x_val, y_val))

### plot the loss graph
plt.plot(history.history['val_loss'], linewidth=1)
plt.plot(history.history['loss'], linewidth=2, linestyle='--')
plt.title('The loss of training model', fontname='Times New Roman', fontsize=18, loc='center')
plt.xlabel('epochs', fontname='Times New Roman', fontsize=18)
plt.ylabel('loss', fontname='Times New Roman', fontsize=18)
plt.xticks(fontfamily='Times New Roman', fontsize=14)
plt.yticks(fontfamily='Times New Roman', fontsize=14)
plt.legend(['train', 'Validation', 'test'])
plt.show()

### loss value of train and validation data
train_loss = history.history['loss']
val_loss = history.history['val_loss']

### Testing Model 
predictions = Model.predict(x_test)
Loss = Model.evaluate(x_test, y_test)
print(Loss)

# save the loss values in csv file
fieldnames = ['Epoch', 'Training Loss', 'Validation Loss']
with open('E:/Education/Electronic/01-PHD/python Code/loss.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for epoch, train_loss_value, val_loss_value in zip(range(1, len(train_loss) + 1), train_loss, val_loss):
        writer.writerow({'Epoch': epoch, 'Training Loss': train_loss_value, 'Validation Loss': val_loss_value})

# save the inverse model and its weights
model_json = Model.to_json()
json_file = open("T-shaped switchat_model_inverse.json", "w")
json_file.write(model_json)   
Model.save_weights("T-shaped switch_Nozhat_model_weights_inverse.h5")
json_file.close()
