from Bio.PDB import *
import io
import glob
import json

'''
Cant rely on BioPython
parser = PDBParser()
structure = parser.get_structure('PHA-L', '4u0g.pdb')
rcount=0
acount=0
for model in structure:
    for i in model.get_residues():
        #print (i)
        rcount+=1
ppb = PPBuilder()
for atom in structure.get_atoms():
    acount+=1
x=0
for pp in ppb.build_peptides(structure):
    #print(pp.get_sequence())
    x+=1
'''
#print(x,rcount,acount)
acount=0
rcount=0

def atom_counter(pdb_str):
    count=0
    file= pdb_str.splitlines()
    for n,line in enumerate(file):
        if line[:4] == "ATOM":
            count+=1
    return count

def residue_counter(pdb_str):
    count=0
    file= pdb_str.splitlines()
    for n,line in enumerate(file):
        if line[:6]=="SEQRES":
            temp=line[19:]
            for i in range(0,len(temp),4):
                #print(temp[i:i+3])
                if temp[i].isalnum():
                    count+=1
    return count

def chain_extractor(pdb_str):
    mol_ids=[]
    chains={}
    names={}
    file= pdb_str.splitlines()
    for n,line in enumerate(file):
        if line[10:16]=="MOL_ID" :
            temp=line[17:]
            pos=temp.index(";")
            num=int(temp[:pos])
            if num not in mol_ids:
                mol_ids.append(num)
                temp=file[n+2][18:file[n+2].index(";")].split(", ")
                chains[num]=temp
                temp=file[n+1][22:file[n+1].index(";")]
                names[num]=temp
        elif line[11:17]=="MOL_ID":
            temp=line[18:]
            pos=temp.index(";")
            num=int(temp[:pos])
            if num not in mol_ids:
                mol_ids.append(num)    
                temp=file[n+2][18:file[n+2].index(";")].split(", ")
                chains[num]=temp
                temp=file[n+1][21:file[n+1].index(";")]
                names[num]=temp
    return mol_ids,chains,names

def sequence_builder_residue(pdb_str,chains):
    file= pdb_str.splitlines()
    res_seq={}
    for i in chains:
        for j in chains[i]:
            res_seq[j]=[]
    for n,line in enumerate(file):
        if line[:6]=="SEQRES":
            chain_num=line[11]
            temp=line[19:].split(" ")
            for i in temp:
                if i !="":
                    res_seq[chain_num].append(i)
    return res_seq

def sequence_builder_atom(pdb_str,chains):
    file= pdb_str.splitlines()
    atom_seq={}
    for i in chains:
        for j in chains[i]:
            atom_seq[j]=[]
    for n,line in enumerate(file):
        if line[:4]=="ATOM" or line[:6]=="HETATM":
            temp=[]
            temp.append(int(line[6:11]))
            temp.append(line[13:line[14:].index(" ")+14])
            temp.append(line[17:20])
            c=line[27:56].split(" ")
            coords=[]
            for i in c:
                if i!="":
                    coords.append(i)
            temp.append(coords)
            atom_seq[line[21]].append(temp)
    return atom_seq

def encoder(x):
    res_dict={"ALA":"A","ARG":"R","ASN":"N","ASP":"D","CYS":"C","GLN":"Q","GLU":"G","GLY":"G","HIS":"H","ILE":"I","LEU":"L","LYS":"K","MET":"M","PHE":"F","PRO":"P","SER":"S","THR":"T","TRP":"W","TYR":"Y","VAL":"V","SEC":"U","PYL":"O"}
    temp=[]
    for i in x:
        if i in res_dict:
            temp.append(res_dict[i])
        else:
            temp.append(i.lower())
    return temp
for filename in glob.glob('pdb_files/*.pdb'):
    with open(filename) as file:
        print(filename)
        file = file.read()
        mol_ids,chains,names=chain_extractor(file)
        acount=atom_counter(file)
        res_seq=sequence_builder_residue(file,chains)
        #atom_seq=sequence_builder_atom(file,chains)
        rcount=residue_counter(file)
        for i in names:
            temp="sep_outputs/"+filename[10:filename.index(".")]+"_"+names[i]+".json"
            with open(temp,"w") as fp:
                temp={}
                temp["Name"]=names[i]
                temp["Chains"]=chains[i]
                temp["Residues_List"]={}
                temp["Atom_List"]={}
                for j in chains[i]:
                    temp["Residues_List"][j]=res_seq[j]
                    res_string="".join(encoder(res_seq[j]))
                    print(res_string)
                    #temp["Atom_List"][j]=atom_seq[j]
                
                #print(temp)
                json.dump(temp,fp)



print(mol_ids,chains,names)
print(acount,rcount)
#print(res_seq)
#print(atom_seq)
