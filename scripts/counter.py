import glob
import requests
import json
'''
agonist=[]
no_agonist=[]
ago_and_ant=[]
not_available=[]
files_done=[]
with open("count/files_done.json") as fp:
    files_done=json.load(fp)
with open("count/agos_and_ant.json") as fp:
    ago_and_ant=json.load(fp)
with open("count/agos.json") as fp:
    agonist=json.load(fp)
with open("count/no.json") as fp:
    not_available=json.load(fp)
with open("count/no_agos.json") as fp:
    no_agonist=json.load(fp)
x=0+len(files_done)
for filename in glob.glob('pdb_files/agonists/*.pdb'):
    filename=filename[-8:-4]
    if filename not in files_done:
        x+=1
        print(filename,x)
        link="https://www.rcsb.org/pdb/rest/customReport.xml?pdbids="+filename+"&customReportColumns=pubmedId&primaryOnly=1"
        r = requests.get(link, allow_redirects=True)
        r=r.content.decode('utf8').splitlines()
        try:
            start=r[4].index(">")+1
        except:
            not_available.append(filename)
            with open("count/no.json","w") as fp:
                    json.dump(not_available,fp)
            files_done.append(filename)
            with open("count/files_done.json","w") as fp:
                json.dump(files_done,fp)
            continue
        end=r[4][start+1:].index("<")+start+1
        target=r[4][start:end]
        print(target)
        if(target=="null"):
            not_available.append(filename)
            with open("count/no.json","w") as fp:
                    json.dump(not_available,fp)
        else:
            link="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id="+target
            r = requests.get(link, allow_redirects=True)
            r=r.content.decode('utf8').replace("'", '"')
            r=r[17:]
            try:
                start=r.index("abstract")
            except:
                not_available.append(filename)
                continue
            end=r[start+10:].index('"')+start+10
            text=r[start+10:end]
            text=text.replace(",","")
            text=text.replace(".","")
            text=text.lower()
            text=text.split(" ")
            if "agonist" in text and "antagonist" in text:
                ago_and_ant.append(filename)
                with open("count/agos_and_ant.json","w") as fp:
                    json.dump(ago_and_ant,fp)
            elif "agonist" in text:
                agonist.append(filename)
                with open("count/agos.json","w") as fp:
                    json.dump(agonist,fp)
            else:
                no_agonist.append(filename)
                with open("count/no_agos.json","w") as fp:
                    json.dump(no_agonist,fp)
        files_done.append(filename)
        with open("count/files_done.json","w") as fp:
            json.dump(files_done,fp)
        
    

print("agonists",len(agonist),"\n","no agonists",len(no_agonist),"\n","ago and ant",len(ago_and_ant),"\n","not available",len(not_available))
print(ago_and_ant)
print(not_available)
'''
antagonist=[]
no_antagonist=[]
ago_and_ant=[]
not_available=[]
files_done=[]
with open("count/ant/files_done.json") as fp:
    files_done=json.load(fp)
with open("count/ant/agos_and_ant.json") as fp:
    ago_and_ant=json.load(fp)
with open("count/ant/ants.json") as fp:
    agonist=json.load(fp)
with open("count/ant/no.json") as fp:
    not_available=json.load(fp)
with open("count/ant/no_ants.json") as fp:
    no_agonist=json.load(fp)
x=0+len(files_done)
for filename in glob.glob('pdb_files/antagonists/*.pdb'):
    filename=filename[-8:-4]
    if filename not in files_done:
        x+=1
        print(filename,x)
        link="https://www.rcsb.org/pdb/rest/customReport.xml?pdbids="+filename+"&customReportColumns=pubmedId&primaryOnly=1"
        r = requests.get(link, allow_redirects=True)
        r=r.content.decode('utf8').splitlines()
        try:
            start=r[4].index(">")+1
        except:
            not_available.append(filename)
            with open("count/ant/no.json","w") as fp:
                    json.dump(not_available,fp)
            files_done.append(filename)
            with open("count/ant/files_done.json","w") as fp:
                json.dump(files_done,fp)
            continue
        end=r[4][start+1:].index("<")+start+1
        target=r[4][start:end]
        print(target)
        if(target=="null"):
            not_available.append(filename)
            with open("count/ant/no.json","w") as fp:
                    json.dump(not_available,fp)
        else:
            link="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id="+target
            r = requests.get(link, allow_redirects=True)
            r=r.content.decode('utf8').replace("'", '"')
            r=r[17:]
            try:
                start=r.index("abstract")
            except:
                not_available.append(filename)
                files_done.append(filename)
                with open("count/ant/files_done.json","w") as fp:
                    json.dump(files_done,fp)
                continue
            end=r[start+10:].index('"')+start+10
            text=r[start+10:end]
            text=text.replace(",","")
            text=text.replace(".","")
            text=text.lower()
            text=text.split(" ")
            if "agonist" in text and "antagonist" in text:
                ago_and_ant.append(filename)
                with open("count/ant/agos_and_ant.json","w") as fp:
                    json.dump(ago_and_ant,fp)
            elif "antagonist" in text:
                antagonist.append(filename)
                with open("count/ant/ants.json","w") as fp:
                    json.dump(antagonist,fp)
            else:
                no_antagonist.append(filename)
                with open("count/ant/no_ants.json","w") as fp:
                    json.dump(no_antagonist,fp)
        files_done.append(filename)
        with open("count/ant/files_done.json","w") as fp:
            json.dump(files_done,fp)
