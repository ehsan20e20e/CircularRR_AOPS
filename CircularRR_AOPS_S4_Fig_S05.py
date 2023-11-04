"""
The code for the research presented in the paper titled "A deep learning method for empirical spectral prediction and inverse design of all-optical nonlinear plasmonic ring resonator switches

@authors: Ehsan Adibnia, Majid Ghadrdan and Mohammad Ali Mansouri-Birjandi
Corresponding author: mansouri@ece.usb.ac.ir

This code is corresponding to the Inverse Deep Neural Network (DNN) section of the article.
This code regenerates the Fig S5a and S5b of the Supplementary Information of the paper.
Please cite the paper in any publication using this code.
"""
import matplotlib.pyplot as plt 
import pandas as pd 
from matplotlib.font_manager import FontProperties

Loss = pd.read_csv("CircularRR_AOPS_S4_Fig_S05.csv")
Loss=Loss.to_numpy()
g = "\u00D7"

# plot Fig S5a
plt.plot(Loss[1:5000,0],Loss[1:5000,5], linewidth=1, color=((255/255, 127/255, 14/255))) #orange 1 layer
plt.plot(Loss[1:5000,0],Loss[1:5000,6], linewidth=1, color=((119/255, 172/255, 48/255))) #green 2 layers
plt.plot(Loss[1:5000,0],Loss[1:5000,7], linewidth=1, color=((126/255, 47/255, 142/255))) #violet 3 layers
plt.plot(Loss[1:5000,0],Loss[1:5000,8], linewidth=1, color=((237/255, 177/255, 32/255))) #Yellow 4 layers
plt.plot(Loss[1:5000,0],Loss[1:5000,9], linewidth=1, color=((255/255, 0/255, 0/255)))    #Red 5 layers
plt.plot(Loss[1:5000,0],Loss[1:5000,4], linewidth=1, color=((0/255, 114/255, 189/255)))   #Blue 5 layers
plt.plot(Loss[1:5000,0],Loss[1:5000,10], linewidth=1, color=((0/255, 0/255, 0/255)))      #Blue 5 layers
plt.title('The validation error of training forward model', fontname='Times New Roman', fontsize=18, loc='center')
plt.xlabel('Epochs', fontname='Times New Roman', fontsize=18)
plt.ylabel('Loss'+' ('+g+'10 ^3)', fontname='Times New Roman', fontsize=18)
plt.xticks(fontfamily='Times New Roman', fontsize=14)
plt.yticks(fontfamily='Times New Roman', fontsize=14)
font_prop = FontProperties(family="Times New Roman", size=14)
plt.legend([ '1 Hidden layer','2 Hidden layers','3 Hidden layers','4 Hidden layers','5 Hidden layers','6 Hidden layers','12 Hidden layers'], prop=font_prop)
plt.show()

# plot Fig S5b
plt.plot(Loss[1:5000,0],Loss[1:5000,20], linewidth=1, color=((255/255, 127/255, 14/255))) #orange 1 neuron
plt.plot(Loss[1:5000,0],Loss[1:5000,22], linewidth=1, color=((119/255, 172/255, 48/255))) #green 5 neurons
plt.plot(Loss[1:5000,0],Loss[1:5000,23], linewidth=1, color=((126/255, 47/255, 142/255))) #violet 10 neurons
plt.plot(Loss[1:5000,0],Loss[1:5000,24], linewidth=1, color=((237/255, 177/255, 32/255))) #yellow 30 neurons
plt.plot(Loss[1:5000,0],Loss[1:5000,4], linewidth=1, color=((0/255, 114/255, 189/255)))   #blue 60 neurons
plt.title('The validation error of training forward model', fontname='Times New Roman', fontsize=18, loc='center')
plt.xlabel('Epochs', fontname='Times New Roman', fontsize=18)
plt.ylabel('Loss'+' ('+g+'10 ^3)', fontname='Times New Roman', fontsize=18)
plt.xticks(fontfamily='Times New Roman', fontsize=14)
plt.yticks(fontfamily='Times New Roman', fontsize=14)
plt.legend([ '1 Neuron','5 Neurons','10 Neurons','30 Neurons','60 Neurons'], prop=font_prop)
plt.show()