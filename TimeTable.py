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

def dailytime():
    print('a')
    temp=list(teachers)
    for i in range (8):
        for j in range(sections):
            x=random.choice(temp)
            temp.remove(x)
            day[j].append(x)
        temp=list(teachers)
    if d==3:
        for i in day:
            i[0],i[1]='Worksheet','Worksheet'
            
import random
sections9=6
sections10=6
sections=sections9+sections10
day=[]
week=[]
for i in range (sections):
    day.append([])
    week.append([])

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
for i in week[:6]:
    print(a)
    a+=1
    for j in i:
        print(j)
        print()
a=0
for i in week[6:]:
    print(a)
    a+=1
    for j in i:
        print(j)
        print()
        
#%%
for i in week:
    print(a)
    a+=1
    for j in i:
        print(j)
        print()
    
     

