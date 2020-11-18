f = open("Files/rosalind_orf.txt")
a=(f.read()).split('\n')[:-1]
f.close()

ind = []
i = 0
st=[]
while i < len(a):
    ind.append(a[i][1:])
    i += 1
    DNA = ""
    while (i < len(a)) and (a[i][0] != ">"):
        DNA += a[i]
        i += 1
    st.append(DNA)

s=st[0]

codonD={"TTT":"F","CTT":"L","ATT":"I","GTT":"V","TTC":"F","CTC":"L","ATC":"I","GTC":"V","TTA":"L","CTA":"L","ATA":"I","GTA":"V","TTG":"L","CTG":"L","ATG":"M","GTG":"V","TCT":"S","CCT":"P","ACT":"T","GCT":"A","TCC":"S","CCC":"P","ACC":"T","GCC":"A","TCA":"S","CCA":"P","ACA":"T","GCA":"A","TCG":"S","CCG":"P","ACG":"T","GCG":"A","TAT":"Y","CAT":"H","AAT":"N","GAT":"D","TAC":"Y","CAC":"H","AAC":"N","GAC":"D","TAA":"Stop","CAA":"Q","AAA":"K","GAA":"E","TAG":"Stop","CAG":"Q","AAG":"K","GAG":"E","TGT":"C","CGT":"R","AGT":"S","GGT":"G","TGC":"C","CGC":"R","AGC":"S","GGC":"G","TGA":"Stop","CGA":"R","AGA":"R","GGA":"G","TGG":"W","CGG":"R","AGG":"R","GGG":"G"}

ind=[]
for i in range(len(s)-2):
  if s[i:i+3]=="ATG":
    ind.append(i)

strings=[]
flag=0
for i in ind:
  j=i
  prots=""
  prot=codonD[s[j:j+3]]
  while prot!="Stop":
    prots+=prot
    j+=3
    if j>len(s)-3:
      flag=1
      break
    prot=codonD[s[j:j+3]]
  if flag==1:
    break
  strings.append(prots)

bond={"A":"T","T":"A","C":"G","G":"C"}
rs=""
for nb in s:
  rs+=bond[nb]
rs=rs[::-1]

ind=[]
for i in range(len(s)-2):
  if rs[i:i+3]=="ATG":
    ind.append(i)

flag=0
for i in ind:
  j=i
  prots=""
  prot=codonD[rs[j:j+3]]
  while prot!="Stop":
    prots+=prot
    j+=3
    if j>len(s)-3:
      flag=1
      break
    prot=codonD[rs[j:j+3]]
  if flag==1:
    break
  strings.append(prots)

for p in list(set(strings)):
  print(p)