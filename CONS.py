f = open("Files/rosalind_cons.txt")
a = (f.read()).rstrip()
f.close()

s = a.split("\n")
ind = []
cnt = []
i = 0
strings=[]
while i < len(s):
    ind.append(s[i][1:])
    i += 1
    DNA = ""
    while (i < len(s)) and (s[i][0] != ">"):
        DNA += s[i]
        i += 1
    strings.append(DNA)
profile=[]
for i in range(len(strings[0])):
  col="".join([x[i] for x in strings])
  profile.append([col.count("A"),col.count("C"),col.count("G"),col.count("T")])

consensus=""
for col in profile:
  consensus+="ACGT"[col.index(max(col))]
print('START HERE\n\n\n')
print(consensus)
print("A: "+" ".join([str(w[0]) for w in profile]))
print("C: "+" ".join([str(w[1]) for w in profile]))
print("G: "+" ".join([str(w[2]) for w in profile]))
print("T: "+" ".join([str(w[3]) for w in profile]))