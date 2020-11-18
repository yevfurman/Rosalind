f = open("Files/rosalind_ini5.txt")
a=(f.read()).split("\n")
f.close()
s=""
for i in range(len(a)):
  if i%2!=0:
    s=s+a[i]+'\n'

print(s)