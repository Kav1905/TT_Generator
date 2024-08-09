#%%
f=open('a','w')
x=input()
f.write(x)
f.close()
f=open('a','r')

teachers=x.split('\n')
f.close()
print(teachers)

#%%
def assign():
    a=1
    c=[]
    for i in range(14):
        l=[]
        for j in temp:
            x=int(j[:2])
            if x==a:
                l.append(j)
            elif x>a:
                break
            else:
                pass
                
        a+=1
        c.append(random.choice(l))
    return c

def check(sec):
    for i in teachers:
        d[i]=d[i]+c.count(i)
    sec.append(c)
    for i in temp:
        x=int(i[:2])
        if x in [1,9,10]:
            if d[i]==2:
                temp.remove(i)
        elif x not in [11,12,13,14]:
            if d[i]==3:
                temp.remove(i)
    return sec
         
import random
sections9=6
sections10=6
sections=sections9+sections10
d={}
for i in teachers:
    d[i]=0
ninth=[]
tenth=[]
temp=list(teachers)
for i in range (sections):
    if i<sections9:
        c=assign()
        ninth=check(ninth)
    elif i==sections9:
        temp=list(teachers)
        d={}
        for i in teachers:
            d[i]=0
        c=assign()
        tenth=check(tenth)
    elif i>sections9:
        c=assign()
        tenth=check(tenth)
print('9th')
a=1
for i in ninth:
    print(a)
    a+=1
    print (i)  
print('10th')
a=1
for i in tenth:
    print(a)
    a+=1
    print (i)  
#%%
for i in ninth:
    print (i)  
for i in tenth:
    print (i)  
