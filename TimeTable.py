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
def dailytime():
    for a in classes:
        for i in range (8):
            for j in range(6):
                temp=list(a[j])
                if a==classes[0]:
                    x=random.choice(temp)
                    temp.remove(x)
                    day[j].append(x)
                elif a==classes[1]:
                    x=random.choice(temp)
                    temp.remove(x)
                    day[j+len(classes[0])].append(x)
                
                
    if d==3:
        for i in day:
            i[0],i[1]='Worksheet','Worksheet'
            
            
import random
sections9=6
sections10=6
sections=sections9+sections10
d={}
for i in teachers:
    d[i]=0
day=[]
week=[]
for i in range (sections):
    day.append([])
    week.append([])

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
classes=[ninth,tenth]
d=1

for i in range(5):
    dailytime()
    d+=1
    for j in range(sections):
        week[j].append(day[j])
    day.clear()
    for i in range (sections):
        day.append([])
a=0   
for i in week[:sections9]:
    print(a)
    a+=1
    for j in i:
        print(j)
        print()
a=0
for i in week[sections9:]:
    print(a)
    a+=1
    for j in i:
        print(j)
        print()
        

    
     

