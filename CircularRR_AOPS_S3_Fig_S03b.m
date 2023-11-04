%The code for the research presented in the paper titled "A deep learning method for empirical spectral prediction and inverse design of all-optical nonlinear plasmonic ring resonator switches
%@authors: Ehsan Adibnia, Majid Ghadrdan and Mohammad Ali Mansouri-Birjandi
%Corresponding author: mansouri@ece.usb.ac.ir
%This code is corresponding to the Forward Deep Neural Network (DNN) section of the article.
%This code regenerates the Fig S3b of the Supplementary Information of the paper.
%Please cite the paper in any publication using this code.
%% =======================================================================
clc;
clear all;
% epochs
x = [1 1000 2000 3000 4000 5000];
% computational cost 
y = [380 400 440 540 590 620];
sizes = [80, 80, 80, 80, 80, 80];
coefficients = polyfit(x, y, 8); 
fitted_values = polyval(coefficients, x);  
plot(x, fitted_values, '--','color', 'red', 'linewidth', 2.5)
hold on
scatter(x, y, sizes, 'filled', 'MarkerFaceColor', 'blue', 'linewidth', 2.85 )
ylabel('Computational cost (Sec)');
xlabel('Epochs');
zlabel('Computational cost (Sec)');
title('Computational cost at Neurons=60 and Layers=6', 'FontWeight', 'normal')
get(gca,'fontname')
set(gca,'fontname','times')
set(gca,'fontsize',18)
set(gca,'linewidth',0.85)
grid off