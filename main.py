import csv
import time

proj_ids = {}
mwas_ids = {}
mrna_ids = {}
with open("ROSMAP_IDkey.csv") as g:
    line1 = g.readline()
    for line in g:
        values = line.split(",")
        if values[9] == '1' and values[11] == '1' and values[12] == '1' and values[15] == '1':
            proj_ids[values[3]] = values[1]
            mwas_ids[values[3]] = True
            mrna_ids[values[4]] = values[3]

ordered_mwas_ids = []
with open("rnaseqinput.csv", "r") as f:
    line1 = f.readline().strip().split(",")
    for label in line1:
        ordered_mwas_ids.append(mrna_ids[label])

columns = []


with open("AMP-AD_ROSMAP_Rush-Broad_IlluminaHumanMethylation450_740_imputed.tsv", "r") as f:
    column_nums = [None]*503


    line1 = f.readline().strip().split("\t")
    for i in range(len(line1)):
        if line1[i] in mwas_ids:
            pos = ordered_mwas_ids.index(line1[i])
            column_nums[pos] = i
            mwas_ids[line1[i]] = False

    print(column_nums)
    # matrix = []
    # for item in column_nums:
    #     matrix.append([0]*len(column_nums))


    for i in column_nums:
        columns.append([])

    ctr = 0
    for line in f:
        ctr += 1
        if ctr % 50000 == 0:
            print(ctr)
        vals = line.strip().split("\t")

        for col, index in zip(columns, column_nums):
            col.append(float(vals[index]))


print(len(columns), len(columns[0]))
# columns = [[columns[j][i] for j in range(len(columns))] for i in range(len(columns[0]))]
time.sleep(10)
print(len(columns), len(columns[0]))

with open ("methylation_restricted.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(columns)





