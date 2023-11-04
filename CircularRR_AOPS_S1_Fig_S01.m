%The code for the research presented in the paper titled "A deep learning method for empirical spectral prediction and inverse design of all-optical nonlinear plasmonic ring resonator switches
%@authors: Ehsan Adibnia, Majid Ghadrdan and Mohammad Ali Mansouri-Birjandi
%Corresponding author: mansouri@ece.usb.ac.ir
%This code is corresponding to the complex refractive index for silver obtained from Johnson and Cristy.
%This code regenerates the Fig S1 of the Supplementary Information of the paper.
%Please cite the paper in any publication using this code.
%% =======================================================================
clc
close all
clear
%%% load dirty data (predicted)
load Johnsonsilver.mat
figure(1)
yyaxis left
plot(Johnsonsilver(1:48,1),Johnsonsilver(1:48,2),'linewidth',2) % plot the transmition spectrum
hold on
ylabel('Real part (blue solid)')
yyaxis right
plot(Johnsonsilver(1:48,1),Johnsonsilver(1:48,3),'linewidth',2, LineStyle='--') % plot the transmition spectrum
ylabel('Imaginary part (red dashed)')
xlabel('Wavelength(nm)')
get(gca,'fontname')  
set(gca,'fontname','times','fontweight','normal') 
set(gca,'fontsize',18)
set(gca,'linewidth',0.85)
title('complex refractive index','fontweight','normal')
grid off