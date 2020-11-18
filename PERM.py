import itertools

f = open("Files/rosalind_perm.txt")
n = int((f.read()).rstrip())
f.close()

l=list(itertools.permutations(list(range(1,n+1))))

print(len(l))
for i in l:
  print(" ".join(list(map(str,i))))