"""
The code for the research presented in the paper titled "A deep learning method for empirical spectral prediction and inverse design of all-optical nonlinear plasmonic ring resonator switches

@authors: Ehsan Adibnia, Majid Ghadrdan and Mohammad Ali Mansouri-Birjandi
Corresponding author: mansouri@ece.usb.ac.ir

This code is corresponding to the Forward Deep Neural Network (DNN) section of the article.
This code regenerates the Fig S6a-n of the Supplementary Information of the paper.
Please cite the paper in any publication using this code.
"""
import matplotlib.pyplot as plt 
import pandas as pd 
from matplotlib.font_manager import FontProperties

Loss = pd.read_csv("CircularRR_AOPS_S2_Fig_S06.csv")
Loss=Loss.to_numpy()

# fig S6m
plt.plot(Loss[:,0],Loss[:,6], linewidth=2, color=((255/255, 127/255, 14/255))) 
plt.plot(Loss[:,0],Loss[:,22], linewidth=2, color=((0/255, 114/255, 189/255)), linestyle='--') 
plt.title('NN with 12 hidden layers for through port analysis', fontname='Times New Roman', fontsize=16, loc='center')
plt.xlabel('Wavelength(nm)', fontname='Times New Roman', fontsize=18)
plt.ylabel('Transmission', fontname='Times New Roman', fontsize=18)
plt.xticks(fontfamily='Times New Roman', fontsize=16)
plt.yticks(fontfamily='Times New Roman', fontsize=16)
font_prop = FontProperties(family="Times New Roman", size=16)
plt.show()

# fig S6k
plt.plot(Loss[:,0],Loss[:,6], linewidth=2, color=((255/255, 127/255, 14/255))) 
plt.plot(Loss[:,0],Loss[:,20], linewidth=2, color=((0/255, 114/255, 189/255)), linestyle='--') 
plt.title('NN with 6 hidden layers for through port analysis', fontname='Times New Roman', fontsize=16, loc='center')
plt.xlabel('Wavelength(nm)', fontname='Times New Roman', fontsize=18)
plt.ylabel('Transmission', fontname='Times New Roman', fontsize=18)
plt.xticks(fontfamily='Times New Roman', fontsize=16)
plt.yticks(fontfamily='Times New Roman', fontsize=16)
font_prop = FontProperties(family="Times New Roman", size=16)
plt.show()

# fig S6i
plt.plot(Loss[:,0],Loss[:,6], linewidth=2, color=((255/255, 127/255, 14/255))) 
plt.plot(Loss[:,0],Loss[:,18], linewidth=2, color=((0/255, 114/255, 189/255)), linestyle='--') 
plt.title('NN with 5 hidden layers for through port analysis', fontname='Times New Roman', fontsize=16, loc='center')
plt.xlabel('Wavelength(nm)', fontname='Times New Roman', fontsize=18)
plt.ylabel('Transmission', fontname='Times New Roman', fontsize=18)
plt.xticks(fontfamily='Times New Roman', fontsize=16)
plt.yticks(fontfamily='Times New Roman', fontsize=16)
font_prop = FontProperties(family="Times New Roman", size=16)
plt.show()

# fig S6g
plt.plot(Loss[:,0],Loss[:,6], linewidth=2, color=((255/255, 127/255, 14/255))) 
plt.plot(Loss[:,0],Loss[:,16], linewidth=2, color=((0/255, 114/255, 189/255)), linestyle='--') 
plt.title('NN with 4 hidden layers for through port analysis', fontname='Times New Roman', fontsize=16, loc='center')
plt.xlabel('Wavelength(nm)', fontname='Times New Roman', fontsize=18)
plt.ylabel('Transmission', fontname='Times New Roman', fontsize=18)
plt.xticks(fontfamily='Times New Roman', fontsize=16)
plt.yticks(fontfamily='Times New Roman', fontsize=16)
font_prop = FontProperties(family="Times New Roman", size=16)
plt.show()

# fig S6e
plt.plot(Loss[:,0],Loss[:,6], linewidth=2, color=((255/255, 127/255, 14/255))) 
plt.plot(Loss[:,0],Loss[:,14], linewidth=2, color=((0/255, 114/255, 189/255)), linestyle='--') 
plt.title('NN with 3 hidden layers for through port analysis', fontname='Times New Roman', fontsize=16, loc='center')
plt.xlabel('Wavelength(nm)', fontname='Times New Roman', fontsize=18)
plt.ylabel('Transmission', fontname='Times New Roman', fontsize=18)
plt.xticks(fontfamily='Times New Roman', fontsize=16)
plt.yticks(fontfamily='Times New Roman', fontsize=16)
font_prop = FontProperties(family="Times New Roman", size=16)
plt.show()

# fig S6c
plt.plot(Loss[:,0],Loss[:,6], linewidth=2, color=((255/255, 127/255, 14/255))) 
plt.plot(Loss[:,0],Loss[:,12], linewidth=2, color=((0/255, 114/255, 189/255)), linestyle='--') 
plt.title('NN with 2 hidden layers for through port analysis', fontname='Times New Roman', fontsize=16, loc='center')
plt.xlabel('Wavelength(nm)', fontname='Times New Roman', fontsize=18)
plt.ylabel('Transmission', fontname='Times New Roman', fontsize=18)
plt.xticks(fontfamily='Times New Roman', fontsize=16)
plt.yticks(fontfamily='Times New Roman', fontsize=16)
font_prop = FontProperties(family="Times New Roman", size=16)
plt.show()

# fig S6a
plt.plot(Loss[:,0],Loss[:,6], linewidth=2, color=((255/255, 127/255, 14/255))) 
plt.plot(Loss[:,0],Loss[:,10], linewidth=2, color=((0/255, 114/255, 189/255)), linestyle='--') 
plt.title('NN with 1 hidden layers for through port analysis', fontname='Times New Roman', fontsize=16, loc='center')
plt.xlabel('Wavelength(nm)', fontname='Times New Roman', fontsize=18)
plt.ylabel('Transmission', fontname='Times New Roman', fontsize=18)
plt.xticks(fontfamily='Times New Roman', fontsize=16)
plt.yticks(fontfamily='Times New Roman', fontsize=16)
font_prop = FontProperties(family="Times New Roman", size=16)
plt.show()

# fig S6n
plt.plot(Loss[:,0],Loss[:,7], linewidth=2, color=((255/255, 127/255, 14/255))) 
plt.plot(Loss[:,0],Loss[:,21], linewidth=2, color=((0/255, 114/255, 189/255)), linestyle='--') 
plt.title('NN with 12 hidden layers for drop port analysis', fontname='Times New Roman', fontsize=16, loc='center')
plt.xlabel('Wavelength(nm)', fontname='Times New Roman', fontsize=18)
plt.ylabel('Transmission', fontname='Times New Roman', fontsize=18)
plt.xticks(fontfamily='Times New Roman', fontsize=16)
plt.yticks(fontfamily='Times New Roman', fontsize=16)
font_prop = FontProperties(family="Times New Roman", size=16)
plt.show()

# fig S6l
plt.plot(Loss[:,0],Loss[:,7], linewidth=2, color=((255/255, 127/255, 14/255))) 
plt.plot(Loss[:,0],Loss[:,19], linewidth=2, color=((0/255, 114/255, 189/255)), linestyle='--') 
plt.title('NN with 6 hidden layers for drop port analysis', fontname='Times New Roman', fontsize=16, loc='center')
plt.xlabel('Wavelength(nm)', fontname='Times New Roman', fontsize=18)
plt.ylabel('Transmission', fontname='Times New Roman', fontsize=18)
plt.xticks(fontfamily='Times New Roman', fontsize=16)
plt.yticks(fontfamily='Times New Roman', fontsize=16)
font_prop = FontProperties(family="Times New Roman", size=16)
plt.show()

# fig S6j
plt.plot(Loss[:,0],Loss[:,7], linewidth=2, color=((255/255, 127/255, 14/255))) 
plt.plot(Loss[:,0],Loss[:,17], linewidth=2, color=((0/255, 114/255, 189/255)), linestyle='--') 
plt.title('NN with 5 hidden layers for drop port analysis', fontname='Times New Roman', fontsize=16, loc='center')
plt.xlabel('Wavelength(nm)', fontname='Times New Roman', fontsize=18)
plt.ylabel('Transmission', fontname='Times New Roman', fontsize=18)
plt.xticks(fontfamily='Times New Roman', fontsize=16)
plt.yticks(fontfamily='Times New Roman', fontsize=16)
font_prop = FontProperties(family="Times New Roman", size=16)
plt.show()

# fig Sh
plt.plot(Loss[:,0],Loss[:,7], linewidth=2, color=((255/255, 127/255, 14/255))) 
plt.plot(Loss[:,0],Loss[:,15], linewidth=2, color=((0/255, 114/255, 189/255)), linestyle='--') 
plt.title('NN with 4 hidden layers for drop port analysis', fontname='Times New Roman', fontsize=16, loc='center')
plt.xlabel('Wavelength(nm)', fontname='Times New Roman', fontsize=18)
plt.ylabel('Transmission', fontname='Times New Roman', fontsize=18)
plt.xticks(fontfamily='Times New Roman', fontsize=16)
plt.yticks(fontfamily='Times New Roman', fontsize=16)
font_prop = FontProperties(family="Times New Roman", size=16)
plt.show()

# fig S6f
plt.plot(Loss[:,0],Loss[:,7], linewidth=2, color=((255/255, 127/255, 14/255))) 
plt.plot(Loss[:,0],Loss[:,13], linewidth=2, color=((0/255, 114/255, 189/255)), linestyle='--') 
plt.title('NN with 3 hidden layers for drop port analysis', fontname='Times New Roman', fontsize=16, loc='center')
plt.xlabel('Wavelength(nm)', fontname='Times New Roman', fontsize=18)
plt.ylabel('Transmission', fontname='Times New Roman', fontsize=18)
plt.xticks(fontfamily='Times New Roman', fontsize=16)
plt.yticks(fontfamily='Times New Roman', fontsize=16)
font_prop = FontProperties(family="Times New Roman", size=16)
plt.show()

# fig S6d
plt.plot(Loss[:,0],Loss[:,7], linewidth=2, color=((255/255, 127/255, 14/255))) 
plt.plot(Loss[:,0],Loss[:,11], linewidth=2, color=((0/255, 114/255, 189/255)), linestyle='--') 
plt.title('NN with 2 hidden layers for drop port analysis', fontname='Times New Roman', fontsize=16, loc='center')
plt.xlabel('Wavelength(nm)', fontname='Times New Roman', fontsize=18)
plt.ylabel('Transmission', fontname='Times New Roman', fontsize=18)
plt.xticks(fontfamily='Times New Roman', fontsize=16)
plt.yticks(fontfamily='Times New Roman', fontsize=16)
font_prop = FontProperties(family="Times New Roman", size=16)
plt.show()

# fig S6b
plt.plot(Loss[:,0],Loss[:,7], linewidth=2, color=((255/255, 127/255, 14/255))) 
plt.plot(Loss[:,0],Loss[:,9], linewidth=2, color=((0/255, 114/255, 189/255)), linestyle='--') 
plt.title('NN with 1 hidden layers for drop port analysis', fontname='Times New Roman', fontsize=16, loc='center')
plt.xlabel('Wavelength(nm)', fontname='Times New Roman', fontsize=18)
plt.ylabel('Transmission', fontname='Times New Roman', fontsize=18)
plt.xticks(fontfamily='Times New Roman', fontsize=16)
plt.yticks(fontfamily='Times New Roman', fontsize=16)
font_prop = FontProperties(family="Times New Roman", size=16)
plt.show()