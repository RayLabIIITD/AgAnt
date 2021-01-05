import glob
import json
not_dwnlded=[] 
for filename in glob.glob('pdb_files/antagonists/*.pdb'):
    with open(filename) as fp:
        fp=fp.read().splitlines()
        if fp[-1][:3]!="END" and fp[-2][:3]!="END":
            not_dwnlded.append(filename[-8:-4])

print(not_dwnlded,len(not_dwnlded))
with open("not_down_ant.txt","w") as fp:
    json.dump(not_dwnlded,fp)

not_dwnlded=[] 
for filename in glob.glob('pdb_files/agonists/*.pdb'):
    with open(filename) as fp:
        fp=fp.read().splitlines()
        if fp[-1][:3]!="END" and fp[-2][:3]!="END":
            not_dwnlded.append(filename[-8:-4])

print(not_dwnlded,len(not_dwnlded))
with open("not_down_ago.txt","w") as fp:
    json.dump(not_dwnlded,fp)