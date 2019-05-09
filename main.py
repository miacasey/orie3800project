import numpy as np
import matplotlib.pyplot as plt

# Number 3
N=5
alpha=1
beta=1
max_bids= np.zeros((N+1,N+1,N+1))
max_exps= np.zeros((N+1,N+1,N+1))
for l in range(1,N+1):
    for c in range(0,N-l+1):
        for g in range(0,c+1):
            max_exp=0
            max_bid=0
            for bid in range(0,101,1):
                b=bid*0.1
                p1= 1-(b/10)
                p2= (b/10)*(1-((alpha+g)/(alpha+beta+c)))
                p3= (b/10)*((alpha+g)/(alpha+beta+c))
                expectation= p1*max_exps[l-1,c,g] + p2*(max_exps[l-1,c+1,g]-(b/2)) + p3*(max_exps[l-1,c+1,g+1]+10-(b/2))
                if expectation > max_exp:
                    max_exp = expectation
                    max_bid= b
            max_bids[l,c,g]= round(max_bid,1)
            max_exps[l,c,g]= max_exp

print(max_bids)

# Number 4
# create tables 
for l in range(1,N+1):
    rows = ['%d C' % x for x in range(0,N+1)]
    columns = ['%d γ' % y for y in range(0,N+1)]
            #print("y:", y, " C:", c, " L:", l, ":::", opt_bid, " ")
    the_table = plt.table(cellText=max_bids[l],
                      rowLabels=rows,
                      colLabels=columns,
                      loc='center'
    ) 
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    plt.tick_params(axis='y', which='both', right=False, left=False, labelleft=False)
    for pos in ['right','top','bottom','left']:
        plt.gca().spines[pos].set_visible(False)
    plt.show()

# Number 5
# initialize arrays for new N value
N=100
max_bids= np.zeros((N+1,N+1,N+1))
max_exps= np.zeros((N+1,N+1,N+1))
for l in range(1,N+1):
    for c in range(0,N-l+1):
        for g in range(0,c+1):
            max_exp=0
            max_bid=0
            for bid in range(0,101,1):
                b=bid*0.1
                p1= 1-(b/10)
                p2= (b/10)*(1-((alpha+g)/(alpha+beta+c)))
                p3= (b/10)*((alpha+g)/(alpha+beta+c))
                expectation= p1*max_exps[l-1,c,g] + p2*(max_exps[l-1,c+1,g]-(b/2)) + p3*(max_exps[l-1,c+1,g+1]+10-(b/2))
                if expectation > max_exp:
                    max_exp = expectation
                    max_bid= b
            max_bids[l,c,g]= max_bid
            max_exps[l,c,g]= max_exp
# plotting average expected value
avg= []
for n in range(1,N+1):
    avg.append(max_exps[n,0,0]/n)
plt.xlabel('N')
plt.ylabel('EV[opt] / N')
plt.plot(avg)
plt.show()

# Number 6
# initialize arrays for new N value
N=50
max_bids= np.zeros((N+1,N+1,N+1))
max_exps= np.zeros((N+1,N+1,N+1))
for l in range(1,N+1):
    for c in range(0,N-l+1):
        for g in range(0,c+1):
            max_exp=0
            max_bid=0
            for bid in range(0,101,1):
                b=bid*0.1
                p1= 1-(b/10)
                p2= (b/10)*(1-((alpha+g)/(alpha+beta+c)))
                p3= (b/10)*((alpha+g)/(alpha+beta+c))
                expectation= p1*max_exps[l-1,c,g] + p2*(max_exps[l-1,c+1,g]-(b/2)) + p3*(max_exps[l-1,c+1,g+1]+10-(b/2))
                if expectation > max_exp:
                    max_exp = expectation
                    max_bid= b
            max_bids[l,c,g]= max_bid
            max_exps[l,c,g]= max_exp
# plotting difference
deltas= []
for i in range (1,N+1):
    deltas.append((max_bids[i,0,0])-5)

plt.xlabel('N')
plt.ylabel('∆ L')
plt.plot(deltas)
plt.show()