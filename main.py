
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
    print(max_exp)
    return max(bids_exp, key=bids_exp.get)

print(V(0,10,1))
