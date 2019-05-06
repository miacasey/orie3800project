
alpha=1
beta=1
N=5

def V(gamma, clicks, left):
    max_bid= 0
    max_expectation= 0
    if left==0:
        return 0
    else:
        for bid in range(0,101,1):
            expectation=0
            b=bid/10
            p1= 1-(b/10)
            p2= (alpha+gamma)/(alpha+beta+clicks)
            p3= (b/10)-p2
            expectation+= p1*V(gamma,clicks,left-1)
            expectation+= p2*(V(gamma,clicks+1,left-1)-b/2)
            expectation+= p3*(V(gamma+1,clicks+1,left-1)+10-b/2)
            if (expectation>max_expectation):
                max_expectation= expectation
                max_bid= b
    return max_bid

print(V(0,10,1))
