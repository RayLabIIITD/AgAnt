import glob
import numpy as np
import json

feats=[]
temp=[]
labels=[]
for filename in glob.glob("ant_bind/*.txt"):
    tempo=[]
    with open(filename) as fp:
        fp = fp.read()
    fp=fp.splitlines()
    for i in fp:
        if i[:6]=="Pocket":
            if len(temp)!=0:
                tempo.append(temp)
            temp=[]
        else:
            try:
                temp.append(float(i[i.index(":")+1:]))
            except:
                continue
    feats.append(tempo)
    labels.append(1)


for filename in glob.glob("ago_bind/*.txt"):
    tempo=[]
    with open(filename) as fp:
        fp = fp.read()
    fp=fp.splitlines()
    for i in fp:
        if i[:6]=="Pocket":
            if len(temp)!=0:
                tempo.append(temp)
            temp=[]
        else:
            try:
                temp.append(float(i[i.index(":")+1:]))
            except:
                continue
    feats.append(tempo)
    labels.append(0)


with open("bind_site_feats.json","w") as fp:
    json.dump(feats,fp)

with open("bind_site_labels.json","w") as fp:
    json.dump(labels,fp)
