import numpy as np
import operator
import matplotlib.pyplot as plt

alpha=1
beta=1
N=3

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
max_exps= np.zeros((N+1,N+1,N+1))

for l in range(1,N+1):
    for c in range(0,N-l+1):
        for g in range(0,c+1):
            max_exp=0
            max_bid=0
            x= (alpha+g)/(alpha+beta+c)
            for bid in range(0,101,1):
                b=bid/10
                p1= 1-(b/10)
                p3= (b/10)*x
                p2= (b/10)*(1-x)
                # expectation = p1 + p2*(-b/2) + p3*(10-b/2)
                expectation= p1*max_bids[l-1,c,g] + p2*(max_bids[l-1,c+1,g]-b/2) + p3*(max_bids[l-1,c+1,g+1]+10-b/2)
                if expectation > max_exp:
                    max_exp = expectation
                    max_bid= b
                    max_bids[g,c,l]= max_bid
                    max_exps[g,c,l]= max_exp
# print(max_bids)
print(max_exps)
print(max_exps[0,0,1])
print(max_exps[1,1,1])
print(max_exps[2,2,1])
print(max_exps[3,3,1])
print(max_exps[4,4,1])


avg_x = []
avg_y = [] 
for n in range(1,N+1): 
    avg_x.append(n)
    avg_y.append(max_exps[n-1,n-1,1]/n)

print(avg_x)
print(avg_y)
# plt.plot(avg_x, avg_y)
# plt.show()


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
# for L in range(1, N+1):
#     for C in range(0, N+1-L):
#         for y in range(0, C+1):
#             opt_bid = max_exps[y,C,L]
#             print("y:", y, " C:", C, " L:", L, ":::", opt_bid, " ")

# ##Number 5 

# avg=[]
# for n in range(1, 21): 
#     avg[n] = max_exps[0,0,n]/n

# print(avg)
