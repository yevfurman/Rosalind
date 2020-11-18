f = open("Files/rosalind_subs.txt")
a=(f.read()).split("\n")
f.close()

s=a[0].rstrip()
t=a[1].rstrip()

lst=[]
for i in range(len(s)-len(t)):
  if s[i:i+len(t)]==t:
    lst.append(i+1)

ans=""
for i in lst:
  ans+=str(i)+" "
print(ans[:-1])