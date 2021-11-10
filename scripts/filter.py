#list out all files with agonist/antagonist in name
import glob
import json
ago=[]
for filename in glob.glob('pdb_files/agonists/*.pdb'):
    with open(filename) as fp:
        fp=fp.read().splitlines()
        fp=fp[0].split(" ")
        temp=[]
        for i in fp:
            for j in i.split("/"):
                temp.append(j)
        fp=temp
        if "AGONISTS" in fp or "AGONIST" in fp or "agonists" in fp or "agonist" in fp:
            ago.append(filename[-8:-4])
print(ago,len(ago))

with open("ago_name.txt","w") as fp:
    json.dump(ago,fp)

ant=[]
for filename in glob.glob('pdb_files/antagonists/*.pdb'):
    with open(filename) as fp:
        fp=fp.read().splitlines()
        fp=fp[0].split(" ")
        temp=[]
        for i in fp:
            for j in i.split("/"):
                temp.append(j)
        fp=temp
        if "ANTAGONISTS" in fp or "ANTAGONIST" in fp or "antagonists" in fp or "antagonist" in fp:
            ant.append(filename[-8:-4])


print(ant,len(ant))
with open("ant_name.txt","w") as fp:
    json.dump(ant,fp)