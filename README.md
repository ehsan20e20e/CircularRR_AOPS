# CircularRR_AOPS
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
### Inverse model
"To train the inverse model, you can utilize the Python code provided in the 'CircularRR_AOPS_Inverse_model.py' file. We have saved the 147,456 unique examples generated through FDTD simulations in the 'result_H.csv' file, which has been uploaded in the following link: https://drive.google.com/file/d/1XW8CZP60sRJwzeInc0dSmcq_Q4VMNfoE/view?usp=drive_link.
To execute the 'CircularRR_AOPS_Inverse_model.py' file, you will require the 'result_H.csv' file, which constitutes big data with a size of 1.8 gigabytes".

#### Figure 6
The loss values after the completion of the training process will generate Figure 6a.
To generate Figure 6b and c, it is necessary to juxtapose the data produced by the FDTD solver based on the geometric parameters derived from the inverse model with the provided geometric parameters






