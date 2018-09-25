import csv

mrna_ids = {}
with open("ROSMAP_IDkey.csv") as g:
    line1 = g.readline()
    for line in g:
        values = line.split(",")
        if values[9] == '1' and values[11] == '1' and values[12] == '1' and values[15] == '1':
            mrna_ids[values[4]] = values[1]

ordered_proj_ids = []
with open("rnaseqinput.csv", "r") as f:
    line1 = f.readline().strip().split(",")
    for label in line1:
        ordered_proj_ids.append(mrna_ids[label])

column_nums = [None]*503
count = []
with open("ROSMAP_clinical.csv", "r") as h:
    line1 = h.readline()
    for line in h:
        values = line.strip().split(",")
        try:
            pos = ordered_proj_ids.index(values[1])
            column_nums[pos] = int(values[12])*(4-int(values[16]))
                               # *int(values[17])
        except ValueError:
            pass

print(column_nums)
distinct = {}

for el in column_nums:
    if el not in distinct:
        distinct[el] = True


mapping = {}
keys = sorted(distinct.keys())
c = 0
print(len(keys))
for k in keys:
    mapping[k] = c
    c+= 1

for i in range(len(column_nums)):
    column_nums[i] = mapping[column_nums[i]]

print(column_nums)




