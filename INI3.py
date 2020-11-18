f = open("Files/rosalind_ini3.txt")
a=(f.read()).split("\n")
f.close()
s=a[0]
lst=list(map(int,a[1].split(" ")))
print(s[lst[0]:lst[1]+1]+" "+s[lst[2]:lst[3]+1])