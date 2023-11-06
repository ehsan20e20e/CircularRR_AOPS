# CircularRR_AOPS

![CircularRR_AOPS4.gif](https://github.com/ehsan20e20e/CircularRR_AOPS/assets/106914575/ddbee65a-e3cb-4ef4-8759-ad03056f7023)

## Describtion
The provided repository showcases the application of deep learning techniques in predicting the spectral response of all-optical plasmonic switches. It is built upon the research presented in the paper titled "A deep learning method for empirical spectral prediction and inverse design of all-optical nonlinear plasmonic ring resonator switches".
This repository is specifically tailored for addressing inverse design challenges, with a specific focus on the fields of photonics and optics.
## Instructions
These instructions will guide you to set up and run a copy of the project on your local machine for development and testing purposes.
## Prerequisites
To execute the MATLAB and Python code, you will need to have MATLAB installed on your system. Specifically, we utilized MATLAB version R2023a, Python version 3.7.13, and Spyder version 5.1.5 within Anaconda version 4.14.0 for this code. Please note that while the project can be completed without these programs, the ability to compare speed and generate data will be limited unless MATLAB and Python are installed.
The required datasets for executing these codes can be accessed through the following link: https://drive.google.com/drive/folders/12n9jV9eL3ReEAF2YD4dCLRF0pCa51JTy?usp=drive_link.
## Geting started
In order to make use of this repository, it is essential to generate the required data for the all-optical switch structure using different FDTD (Finite-Difference Time-Domain) solvers, such as Lumerical, RSoft, or MATLAB. These solvers facilitate the generation and simulation of the optical switch structure, enabling the analysis of its performance and characteristics.

In this case, the raw data generated for the proposed plasmonic switch structure is available in the form of CSV files. These files have been provided to aid in the regeneration of the graphs and results that are presented in this article.

===> Please note that the data related to Drop port has been mistakenly entered as negative. Therefore, in the written code, we have taken the absolute value of the input data
### Forward model
To train the forward model, you can utilize the Python code provided in the 'CircularRR_AOPS_Forward_model.py' file. We have saved the 147,456 unique examples generated through FDTD simulations in the "result_V.csv" file. To execute the 'CircularRR_AOPS_Forward_model.py' file, you will require the 'result_H.csv' file, which constitutes big data with a size of 5.8 gigabytes.

The 'result_V.csv' file (7 parts) can be accessed through the following link: https://drive.google.com/drive/folders/12n9jV9eL3ReEAF2YD4dCLRF0pCa51JTy?usp=drive_link.

First part link: https://drive.google.com/file/d/1AcqJO9Qy34U64vmeluImQcEhMb7MNPGP/view?usp=drive_link.

second part link: https://drive.google.com/file/d/1IyZfRIT8rBBdbkuAULWjWX0sWpynGatL/view?usp=drive_link.

3th part link: https://drive.google.com/file/d/12sdaScipwbH1qMnLSl0erEOm6hB9HGLd/view?usp=drive_link.

4th part link: https://drive.google.com/file/d/1R9HOWI5C4JGDUw0pwZd9wpX3vV0L-06k/view?usp=drive_link.

5th part link: https://drive.google.com/file/d/1g7PXAXhSXLVsp41bHdyKxCvUy8YYXESo/view?usp=drive_link.

6th part link: https://drive.google.com/file/d/1L28Gezy-3qQvxwKAJYG5UH6XhgPf76eH/view?usp=drive_link.

7th oart link: https://drive.google.com/file/d/1kWqZg9hmLQG77qri3zCgIPGm32_gE_vK/view?usp=drive_link.

#### Figure 3
Figure 3a: The loss values after the completion of the training process will generate Figure 3a.

Figure 3b and 3c: To obtain Figures 3b and 3c, you can instruct the trained model to predict the output spectra for unseen geometric parameters at wavelengths ranging from 1000 to 1800 nm. In other words, you need to predict the transmission spectra for 800 different wavelengths to form the complete transmission spectrum. Then, compare this predicted spectrum with the spectrum obtained using the FDTD method. For the closest data, you would need to search for the closest data points to the selected geometric parameters in file "result_V.csv". 

For the purpose of easily reproducing the Figure 3b,c, we have stored the acquired data. Therefore, to test or use forward model, you can utilize the file "CircularRR_AOPS_Fig_03bc.py". The required data for running this file is stored in the file "CircularRR_AOPS_Fig_03bc_Lower_sample.csv", "CircularRR_AOPS_Fig_03bc_Higher_sample.csv", "CircularRR_AOPS_Fig_03bc_FDTD_origin.csv", "CircularRR_AOPS_forward_model.json" and "CircularRR_AOPS_forward_model_weights.h5" which have been loaded here.


### Inverse model
To train the inverse model, you can utilize the Python code provided in the 'CircularRR_AOPS_Inverse_model.py' file. We have saved the 147,456 unique examples generated through FDTD simulations in the "result_H.csv" file, which has been uploaded in the following link: https://drive.google.com/file/d/1XW8CZP60sRJwzeInc0dSmcq_Q4VMNfoE/view?usp=drive_link.

To execute the 'CircularRR_AOPS_Inverse_model.py' file, you will require the 'result_H.csv' file, which constitutes big data with a size of 1.8 gigabytes.

#### Figure 6
The loss values after the completion of the training process will generate Figure 6a.
To test invese model and to generate Figure 6b and c, it is necessary to juxtapose the data produced by the FDTD solver based on the geometric parameters derived from the inverse model with the provided geometric parameters. To test the inverse model and obtain the legend of Figure 6, you would need to feed the data generated by the FDTD solver as input to the inverse neural network model, specifically for the farthest data point from the training data. Then, you can obtain the output of the neural network model. Finally, in order to alleviate the error of the forward network, it is essential to obtain the transmission spectrum of the proposed structure using an FDTD solver.

Figure 6b and c:

step 1 (geometric parameter): For the purpose of easily reproducing the legend of Figure 6b and c, we have stored the acquired data. Therefore, to test or use inverse model, you can utilize the file "CircularRR_AOPS_Figure06.py". The required data for running this file is stored in the file "CircularRR_AOPS_Figure06_furthest_data.csv", "CircularRR_AOPS_inverse_model.json" and "CircularRR_AOPS_inverse_model_weights.h5" which have been loaded here.

step 2 (transmission spectra): For the purpose of easily reproducing the Figure 6b and c, we have stored the acquired data. Therefore, to regenerate the Figure 6b and c, you can utilize the file "CircularRR_AOPS_Fig_06bc.py". The required data for running this file is stored in the file "CircularRR_AOPS_Fig_06bc_furthest_predicted.csv" which have been loaded here.

### Supplementary Information 
#### Figure S1
to generate Figure S1, you can utilize the file "CircularRR_AOPS_S1_Fig_S01.m". The required data for running this file is stored in the file "Johnsonsilver.mat", which has been loaded here.

#### Figure S2
to generate Figure S2, you can utilize the file "CircularRR_AOPS_S2_Fig_S02.py". The required data for running this file is stored in the file "result_V.csv", which has been uploaded in the following link: https://drive.google.com/file/d/1XW8CZP60sRJwzeInc0dSmcq_Q4VMNfoE/view?usp=drive_link.

#### Figure S3
Figure S3a: To plot a three-dimensional bar chart of The computational cost, you would need to vary the number of layers and the number of neurons each time and record the training time. For the purpose of easily reproducing the plot, we have stored the acquired data. Therefore, to generate Figure S3a, you can utilize the file "CircularRR_AOPS_S3_Fig_S03a.m".

Figure S3b: To obtain Figure S3b, you can keep the number of neurons fixed at 60 and the number of layers fixed at 6 and then you would need to vary the number of epochs. For the purpose of easily reproducing the plot, we have stored the acquired data. Therefore, to generate Figure S3b, you can utilize the file "CircularRR_AOPS_S3_Fig_S03b.m".

#### Figure S5
To plot Figure S5, you would need to vary the number of layers and the number of neurons each time and record the loss value. For the purpose of easily reproducing the plot, we have stored the acquired data. Therefore, to generate Figure S5, you can utilize the file "CircularRR_AOPS_S4_Fig_S05.py". The required data for running this file is stored in the file "CircularRR_AOPS_S4_Fig_S05.csv", which has been loaded here.

#### Figure S6
To plot Figure S6, you would need to vary the number of layers each time and after training the network, use it to predict the transmission spectrum of a structure with specific geometric parameters that the network has not seen before. In this paper, for Figure S6, we considered g1=g2=g3=45nm and g4=g5=20nm, and compared the predicted spectrum with the spectrum obtained from the Finite-Difference Time-Domain (FDTD) method.

For the purpose of easily reproducing the plot, we have stored the acquired data. Therefore, to generate Figure S6, you can utilize the file "CircularRR_AOPS_S2_Fig_S06.py". The required data for running this file is stored in the file "CircularRR_AOPS_S2_Fig_S06.csv", which has been loaded here.



