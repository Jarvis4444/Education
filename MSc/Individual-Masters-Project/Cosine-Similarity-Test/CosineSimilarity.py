import numpy as np
from numpy import dot
from numpy.linalg import norm
 
with open("yara.csv") as f:
    lines = f.readlines()
tags = []
apts = []
data = {}
for line in lines[1:]:
    s, a, t = line.strip().split(",")
    apts.append(a)
    tags.append(t)
    if a in data.keys():
        data[a]["tags"].append(t)
        data[a]["samples"].append(s)
    else:
        data[a] = {"tags": [t], "samples": [s]}
for d in data.keys():
    data[d]["cnt"] = len(list(set(data[d]["samples"])))
apts = list(set(apts))
tags = list(set(tags))
apts.sort()
tags.sort()
vectors = []
for a in apts:
    v = []
    for t in tags:
        v.append(round(data[a]["tags"].count(t) / data[a]["cnt"], 2))
    vectors.append({"apt": a, "vector": v})
correlations=[]
for i in range(len(vectors)):
    v1=vectors[i]
    for j in range(i+1,len(vectors)):
        v2=vectors[j]
        if v1["apt"] != v2["apt"]:
            a = v1["vector"]
            b = v2["vector"]
            correlations.append(["%s,%s"% (v1["apt"], v2["apt"]),
                  dot(a, b) / (norm(a) * norm(b))])
correlations.sort(key = lambda x: x[1])
for c in correlations[-100:]:
    print(c[0],round(c[1],2))
