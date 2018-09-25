from sklearn.decomposition import PCA

import csv
Matrix = []
with open("rnaseqinput.csv", "r", newline='') as f:
    readCSV = csv.reader(f, delimiter=',')
    for row in readCSV:
        Matrix.append(row)

print("read")
Matrix = [[Matrix[j][i] for j in range(len(Matrix))] for i in range(len(Matrix[0]))]

pca = PCA(n_components=10)
Matrix = pca.fit_transform(Matrix)

print("fitted")


with open ("rna_restricted_matrix.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(Matrix)