import numpy as np

alpha=1
beta=1
N=5

def V(gamma, clicks, left):
    bids_exp = {}
    if left==0:
        return 0
    else:
        for bid in range(0,101,1):
            expectation=0
            b=bid/10
            p1= 1-(b/10)
            p3= (b/10)*(alpha+gamma)/(alpha+beta+clicks)
            p2= (b/10)*(1-((alpha+gamma)/(alpha+beta+clicks)))
            expectation+= p1*V(gamma,clicks,left-1)
            expectation+= p2*(V(gamma,clicks+1,left-1)-b/2)
            expectation+= p3*(V(gamma+1,clicks+1,left-1)+10-b/2)
            bids_exp[b]= expectation

    max_exp= max(bids_exp.values())
    return max_exp

def makeTable(N):
    table= np.zeros((N,N,N))
    for l in range(N,0,-1):
        for c in range(N-l+1):
            for g in range(c+1):
                table[l,g,c]= V(g,c,l)
                print(V(g,c,l))
    return(table)

# print(makeTable(N))
print(V(10,10,2))
print(V(0,10,2))
print(V(0,0,5))
