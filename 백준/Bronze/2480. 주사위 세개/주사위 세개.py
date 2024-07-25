f,s,t = map(int,input().split(" "))
l=[]
if f == s == t :
    print(10000+s*1000)
elif f==s and f!=t and s!=t :
    print(1000+f*100)
elif f==t and f!=s and t!=s : 
    print(1000+t*100)
elif t==s and t!=f and s!=f :
    print(1000+s*100)
else :
    l.append(f)
    l.append(s)
    l.append(t)
    print(max(l)*100)