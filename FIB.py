f = open("Files/rosalind_fib.txt")
s=list(map(int,(f.read()).split(" ")))
f.close()
n=s[0]
k=s[1]
a,b=1,1
for i in range(n-2):
  a,b=b,3*a+b
print(b)