f = open("Files/rosalind_fibd.txt")
s=list(map(int,(f.read()).split(" ")))
f.close()
n=s[0]
m=s[1]

young,old=1,[0]*(m-1)
tot=young+sum(old)

for i in range(n-1):
  young,old=sum(old),[young]+old[:-1]

print(young+sum(old))