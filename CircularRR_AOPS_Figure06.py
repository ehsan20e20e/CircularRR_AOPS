# -*- coding: utf-8 -*-
"""
The code for the research presented in the paper titled "A deep learning method for empirical spectral prediction and inverse design of all-optical nonlinear plasmonic ring resonator switches

@authors: Ehsan Adibnia, Majid Ghadrdan and Mohammad Ali Mansouri-Birjandi
Corresponding author: mansouri@ece.usb.ac.ir

This code is coresponding to the Inverse Deep Neural Network (DNN) section of the acticle.
This code regenerates the Fig 6b and Fig 6c of the paper.
Please cite the paper in any publication using this code.
"""
import matplotlib.pyplot as plt 
import pandas as pd 
from matplotlib.font_manager import FontProperties

lum = pd.read_csv("inverse_test.csv", header=None)
g = "\u00D7"
lum=lum.to_numpy()

plt.plot(lum[1:800,0],lum[1:800,6], linewidth=2, color='#ff7f0e')
plt.plot(lum[1:800,0],lum[1:800,13], linewidth=2, linestyle='--', color='#1f77b4')
plt.title('Results of inverse design for through port', fontname='Times New Roman', fontsize=18, loc='center')
plt.xlabel('Wavelength (nm)', fontname='Times New Roman', fontsize=18)
plt.ylabel('Transmission', fontname='Times New Roman', fontsize=18)
plt.xticks(fontfamily='Times New Roman', fontsize=14)
plt.yticks(fontfamily='Times New Roman', fontsize=14)
font_prop = FontProperties(family="Times New Roman", size=14)
plt.legend(['Desierd (49,37,43,18,22)', 'DL (57,38,43,15,21)'], prop=font_prop)
plt.show()

plt.plot(lum[1:800,0],lum[1:800,7], linewidth=2, color='#ff7f0e')
plt.plot(lum[1:800,0],lum[1:800,14], linewidth=2, linestyle='--', color='#1f77b4')
plt.title('Results of inverse design for drop port', fontname='Times New Roman', fontsize=18, loc='center')
plt.xlabel('Wavelength (nm)', fontname='Times New Roman', fontsize=18)
plt.ylabel('Transmission', fontname='Times New Roman', fontsize=18)
plt.xticks(fontfamily='Times New Roman', fontsize=14)
plt.yticks(fontfamily='Times New Roman', fontsize=14)
plt.legend(['Desierd (49,37,43,18,22)', 'DL (57,38,43,15,21)'], prop=font_prop)
plt.show()