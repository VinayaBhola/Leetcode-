s="man"
s_norm=0
s_rev=len(s)-1
while (s_norm<s_rev):
    if s[s_norm]!=s[s_rev]:
        print("not")
        break
    s_norm+=1 
    s_rev-=1
else:
    print("yes")    