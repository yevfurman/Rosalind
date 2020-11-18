f = open("Files/rosalind_iprb.txt")
a=(f.read()).split(" ")
f.close()

k,m,n=int(a[0]),int(a[1]),int(a[2])
Omega=k+m+n
print(round((k*(2*Omega-k-1)+m*(m-1)*0.75+m*n)/Omega/(Omega-1),6))