f = open("Files/rosalind_splc.txt")
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

dnas=strings[0]
for i in range(1,len(strings)):
    dnas=dnas.replace(strings[i],"")

codonD={"TTT":"F","CTT":"L","ATT":"I","GTT":"V","TTC":"F","CTC":"L","ATC":"I","GTC":"V","TTA":"L","CTA":"L","ATA":"I","GTA":"V","TTG":"L","CTG":"L","ATG":"M","GTG":"V","TCT":"S","CCT":"P","ACT":"T","GCT":"A","TCC":"S","CCC":"P","ACC":"T","GCC":"A","TCA":"S","CCA":"P","ACA":"T","GCA":"A","TCG":"S","CCG":"P","ACG":"T","GCG":"A","TAT":"Y","CAT":"H","AAT":"N","GAT":"D","TAC":"Y","CAC":"H","AAC":"N","GAC":"D","TAA":"Stop","CAA":"Q","AAA":"K","GAA":"E","TAG":"Stop","CAG":"Q","AAG":"K","GAG":"E","TGT":"C","CGT":"R","AGT":"S","GGT":"G","TGC":"C","CGC":"R","AGC":"S","GGC":"G","TGA":"Stop","CGA":"R","AGA":"R","GGA":"G","TGG":"W","CGG":"R","AGG":"R","GGG":"G"}
ans=""
i=0
while(codonD[dnas[i:i+3]]!="Stop"):
  ans+=codonD[dnas[i:i+3]]
  i+=3
print(ans)