f = open("Files/rosalind_revp.txt")
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

# s="TCAATGCATGCGGGTCTATATGCAT"

bond={"A":"T","T":"A","C":"G","G":"C"}

def revp(st):
  ans=""
  for nb in st:
    ans+=bond[nb]
  return ans[::-1]

for i in range(len(s)):
  for j in range(4,13):
    if i+j>len(s):
      break
    if s[i:i+j]==revp(s[i:i+j]):
      print(i+1,j)