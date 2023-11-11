%The code for the research presented in the paper titled "A deep learning method for empirical spectral prediction and inverse design of all-optical nonlinear plasmonic ring resonator switches
%@authors: Ehsan Adibnia, Majid Ghadrdan and Mohammad Ali Mansouri-Birjandi
%Corresponding author: mansouri@ece.usb.ac.ir
% In this code, first and second-order derivative of transmission spectrum versus wavelength, will be calculated.
% In this code, local minima and maxima will be calculated..
% In this code, we proposed an algorithm to find optimal point for switching application.
%This code regenerates the Fig S7 of the Supplementary Information of the paper.
%Please cite the paper in any publication using this code.
%% =======================================================================
clc
close all
clear
%%% load dirty data (predicted)
load dataset_T-shape3.mat
%%% initialization: the assignment of an initial value for a data object or variable.
Length=800*9216; % total number of rows (total number of data)
n_WL=800; % number of WaveLength points at each spectrum (simulation)
n_S=Length/n_WL; % number of spectrum (simulation)

%%% Create clean data
input=NaN(Length,15);
%%% copy output dataset to input(column 2 to 10) matrix for matlab. {in this problem we use the first column for feauture dataset! (easy plot and ...}
input(1:Length,1)=datasetTshape3(2:Length+1,2); % wavelength (feature)
input(1:Length,2)=datasetTshape3(2:Length+1,8); % first output (output)
input(1:Length,3)=datasetTshape3(2:Length+1,9); % second output (output)
%%% copy feature of dataset to input(column 11 to inf) matrix for matlab
input(1:Length,11)=datasetTshape3(2:Length+1,3); % W_input (feature)
input(1:Length,12)=datasetTshape3(2:Length+1,4); % W_output (feature)
input(1:Length,13)=datasetTshape3(2:Length+1,5); % W_rect (feature)
input(1:Length,14)=datasetTshape3(2:Length+1,6); % G_input (feature)
input(1:Length,15)=datasetTshape3(2:Length+1,7); % G_output (feature)

%% ===================================================================
% copy input data for calculis and process steps as following:
% copy transmition spectrum of first waveguide (through)(column 2) to "Process_Data1"
% copy transmition spectrum of second waveguide (drop)(column 3) to "Process_Data2"
Process_Data1=NaN(Length,15);
Process_Data1(1:Length,1:2)=input(1:Length,1:2);
Process_Data1(1:Length,11:15)=input(1:Length,11:15);
%
Process_Data2=NaN(Length,15);
Process_Data2(1:Length,1)=input(1:Length,1);
Process_Data2(1:Length,2)=input(1:Length,3);
Process_Data2(1:Length,11:15)=input(1:Length,11:15);
%% ===================================================================
%%      ==> second waveguide (drop) (Process_Data2) <==
%% ===================================================================
% column 3 of Process_Data2 = first-order derivative
% column 4 of Process_Data2 = second-order derivative
for j=0:n_S-1
Process_Data2(2+(j*n_WL):(n_WL-1)+(j*n_WL),3)=(Process_Data2(3+(j*n_WL):(n_WL)+(j*n_WL),2)-Process_Data2(1+(j*n_WL):(n_WL-2)+(j*n_WL),2))./...
    (Process_Data2(3+(j*n_WL):(n_WL)+(j*n_WL),1)-Process_Data2(1+(j*n_WL):(n_WL-2)+(j*n_WL),1)); % calculate of first-order derivative and save in 3rd column
Process_Data2(2+(j*n_WL):(n_WL-1)+(j*n_WL),4)=(Process_Data2(3+(j*n_WL):(n_WL)+(j*n_WL),3)-Process_Data2(1+(j*n_WL):(n_WL-2)+(j*n_WL),3))./...
    (Process_Data2(3+(j*n_WL):(n_WL)+(j*n_WL),1)-Process_Data2(1+(j*n_WL):(n_WL-2)+(j*n_WL),1)); %calculate of second-order derivative and save in 3rd column
Process_Data2(2+2+(j*n_WL):(n_WL-1)+(j*n_WL)-2,5)=Process_Data2(2+2+(j*n_WL):(n_WL-1)+(j*n_WL)-2,4);
end
%%
%%% finding of Local Maximum and minimum of drop spectrum
Max_Through=[]; % Local Maximum of drop spectrum
pkss=[]; % peaks of each spectrum in following loop (not matter)
id_MT=[]; % id of Local Maximum of drop spectrum
d=[]; % coresponding features

%%% finding of Local Minimum of drop spectrum
Min_Through=[]; % Local minimum of drop spectrum
pkss1=[]; % peaks of each spectrum in following loop (not matter)
id_MT1=[]; % id of Local Minimum of drop spectrum
d1=[]; % coresponding features

%%% finding of Local Maximum of second-order derivative of drop transmition <===> minimum of drop spectrum
Max_Through2=[]; % Local Maximum of second-order derivative of drop transmition <===> minimum of drop spectrum
pkss2=[]; % peaks of each spectrum in following loop (not matter)
id_MT2=[]; % id of Local Maximum of second-order derivative of drop spectrum
d2=[]; % coresponding features

for j=0:n_S-1
    %%% finding of Local Maximum of drop spectrum
[pks,locs] = findpeaks(Process_Data2(1+(j*n_WL):n_WL+(j*n_WL),2),Process_Data2(1+(j*n_WL):n_WL+(j*n_WL),1)); % finding Local Maximum of drop spectrum and theirs locations
[numRows,numCols] = size(pks); % number of Local Maximum in each spectrum (in each loop)
id_MT(1:numRows,1)=j; % number of spectrum (loop)
d(1:numRows,1:5)=Process_Data2(locs-1000+(j*n_WL),11:15);
pkss=[id_MT(:,1),locs(:,1),pks(:,1),d(:,1:5)]; % concatinating of above matrix
Max_Through=[Max_Through;pkss]; % concatinating of peaks of each spectrum to achieve Local Maximum of drop spectrum
id_MT=[];
d=[];

    %%% finding of Local minimum of drop spectrum
DataInv = 1.01*max(Process_Data2(:,2)) - Process_Data2(:,2);
[pks1,locs1] = findpeaks(DataInv(1+(j*n_WL):n_WL+(j*n_WL),1),Process_Data2(1+(j*n_WL):n_WL+(j*n_WL),1));
[numRows1,numCols1] = size(pks1); % number of Local Maximum in each spectrum (in each loop)
id_MT1(1:numRows1,1)=j; % number of spectrum (loop)
d1(1:numRows1,1:5)=Process_Data2(locs1-1000+(j*n_WL),11:15);
pkss1=[id_MT1(:,1),locs1(:,1),pks1(:,1),d1(:,1:5)]; % concatinating of above matrix
Min_Through=[Min_Through;pkss1]; % concatinating of peaks of each spectrum to achieve Local Maximum of through spectrum
id_MT1=[];
d1=[];

   %%% finding of Local Maximum of second-order derivative of drop transmition <===> minimum of drop spectrum ('MinPeakProminence' used for sharp min/max)
[pks2,locs2] = findpeaks(Process_Data2(1+(j*n_WL):n_WL+(j*n_WL),4),Process_Data2(1+(j*n_WL):n_WL+(j*n_WL),1),'MinPeakProminence',0.01); % finding sharp!! Maximum of second-order derivative of drop spectrum (sharp minimum of drop spectrum) and theirs locations
[numRows2,numCols2] = size(pks2); % number of Local Maximum in each spectrum (in each loop)
id_MT2(1:numRows2,1)=j; % number of spectrum (loop)
d2(1:numRows2,1:5)=Process_Data2(locs2-1000+(j*n_WL),11:15);
pkss2=[id_MT2(:,1),locs2(:,1),pks2(:,1),d2(:,1:5)]; % concatinating of above matrix
Max_Through2=[Max_Through2;pkss2]; % concatinating of peaks of each spectrum to achieve Local Maximum of drop spectrum
id_MT2=[];
d2=[];
end

%%
%%% waterfall plot of second waveguide (drop)
% figure(10) shows the transmition spectrums
% figure(20) shows the second-order derivative of transmition spectrums
z=ones(n_WL,1);
zx=ones(n_WL-20,1); % remove 20 points of end of each spectrum to remove the discontinues 
for j=0:1:5
figure(10)
plot3(Process_Data2(1+(j*n_WL):n_WL+(j*n_WL),1),z*j,Process_Data2(1+(j*n_WL):n_WL+(j*n_WL),2),'linewidth',2)
hold on
grid on
figure(20)
plot3(Process_Data2(1+(j*n_WL):n_WL+(j*n_WL)-20,1),zx*j,Process_Data2(1+(j*n_WL):n_WL+(j*n_WL)-20,4),'linewidth',2)
hold on
grid on
end
figure(10)
xlabel('Wavelength(nm)')
ylabel('Number of spectrum','Color','k')
zlabel('Transmission','Color','k')
title('Transmission spectrums in through port')
get(gca,'fontname')  % shows you what you are using.
set(gca,'fontname','times','fontweight','bold')  % Set it to times
set(gca,'fontsize',16)
set(gca,'linewidth',0.85)
figure(20)
xlabel('Wavelength(nm)')
ylabel('Number of spectrum','Color','k')
zlabel('2nd-order derivative of transmission','Color','k')
chr = '2nd-order derivative of transmission spectrums in drop port';
title(chr)
get(gca,'fontname')  % shows you what you are using.
set(gca,'fontname','times','fontweight','bold')  % Set it to times
set(gca,'fontsize',16)
set(gca,'linewidth',0.85)