f = open("Files/rosalind_ini2.txt")
a=list(map(int,(f.read()).split(" ")))
f.close()
print(a[0]**2+a[1]**2)