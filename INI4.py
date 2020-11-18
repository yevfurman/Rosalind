f = open("Files/rosalind_ini4.txt")
a=list(map(int,(f.read()).split(" ")))
f.close()
summ=0
for i in range(a[0],a[1]+1):
  if i%2!=0:
    summ+=i
print(summ)