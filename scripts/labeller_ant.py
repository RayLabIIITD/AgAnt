import glob
import json
import requests
import pandas as pd
from termcolor import colored

filenames=glob.glob('labels/*.xlsx')


a=0
b=0
c=0
d=0
e=0
if len(filenames)==1:
    df=pd.DataFrame()
    Data={"PDB_ID":[],"PDB_TITLE":[],"PDB_HEADER":[],"MOLECULES":[],"COMPOUND_IDS":[],"PUBMED_ID":[],"PUBMED_ABS":[]}
    labels={}
    x=0
    with open("labels/labels.json") as fp:
        labels=json.load(fp)
    x+=len(labels)
    for filename in glob.glob('pdb_files/ant_header/*.pdb'):
        target=""
        text=""
        title=""
        header=""
        filename=filename[-8:-4]
        cmpdid=[]
        #if filename not in labels:
        molecules=[]
        labels[filename]={"Molecule":"","Agonist":""}
        x+=1
        #print(filename,x)
        link="https://files.rcsb.org/header/"+filename+".pdb"
        r = requests.get(link, allow_redirects=True)
        r=r.content.decode('utf8').splitlines()
        for n,i in enumerate(r):
            if i[:6]=="HEADER":
                header+=i[6:]
                #print(i)
            elif i[:5]=="TITLE":
                title+=i[5:]
                #print(i)
            #elif i[:6]=="COMPND":
            #    if i[11:19]=="MOLECULE":
            #        molecules.append(i[20:])
                #print(i)
        link="https://www.ebi.ac.uk/pdbe/api/pdb/entry/molecules/"+filename
        r = requests.get(link, allow_redirects=True)
        r=r.json()
        for i in r:
            for  j in r[i]:
                try:
                    if j['chem_comp_ids'][0]!="HOH":
                        cmpdid.append(j['chem_comp_ids'][0])
                        molecules.append(j['molecule_name'][0])
                except:
                    pass
                try:
                    molecules.append(j['synonym'])
                except:
                    continue
        
        link="https://www.rcsb.org/pdb/rest/customReport.xml?pdbids="+filename+"&customReportColumns=pubmedId&primaryOnly=1"
        r = requests.get(link, allow_redirects=True)
        r=r.content.decode('utf8').splitlines()
        start=r[4].index(">")+1
        end=r[4][start+1:].index("<")+start+1
        target=r[4][start:end]
        link="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id="+target
        r = requests.get(link, allow_redirects=True)
        r=r.content.decode('utf8').replace("'", '"')
        r=r[17:]
        try:
            start=r.index("abstract")
            end=r[start+10:].index('",')+start+10
            text=r[start+10:end]
            text=text.lower()
            #print(text)
        except:
            pass
        Data["PDB_ID"].append(filename)
        Data["PDB_TITLE"].append(title)
        Data["MOLECULES"].append(molecules)
        Data["COMPOUND_IDS"].append(cmpdid)
        Data["PDB_HEADER"].append(header)
        Data["PUBMED_ID"].append(target)
        Data["PUBMED_ABS"].append(text)
        #labels[filename]["Molecule"]=input("Molecule: ")
        #labels[filename]["Agonist"]=input("Agonist: ")
        
            #with open("labels/labels.json","w") as fp:
            #            json.dump(labels,fp)
    print("Header done")
    with open("count/ant/ants.json") as fp:
        names=json.load(fp)
        for filename in names:
            target=""
            text=""
            molecules=[]
            cmpdid=[]
            title=""
            header=""
            #if filename not in labels:
            labels[filename]={"Molecule":"","Agonist":""}
            x+=1
            #print(filename,x)
            link="https://files.rcsb.org/header/"+filename+".pdb"
            r = requests.get(link, allow_redirects=True)
            r=r.content.decode('utf8').splitlines()
            for n,i in enumerate(r):
                if i[:6]=="HEADER":
                    header+=i[6:]
                    #print(i)
                elif i[:5]=="TITLE":
                    title+=i[6:]
                    #print(i)
                #elif i[:6]=="COMPND":
                #    if i[11:19]=="MOLECULE":
                #        molecules.append(i[20:])
                    #print(i)
            link="https://www.ebi.ac.uk/pdbe/api/pdb/entry/molecules/"+filename
            r = requests.get(link, allow_redirects=True)
            r=r.json()
            for i in r:
                for  j in r[i]:
                    try:
                        if j['chem_comp_ids'][0]!="HOH":
                            cmpdid.append(j['chem_comp_ids'][0])
                            molecules.append(j['molecule_name'][0])
                    except:
                        pass
                    try:
                        molecules.append(j['synonym'])
                    except:
                        continue
            link="https://www.rcsb.org/pdb/rest/customReport.xml?pdbids="+filename+"&customReportColumns=pubmedId&primaryOnly=1"
            r = requests.get(link, allow_redirects=True)
            r=r.content.decode('utf8').splitlines()
            start=r[4].index(">")+1
            end=r[4][start+1:].index("<")+start+1
            target=r[4][start:end]
            link="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id="+target
            #print(target)
            r = requests.get(link, allow_redirects=True)
            r=r.content.decode('utf8').replace("'", '"')
            r=r[17:]
            try:
                start=r.index("abstract")
                end=r[start+10:].index('",')+start+10
                text=r[start+10:end]
                text=text.lower()
                #print(text)
            except:
                pass
            Data["PDB_ID"].append(filename)
            Data["PDB_TITLE"].append(title)
            Data["MOLECULES"].append(molecules)
            Data["COMPOUND_IDS"].append(cmpdid)
            Data["PDB_HEADER"].append(header)
            Data["PUBMED_ID"].append(target)
            Data["PUBMED_ABS"].append(text)
            #labels[filename]["Molecule"]=input("Molecule: ")
            #labels[filename]["Agonist"]=input("Agonist: ")
            #with open("labels/labels.json","w") as fp:
            #            json.dump(labels,fp)
    print("antsdone")
    with open("count/ant/agos_and_ant.json") as fp:
        names=json.load(fp)
        for filename in names:
            target=""
            text=""
            molecules=[]
            cmpdid=[]
            title=""
            header=""
            #if filename not in labels:
            labels[filename]={"Molecule":"","Agonist":""}
            x+=1
            #print(filename,x)
            link="https://files.rcsb.org/header/"+filename+".pdb"
            r = requests.get(link, allow_redirects=True)
            r=r.content.decode('utf8').splitlines()
            for n,i in enumerate(r):
                if i[:6]=="HEADER":
                    header+=i[6:]
                    #print(i)
                elif i[:5]=="TITLE":
                    title+=i[6:]
                    #print(i)
                #elif i[:6]=="COMPND":
                #    if i[11:19]=="MOLECULE":
                #        molecules.append(i[20:])
                    #print(i)
            link="https://www.ebi.ac.uk/pdbe/api/pdb/entry/molecules/"+filename
            r = requests.get(link, allow_redirects=True)
            r=r.json()
            for i in r:
                for  j in r[i]:
                    try:
                        if j['chem_comp_ids'][0]!="HOH":
                            cmpdid.append(j['chem_comp_ids'][0])
                            molecules.append(j['molecule_name'][0])
                    except:
                        pass
                    try:
                        molecules.append(j['synonym'])
                    except:
                        continue
            link="https://www.rcsb.org/pdb/rest/customReport.xml?pdbids="+filename+"&customReportColumns=pubmedId&primaryOnly=1"
            r = requests.get(link, allow_redirects=True)
            r=r.content.decode('utf8').splitlines()
            start=r[4].index(">")+1
            end=r[4][start+1:].index("<")+start+1
            target=r[4][start:end]
            link="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id="+target
            #print(target)
            r = requests.get(link, allow_redirects=True)
            r=r.content.decode('utf8').replace("'", '"')
            r=r[17:]
            try:
                start=r.index("abstract")
                end=r[start+10:].index('",')+start+10
                text=r[start+10:end]
                text=text.lower()
                #print(text)
            except:
                pass
            Data["PDB_ID"].append(filename)
            Data["PDB_TITLE"].append(title)
            Data["MOLECULES"].append(molecules)
            Data["COMPOUND_IDS"].append(cmpdid)
            Data["PDB_HEADER"].append(header)
            Data["PUBMED_ID"].append(target)
            Data["PUBMED_ABS"].append(text)
            #labels[filename]["Molecule"]=input("Molecule: ")
            #labels[filename]["Agonist"]=input("Agonist: ")
            #with open("labels/labels.json","w") as fp:
            #            json.dump(labels,fp)
    print("agosandantdone")
    df = pd.DataFrame(Data)
    df.to_excel("labels/labels_ant.xlsx")
else:
    x=0
    df = pd.read_excel (r'labels/labels_ant.xlsx')
    df=df.drop(columns=['Unnamed: 0'])
    for n,i in df.iterrows():
        x+=1
        print(x)
        if i["Label"]!=i["Label"]:
            #print(i)
            print(i["PDB_ID"])
            #print(i["PDB_TITLE"])
            #print(i["PDB_HEADER"])
            text=i["PDB_TITLE"]
            l1=['AGONIST','ANTAGONIST']
            result = " ".join(colored(t,'white','on_red') if t in l1 else t for t in text.split())
            print(result)
            text=i["PDB_HEADER"]
            l1=['AGONIST','ANTAGONIST']
            result = " ".join(colored(t,'white','on_red') if t in l1 else t for t in text.split())
            print(result)
            print(i["MOLECULES"])
            print(i["PUBMED_ID"])
            
            text=i["PUBMED_ABS"]
            l1=['agonist','antagonist','antgonist,','antgonist.','antagonists','antagonists.']
            result = " ".join(colored(t,'white','on_red') if t in l1 else t for t in text.split())
            print(result)
            #print(i["PUBMED_ABS"])
            labell=input()
            df.at[n,"Label"]=labell
            df.to_excel("labels/labels_ant.xlsx")  
        elif i["Label"]==0:
            a+=1
        elif i["Label"]==1:
            b+=1
        elif i["Label"]==2:
            c+=1
        elif i["Label"]==3:
            d+=1
        elif i["Label"]==4:
            e+=1
print(a,b,c,d,e)
