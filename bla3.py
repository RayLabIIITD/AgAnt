import json
import numpy as np
with open("input.json") as fp:
    abc=json.load(fp)
temp=[]
for i in abc:
    print(np.array(i).shape)
    temp.append(np.array(i))
