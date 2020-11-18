f = open("Files/rosalind_gc.txt")
a = (f.read()).rstrip()
f.close()

s = a.split("\n")
ind = []
cnt = []
i = 0
while i < len(s):
    ind.append(s[i][1:])
    i += 1
    DNA = ""
    while (i < len(s)) and (s[i][0] != ">"):
        DNA += s[i]
        i += 1
    cnt.append((DNA.count("C") + DNA.count("G")) / len(DNA) * 100)

i = cnt.index(max(cnt))
print(ind[i])
print(round(cnt[i], 6))