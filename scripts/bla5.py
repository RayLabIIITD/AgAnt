import glob
import json
row_label=[]
for filename in glob.glob("pdb_files/ant_real/*.pdb"):
    filename=filename[-8:-4]
    row_label.append(filename)
for filename in glob.glob("pdb_files/ago_real/*.pdb"):
    filename=filename[-8:-4]
    if filename not in row_label:
        row_label.append(filename)
    else:
        print(filename)

with open("row_label.json","w") as fp:
    json.dump(row_label,fp)
print(len(row_label))