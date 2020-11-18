f = open("Files/rosalind_grph.txt")
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
graph=""
for i in range(len(strings)):
  for j in (list(range(i))+list(range(i+1,len(strings)))):
    if strings[i][-3:]==strings[j][:3]:
      graph+=ind[i]+" "+ind[j]+'\n'

print(graph)

ansfile = open("Answers/Answer GRPH.txt", "w")
n = ansfile.write(graph)
ansfile.close()