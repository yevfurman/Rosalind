f = open("Files/rosalind_hamm.txt")
a=(f.read()).split("\n")
f.close()

summ=0
for i in range(len(a[0])):
  if a[0][i]!=a[1][i]:
    summ+=1
print(summ)