import json
import requests
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.manifold import TSNE
import gensim 
model = gensim.models.Word2Vec.load("word2vec.model")
words = list(model.wv.vocab)
print('Vocabulary size: %d' % len(words))
embeddings_index = {}
for i in words:
  embeddings_index[i]=model[i]
seq_dict = embeddings_index
embed_seqs={}
input=[]
output=[]
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
        for n,j in enumerate(i[:-2]):#change here
            embed.append(seq_dict[i[n:n+3]].tolist())#and here
    input.append(embed)
    output.append(0)
    embed_seqs[filename]=embed

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
            embed.append(seq_dict[i[n:n+3]].tolist())#here
    embed_seqs[filename]=embed
    input.append(embed)
    output.append(1)
    #print(np.array(embed).shape)

    #print(embed
with open("input_7.json","w") as fp:
    json.dump(input,fp)
with open("output_7.json","w") as fp:
    json.dump(output,fp)