# Author: KASHIF HUSSAIN TALPUR, Postdoc Fellow, UESTC, Chengdu, China.
# LinkedIn: https://www.linkedin.com/in/kashif-hussain-datascientist/
# ResearchGate: https://www.researchgate.net/profile/Kashif_Hussain5
# Date: Jan 28, 2019
# Email: usitsoft@hotmail.com

# Please refer to ReadMe.PDF for greater detail.

# =========================
# SHORTEST PATH ALGORITHM
# =========================

import numpy as np

# Load data from .mis file to list m. 
f = open("F:\\Python\\Shortest Path Graph\\KSPA\\casestudy3.mis", "r", encoding="utf-8")
m=[];
temp=1;
for row in f:    
    if temp==1:
        n=int(row[:].split()[2])
    else:      
        m.append(list(map(int, row[2:-1].split())))
    temp+=1

# Create matrix that contains information about edges between nodes. Value 1 represents an edge between two nodes represented by row and column. 
e=max(max(m))
print("The graph contains ", n, " nodes and ", e, " edges.")
mapData=np.zeros((e,e))
for i in range(0,(np.shape(m)[0])):
    r=m[i][0]-1
    c=m[i][1]-1
    mapData[r][c]=1
    mapData[c][r]=1    

# Inputs: find shortest path between nodes s and t.
s=1 # From node 1
t=10 # To node 10
print("Shortest path between nodes ",s," and ",t)
s-=1
t-=1
if t>n-1:
    t=n-1
path=[]
temp=s
while(True):
    for j in range(0,t+1):
        if mapData[temp][j]==1:
            r=temp; c=j;    
    temp=c
    path.append([r,c])
    print("e", r+1,c+1) # Display edge from node A to node B
    if c==t:
        break

