import glob
import json
import requests
import pandas as pd


ligs=[]
df = pd.read_excel (r'labels/labels_ago.xlsx')
for n,i in df.iterrows():
    if i["Label"]==1:
        temp= i["COMPOUND_IDS"]
        temp=temp.replace("[","").replace("]","").replace("'","").replace(" ","")
        temp=temp.split(",")
        for i in temp:
            ligs.append(i)
df = pd.read_excel (r'labels/labels_ant.xlsx')
for n,i in df.iterrows():
    break
    if i["Label"]==1:
        temp= i["COMPOUND_IDS"]
        temp=temp.replace("[","").replace("]","").replace("'","").replace(" ","")
        temp=temp.split(",")
        for i in temp:
            ligs.append(i)

for i in ligs:
    link="https://files.rcsb.org/ligands/view/"+i+"_model.pdb"
    name="ligands/"+i+".pdb"
    r = requests.get(link, allow_redirects=True)
    open(name, 'wb').write(r.content)