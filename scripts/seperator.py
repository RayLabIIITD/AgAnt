import shutil
import pandas as pd
import glob
with open("not_down_ago.txt") as fp:
    fp=fp.read()
    fp=fp[1:-1].replace("\"","").replace("\'","").split(", ")
    print(len(fp))
    for i in fp:
        source="pdb_files/agonists/"+i+".pdb"
        destination="pdb_files/agons_not_dwnlded/"+i+".pdb"
        try:
            shutil.move(source, destination)
        except:
            pass

with open("not_down_ant.txt") as fp:
    fp=fp.read()
    fp=fp[1:-1].replace("\"","").replace("\'","").split(", ")
    print(len(fp))
    for i in fp:
        source="pdb_files/antagonists/"+i+".pdb"
        destination="pdb_files/anta_not_dwnlded/"+i+".pdb"
        try:
            shutil.move(source, destination)
        except:
            pass

with open("rd_agon.txt") as fp:
    fp=fp.read()
    fp=fp[1:-1].replace("\"","").replace("\'","").split(", ")
    print(len(fp))
    for i in fp:
        source="pdb_files/agonists/"+i+".pdb"
        destination="pdb_files/rd_in_agons/"+i+".pdb"
        try:
            shutil.move(source, destination)
        except:
            pass

with open("rd_ant.txt") as fp:
    fp=fp.read()
    fp=fp[1:-1].replace("\"","").replace("\'","").split(", ")
    print(len(fp))
    for i in fp:
        source="pdb_files/antagonists/"+i+".pdb"
        destination="pdb_files/rd_in_antagons/"+i+".pdb"
        try:
            shutil.move(source, destination)
        except:
            pass
x=0
y=0
filenames=glob.glob('pdb_files/ago_real/*.pdb')
df = pd.read_excel (r'labels/labels_ago.xlsx')
df=df.drop(columns=['Unnamed: 0'])
temp=[]
for i in filenames:
    temp.append(i[-8:-4])
filenames=temp
fils=[]
for n,i in df.iterrows():
    if i["Label"]==1:
        k=i["PDB_ID"]
        fils.append(k)
        source="pdb_files/ago_header/"+k+".pdb"
        destination="pdb_files/ago_real/"+k+".pdb"
        try:
            shutil.move(source, destination)
        except:
            pass

df = pd.read_excel (r'labels/labels_ant.xlsx')
df=df.drop(columns=['Unnamed: 0'])
for n,i in df.iterrows():
    if i["Label"]==1:
        k=i["PDB_ID"]
        source="pdb_files/ant_header/"+k+".pdb"
        destination="pdb_files/ant_real/"+k+".pdb"
        try:
            shutil.move(source, destination)
        except:
            pass