#list all dna/rna files
import glob
import json
import re
rna_dna=[]
for filename in glob.glob('pdb_files/agonists/*.pdb'):
    with open(filename) as fp:
        fp=fp.read().splitlines()
        fp=re.split("/|-| ",fp[0])
        temp=[]
        for i in fp:
            temp.append(i)
        fp=temp
        if "DNA" in fp or "RNA" in fp:
            rna_dna.append(filename[-8:-4])
print(rna_dna,len(rna_dna))

with open("rd_agon.txt","w") as fp:
    json.dump(rna_dna,fp)

rna_dna=[]
for filename in glob.glob('pdb_files/antagonists/*.pdb'):
    with open(filename) as fp:
        fp=fp.read().splitlines()
        fp=re.split(" /-",fp[0])
        temp=[]
        for i in fp:
            temp.append(i)
        fp=temp
        if "DNA" in fp or "RNA" in fp:
            rna_dna.append(filename[-8:-4])


print(rna_dna,len(rna_dna))
with open("rd_ant.txt","w") as fp:
    json.dump(rna_dna,fp)



