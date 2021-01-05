'''
with open("customReport.txt") as fp:
    fp=fp.read().splitlines()
    agonist=[]
    antagonist=[]
    for i in fp:
        if "ANTAGONIST" in i or "antagonist" in i:
            antagonist.append(i)
        elif "AGONIST" in i or "agonist" in i:
            agonist.append(i)
    #print(agonist,antagonist)
    #print(len(agonist),len(antagonist))
from pypdb import *
found_pdbs = Query('Protease bound with agonist').search()
print(len(found_pdbs),found_pdbs)
'''

import glob 
dwnlded=[]
for filename in glob.glob('pdb_files/agonists/*.pdb'):
    dwnlded.append(filename[19:23])
import requests
agons=[]
repeat=[]
with open("agonist.txt") as fp:
    fp=fp.read().split(",")
    for i in fp:
        if i not in agons:
            agons.append(i)
        else:
            repeat.append(i)

for i in agons:
    if i not in dwnlded:
        link="https://files.rcsb.org/download/"+i+".pdb"
        name="pdb_files/agonists/"+i+".pdb"
        r = requests.get(link, allow_redirects=True)
        open(name, 'wb').write(r.content)
print(agons[:100],len(agons),len(repeat))

dwnlded=[]
for filename in glob.glob('pdb_files/antagonists/*.pdb'):
    dwnlded.append(filename[22:26])
print(dwnlded[0])
print(len(dwnlded))

antagons=[]
repeat=[]
with open("antagonist.txt") as fp:
    fp=fp.read().split(",")
    for i in fp:
        if i not in antagons:
            antagons.append(i)
        else:
            repeat.append(i)
print(len(antagons),len(repeat))



for i in antagons:
    if i not in dwnlded:
        link="https://files.rcsb.org/download/"+i+".pdb"
        name="pdb_files/antagonists/"+i+".pdb"
        print(link)
        r = requests.get(link, allow_redirects=True)
        open(name, 'wb').write(r.content)

print(antagons[:100],len(antagons),len(repeat))
