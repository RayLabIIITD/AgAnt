import json
import requests
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import gensim 
from sklearn.manifold import TSNE

embed_seqs=[]
for filename in glob.glob("pdb_files/ant_real/*.pdb"):
    filename=filename[-8:-4]
    seq=[]
    embed=[]
    link="https://www.rcsb.org/fasta/entry/"+filename+"/download"
    r = requests.get(link, allow_redirects=True)
    r=r.content.decode('utf8').splitlines()
    #print(r)
    for i in r:
        if i[0]!='>':
            temp=i
            seq.append(temp)
    for i in seq:
        for n,j in enumerate(i[:-2]):#here
            if i[n:n+3] not in embed_seqs:#here
                embed_seqs.append(i[n:n+3])#here


for filename in glob.glob("pdb_files/ago_real/*.pdb"):
    filename=filename[-8:-4]
    seq=[]
    embed=[]
    link="https://www.rcsb.org/fasta/entry/"+filename+"/download"
    r = requests.get(link, allow_redirects=True)
    r=r.content.decode('utf8').splitlines()
    #print(r)
    for i in r:
        if i[0]!='>':
            temp=i
            seq.append(temp)
    for i in seq:
        for n,j in enumerate(i[:-2]):#here
            if i[n:n+3] not in embed_seqs:#here
                embed_seqs.append(i[n:n+3])#here
    #print(np.array(embed).shape)
    #print(embed
with open("temp.json","w") as fp:#here
    json.dump(embed_seqs,fp) 
print(len(embed_seqs))

with open("temp.json") as fp:#here
    embed_seqs=json.load(fp) 
temp=[]
for i in embed_seqs:
    temp2=[]
    temp2.append(i)
    temp.append(temp2)
embed_seqs=temp


EMBEDDING_DIM = 100
# train word2vec model
model = gensim.models.Word2Vec(sentences=embed_seqs, size=EMBEDDING_DIM, min_count=1)
# vocab size
words = list(model.wv.vocab)
print('Vocabulary size: %d' % len(words))
#print(words)
filename = 'word2vec.model'
#print(model["CGM"])
model.save(filename)
embeddings_index = {}
for i in words:
  embeddings_index[i]=model[i]
