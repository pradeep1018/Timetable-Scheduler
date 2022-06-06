ans=[]
courses=open('input3.txt')
g=[]
while True:
    k=courses.readlines(1)
    if(len(k)!=0):
        g.append(k[0].split())
    else:
        break
courses.close

students=open('students.txt')
a=[]
for i in range(10):
    j=[]
    for i in range(5):
        k=students.readlines(1)
        j.append(k[0].split())
    a.append(j)
students.close
def dim3(m):
    l=[]
    l3=[]
    f=open(m,"r")
   
    k=f.read()
    f.close()
    start=k.find("\n")+2
    end=k.find("\n",start)
    if(end==-1):
        end=len(k)
    while(start<end):
        i=start
        n=0
        while(i<end):
            if(k[i]!=","):
                j=min(k.find("\n",i),k.find(",",i))
                if(k[i:j] not in l):
                    l.append(k[i:j])
                    if(n==3):
                        l3.append([str((8+n)%12)+"-"+str(12)])
                    elif(n==4):
                        l3.append([str(12)+"-"+str((9+n)%12)])    
                    else:
                        l3.append([str((8+n)%12)+"-"+str((9+n)%12)])
                else:
                    for m in range(len(l)):
                        if(l[m]==k[i:j]):
                            if(n==3):
                                l3[m].append(str((8+n)%12)+"-"+str(12))
                            elif(n==4):
                                l3[m].append(str(12)+"-"+str((9+n)%12))  
                            else:
                                l3[m].append(str((8+n)%12)+"-"+str((9+n)%12))  
                i=j-1
            if(k[i]==","):
                n=n+1
            i=i+1
            if(i==-1):
                i=end
        start=end+2
        end=k.find("\n",start)
        if(end==-1):
            end=len(k)
    return l,l3
def Maxz(g,a,r):
    f=[0,0,0]
    for i in range(10):
        for j in range(3):
            if(a[i][r][j]=='1'):
                f[j]+=1
    for i in range(3):
        temp=f[i]
        f[i]=[temp,g[r][i]]
    return Sort(f)
def Sort(l):
    for i in range(len(l)-1):
        if(l[0][0]<l[1][0]):
            temp=l[0]
            l[0]=l[1]
            l[1]=temp
        if(l[1][0]<l[2][0]):
            temp=l[1]
            l[1]=l[2]
            l[2]=temp
    return l
def arr(g):
    ar=[]
    for i in range(5):
        ar.append(Maxz(g,a,i))
    return ar
def present(r,l):
    count=0
    for i in l:
        if(r==l[i]):
            count=1
            break
    if(count==0):
        return 0
    else:
        return 1
sublist,nig=dim3("input1.csv")
ar=arr(nig)
bruh=[]
newlist=[]
for i in range(len(ar)):
    for j in range(len(ar[i])):
        
        x=ar[i][j][1].split("-")
        x.remove(x[1])
        x.insert(0,ar[i][j][0])
        for k in range(len(x)):
            x[1]=int(x[1])
        newlist.append(x)
    bruh.append(newlist)
    newlist=[]
newlist=[8,9,10,11,12,2,3,4,5]
newbruh=[0,0,0,0,0,0,0,0,0]
matchcount=0

shit=[]
for i in range(len(bruh)):
    shit.append(0)
i=0
while(i<len(bruh)):
    k=bruh[i][0][1]
    kk=ans.count(k)
    if(kk!=0):
        kk=ans.index(k)
        k=bruh[i][shit[i]][0]
        j=bruh[kk][shit[kk]][0]
        if(k>j):
            ans[kk]=bruh[kk][shit[kk]][1]
            ans.append(bruh[i][shit[i]][1])
            shit[i]+=1
            shit[kk]+=1
        elif(k<j):
            ans.append(bruh[i][shit[i]][1])
            shit[i]+=1
            shit[kk]+=1
            i+=1
        elif(k==j):
            k=bruh[i][1][1]
            j=bruh[kk][shit[kk]][1]
            if(k!=j):
                ans.append(bruh[kk][shit[kk]][1])
                i+=1
            else:
                i+=1
    else:
        ans.append(k)
        shit[i]=shit[i]+1
        i+=1
def tocsv(t,subject):
    f=open("output1.csv","w")
    f.write("Slots,8AM to 9AM,9AM to 10AM,10AM to 11AM,11AM to 12PM,12PM to 1PM,LUNCH,2PM to 3PM,3PM to 4PM,4PM to 5PM, 5PM to 6PM")
    f.write("\n")
    d={}
    for i in range(len(t)):
        d[t[i]]=subject[i]
    f.write(",")
    for i in range(8,13):
        if(i in d):
            f.write(d[i]+",")
        else:
            f.write(",")
    f.write(",")
    for i in range(2,6):
        if(i in d):
            f.write(d[i]+",")
        else:
            f.write(",")
tocsv(ans,sublist)