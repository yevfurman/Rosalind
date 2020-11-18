f = open("Files/rosalind_iev.txt")
a = (f.read())
f.close()

s = list(map(int,a.split(" ")))

print(2*(sum(s[:3])+3*s[3]/4+s[4]/2))