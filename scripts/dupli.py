import glob
import json
agos=[]
ants=[]
for filename in glob.glob("pdb_files/ant_real/*.pdb"):
    filename=filename[-8:-4]
    ants.append(filename)
for filename in glob.glob("pdb_files/ago_real/*.pdb"):
    filename=filename[-8:-4]
    agos.append(filename)

with open("agos_real.json","w") as fp:
    json.dump(agos,fp)

with open("ants_real.json","w") as fp:
    json.dump(ants,fp)