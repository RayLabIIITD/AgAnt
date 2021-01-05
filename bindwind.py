import glob
import numpy as np
import json
for filename in glob.glob("ago_bind/*.pdb"):
    print(filename)
    with open(filename) as fp:
        fp = fp.read()
    fp=fp.splitlines()
    for i in fp:
        #print(i[17:20])
        if i[17:20]=="STP":
            print(i)
    break