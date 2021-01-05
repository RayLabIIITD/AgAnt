import shutil

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

with open("ago_name.txt") as fp:
    fp=fp.read()
    fp=fp[1:-1].replace("\"","").replace("\'","").split(", ")
    print(len(fp))
    for i in fp:
        source="pdb_files/antagonists/"+i+".pdb"
        destination="pdb_files/ago_header/"+i+".pdb"
        try:
            shutil.move(source, destination)
        except:
            pass

with open("ant_name.txt") as fp:
    fp=fp.read()
    fp=fp[1:-1].replace("\"","").replace("\'","").split(", ")
    print(len(fp))
    for i in fp:
        source="pdb_files/antagonists/"+i+".pdb"
        destination="pdb_files/ant_header/"+i+".pdb"
        try:
            shutil.move(source, destination)
        except:
            pass