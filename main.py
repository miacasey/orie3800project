
alpha=1
beta=1
N=5

def V(gamma, clicks, left):
    max_bid= 0
    max_expectation= -100
    bid_dict={}
    if left<1:
        return 0
    else:
        for bid in range(0,101,1):
            expectation=0
            b=float(bid/10)
            ##alpha = alpha + gamma
            ##beta = beta + clicks-gamma
            x= (alpha+gamma)/(alpha+beta+clicks)
            p1= 1-(float(b/10))
            p2= float(b/10)*(1-x)
            p3= x*float(b/10)
            expectation+= p1*V(gamma,clicks,left-1)
            expectation+= p2*(V(gamma,clicks+1,left-1)-float(b/2))
            expectation+= p3*(V(gamma+1,clicks+1,left-1)+10-float(b/2))
            print(expectation)
            if (expectation>max_expectation):
                max_expectation= expectation
                max_bid= b
    return max_bid

print(V(5,5,3))
