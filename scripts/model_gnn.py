import os 
os.environ["DGLBACKEND"] ="pytorch"
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
import json
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet
from sklearn.model_selection import train_test_split, cross_validate,StratifiedKFold
from pickle import load
from numpy import array
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils.vis_utils import plot_model
from keras.models import Model
from keras.layers import Input
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Dropout
from keras.layers import Embedding
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from keras.layers.merge import concatenate
#from sklearn.pipeline import Pipel
import pandas as pd
import numpy as np
import ast
import string
import nltk
import matplotlib.pyplot as plt
#nltk.download('wordnet')
import seaborn as sns
from sklearn import svm
from sklearn import metrics
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix,roc_auc_score
import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D
from tensorflow.keras.losses import sparse_categorical_crossentropy
from tensorflow.keras.optimizers import Adam
import seaborn as sns
from sklearn.manifold import TSNE
import torch

import pickle
import pandas as pd
import numpy as np
from tqdm import tqdm
from dgllife.model.model_zoo import GCNPredictor
from dgllife.model.model_zoo import AttentiveFPPredictor
from dgllife.model.model_zoo import WeavePredictor
import dgl
import torch
from torch.nn import NLLLoss
from torch.utils.data import DataLoader
from sklearn.metrics import f1_score, precision_score, recall_score, matthews_corrcoef,classification_report,accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import f1_score, precision_score, recall_score
from torch.nn import CrossEntropyLoss
from torch.utils.data import DataLoader
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
from sklearn.model_selection import StratifiedKFold
import glob
import dgl
import pickle
import networkx as nx
from dgl.data.utils import load_graphs

data=[]
labels=[]
agos=[]
ants=[]
labels_agos=[]
labels_ants=[]
with open("g_files/1A00.pt","rb") as fp:
    model = pickle.load(fp)
    print(model)
for filename in glob.glob("g_files/*.pt"):
  with open(filename,"rb") as fp:
    model = pickle.load(fp)
  #model[0].ndata['feats'] = torch.cat((model[0].ndata['residue_name'].reshape([model[0].ndata['residue_name'].shape[0],1]),model[0].ndata['h'],model[0].ndata['ss'],model[0].ndata['asa'],model[0].ndata['rsa'],model[0].ndata['coords']), dim=1)
  data.append(model[0])
  ants.append(model[0])
  labels_ants.append(torch.tensor([0,0]))
  labels.append(torch.tensor([0,0]))

#data = load_graphs("./data.bin")
#data=data[0]
dataa=[]
for g in data:
  g.ndata['feats'] = torch.cat((g.ndata['residue_name'].reshape([g.ndata['residue_name'].shape[0],1]).float(),g.ndata['h'],g.ndata['ss'],g.ndata['asa'],g.ndata['rsa'],g.ndata['coords']), dim=1)
  g.edata['feats'] = g.edata['delaunay_euclidean_distance'].float()
  dataa.append(g)
data=dataa

#labels = [np.random.randn(0,1) for x in range(0,len(data))]
def collate(samples):
    # The input `samples` is a list of pairs
    #  (graph, label).
    graphs, labels = map(list, zip(*samples))
    batched_graph = dgl.batch(graphs, node_attrs=['feats'],edge_attrs=["feats"])
    batched_graph.set_n_initializer(dgl.init.zero_initializer)
    batched_graph.set_e_initializer(dgl.init.zero_initializer)
    return batched_graph, torch.stack(labels)

train_data=[]
train_labels=[]
for n,abc in enumerate(data):
 train_data.append(abc)
 train_labels.append(labels[n])
n_feats = 22
train_data = list(zip(train_data, train_labels))
#Create dataloaders
train_loader = DataLoader(train_data, batch_size=15, shuffle=True,collate_fn=collate,drop_last=True)
#gcn_net = GCNPredictor(in_feats=n_feats,hidden_feats=[512,512],batchnorm=[True, True],dropout=[0.4, 0.4],classifier_hidden_feats=512,n_tasks=2)
#gcn_net = AttentiveFPPredictor(n_feats,17,n_tasks=2,num_layers=5)
gcn_net = GCNPredictor(in_feats=n_feats,hidden_feats=[512,512],dropout=[0.1, 0.1],classifier_hidden_feats=512,n_tasks=2)
epoch_losses = []
epoch_f1_scores = [] 
epoch_precision_scores = []
epoch_recall_scores = []
device="cuda"
epochs=100
gcn_net.to(device)
loss_fn = CrossEntropyLoss()
optimizer = torch.optim.Adam(gcn_net.parameters(), lr=0.005)
gcn_net.train()
for epoch in range(epochs):
  epoch_loss = 0
  preds = []
  labs = []
  # Train on batch
  for num, (bg, las) in enumerate(train_loader):
      las = las.to(device)
      graph_feats = bg.ndata.pop('feats').to(device)
      edge_feats = bg.edata.pop('feats').to(device)
      graph_feats, edge_feats,las = graph_feats.to(device), edge_feats.to(device),las.to(device)
      y_pred = gcn_net(bg, graph_feats)
      preds.append(y_pred.detach().numpy())
      labs.append(las.detach().numpy())
      ls = np.argmax(las, axis=1)
      loss = loss_fn(y_pred, ls)
      optimizer.zero_grad()
      loss.backward()
      optimizer.step()
      epoch_loss += loss.detach().item()

  epoch_loss /= (num + 1)
  print(epoch)
  preds = np.vstack(preds)
  labs = np.vstack(labs)
  f1 = f1_score(np.argmax(labs, axis=1), np.argmax(preds, axis=1))
  accuracy = accuracy_score(np.argmax(labs, axis=1), np.argmax(preds, axis=1))
  precision = precision_score(np.argmax(labs, axis=1), np.argmax(preds, axis=1))
  recall = recall_score(np.argmax(labs, axis=1), np.argmax(preds, axis=1))
  epoch_losses.append(epoch_loss)
  epoch_f1_scores.append(f1)
  epoch_precision_scores.append(precision)
  epoch_recall_scores.append(recall)
print("train",classification_report(np.argmax(labs, axis=1), np.argmax(preds, axis=1)))
print("train",confusion_matrix(np.argmax(labs, axis=1), np.argmax(preds, axis=1)))
gcn_net.eval()

