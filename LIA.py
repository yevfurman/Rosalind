f = open("Files/rosalind_lia.txt")
a=list(map(int,(f.read()).split(" ")))
f.close()

k=a[0]
N=a[1]

from math import factorial as fact
summ=0
for i in range(N):
  summ+=(3**(2**k-i))*fact(2**k)//fact(2**k-i)//fact(i)
print(1-summ/4**(2**k))