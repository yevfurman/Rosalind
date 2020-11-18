f = open("Files/rosalind_ini6.txt")
s=(f.read()).split(" ")
f.close()
s=[w.rstrip() for w in s]
ans=""
for w in set(s):
  ans=ans+w+" "+str(s.count(w))+'\n'
print('\nStart here\n')
print(ans)