M = csvread('methylation_restricted_matrix.csv');
M = transpose(M)
N = partialcorr(M, mean(M, 2));
HeatMap(N)