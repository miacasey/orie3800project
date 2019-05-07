import numpy as np
import operator

alpha=1
beta=1
N=5

# bid_dict={}
# max_expectation=0:
# for L in range(0,N+1):
#     for C in range(0, N-L+1):
#         for G in range(0, C):
#             for bid in range(0,101,1):
#                 expectation=0
#                 b=bid/10
#                 expectation=1-(b/10)


##Number 2
bids_exp = {}
#for bid in range(0,101,1):
    # expectation=0
    # b=bid/10
    # p1= 1-(b/10)
    # p3= (b/10)*(alpha+gamma)/(alpha+beta+clicks)
    # p2= (b/10)*(1-((alpha+gamma)/(alpha+beta+clicks)))
max_bids= np.zeros((N+1,N+1,N+1))

for l in range(0,N+1):
    for c in range(0,N-l+1):
        for g in range(0,c+1):
            max_exp=0
            max_bid=0
            x= (alpha+g)/(alpha+beta+c)
            if (l==0):
                max_bids[l,c,g]
            else:
                for bid in range(0,101,1):
                    b=bid/10
                    p1= 1-(b/10)
                    p3= (b/10)*x
                    p2= (b/10)*(1-x)
                    # expectation = p1 + p2*(-b/2) + p3*(10-b/2)
                    expectation = p1*max_bids[l-1,c,g] + p2*(max_bids[l-1,c+1,g]-b/2) + p3*(max_bids[l-1,c+1,g+1]+10-b/2)
                    if expectation > max_exp:
                        max_exp = expectation
                        max_bids[l,c,g]
                        max_bid= bid
print(max_bids)
                #expectation+= p1*V(gamma,clicks,left-1)
                #expectation+= p2*(V(gamma,clicks+1,left-1)-b/2)
                #expectation+= p3*(V(gamma+1,clicks+1,left-1)+10-b/2)


# max_exp= max(bids_exp.values())
# max_bid= max(bids_exp.items(),  key=operator.itemgetter(1))
##print(max_bid)
# return max_exp

##need to keep track of largest expected value
##use bottom up version of for loop
##just call the largest expected value so far

##Number 3
# def makeTable(N):
#     table= np.zeros((N+1,N+1,N+1))
#     for l in range(N+1):
#         for c in range(N+1-l):
#             for g in range(c+1):
#                 table[l,g,c]= V(g,c,l)
#                 print(V(g,c,l))
#     return(table)
#
# ##Number 4
# def tabOptBid(N):
#     for L in range(0, N+1):
#         for C in range(0, N+1-L):
#             for y in range(0, C+1):
#                 opt_bid = V(y, C, L)
#                 print("y:", y, " C:", C, " L:", L, ":::", opt_bid, " ")
##tabOptBid(3)

# print(makeTable(N))
##print(V(10,10,2))
#print(V(0,10,2))
