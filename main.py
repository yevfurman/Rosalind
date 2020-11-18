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
rs=""
for nb in s:
  rs+=bond[nb]
rs=rs[::-1]

for i in range(len(s)):
  for j in range(4,12):
    if i+j>len(s):
      break
    if i==0:
      rev=rs[-i-j:]
    elif i+j==len(s):
      rev=rs[:-i]
    elif i==0 and i+j==len(s):
      rev=rs
    else:
      rev=rs[-i-j:-i]
    if s[i:i+j]==rev:
      print(i+1,j)

def revp(st):
  ans=""
  for nb in st:
    ans+=bond[nb]
  return ans[::-1]