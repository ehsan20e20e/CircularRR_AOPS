%The code for the research presented in the paper titled "A deep learning method for empirical spectral prediction and inverse design of all-optical nonlinear plasmonic ring resonator switches
%@authors: Ehsan Adibnia, Majid Ghadrdan and Mohammad Ali Mansouri-Birjandi
%Corresponding author: mansouri@ece.usb.ac.ir
%This code is corresponding to the Forward Deep Neural Network (DNN) section of the article.
%This code regenerates the Fig S3a of the Supplementary Information of the paper.
%Please cite the paper in any publication using this code.
%% =======================================================================
clc;
clear all;
y = [1 2 3 4 5 6 7];
% computational cost 
z = [25 90 180 280 480;
      40 100 200 300 500;
      60 120 240 340 540;
      85 150 340 440 640;
      120 195 390 490 690;
     150 230 420 600 720;
      190 300 520 690 940];
ylabels = {'1 layer', '2 layers', '3 layers', '4 layers', '5 layers', '6 layers', '12 layers'}; 
xlabels = {'1 neuron', '5 neurons', '10 neurons', '30 neurons', '60 neurons'}; 
bar3(y, z);
numBars = size(z, 2);
numBars2 = size(z, 1);
xpos = repmat(1:numBars, numel(y), 1);
set(gca, 'xtick', 1:numBars, 'xticklabel', xlabels);
set(gca, 'ytick', 1:numBars2, 'yticklabel', ylabels);
ylabel('Numbers of hidden layers');
xlabel('Numbers of neurons');
zlabel('Computational cost (Sec)');
title('Analysis of computational cost', 'FontWeight', 'normal')
get(gca,'fontname')  
set(gca,'fontname','times')  
set(gca,'fontsize',18)
set(gca,'linewidth',0.85)
grid on