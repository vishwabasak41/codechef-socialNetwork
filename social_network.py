N,M=(input().split(" "))
N=int(N)
M=int(M)
Narray=[]
Narr=[]
newlist_sp=[]
newlist_nsp=[]
sp=[]
nsp=[]
dict={}
final_dict=[]
ans=[]
Narray=(input().split(" "))
for i in range(int(N)):
    val=int(Narray[i])
    Narr.append(val)
#Narr list consisting of no of special friends
for i in range(1,int(M)+1):
    sr,pop,pos=((input().split(" ")))
    pop=int(pop)
    pos=str(pos)
    dict={sr:{
        "popularity":pop,
        "post":pos
    },}
    final_dict.append(dict[sr])
from operator import itemgetter

for i in range(int(M)):
    if final_dict[i]["popularity"] in Narr:
        sp.append(final_dict[i])
        newlist_sp = sorted(sp, key=itemgetter('popularity'), reverse=True)
    else:
        nsp.append(final_dict[i])
        newlist_nsp = sorted(nsp, key=itemgetter('popularity'), reverse=True)
for i in range(int(N)):
    ans.append(newlist_sp[i]['post'])
for i in range(int(M-N)):
    ans.append(newlist_nsp[i]['post'])
for i in range(len(ans)):
    print(ans[i])