import urllib.request
import re

f = open("Files/rosalind_mprt.txt")
a = (f.read()).rstrip()
f.close()

s = a.split("\n")
mtch=[]

for id in s:
  url="https://www.uniprot.org/uniprot/"+id+".fasta"
  uf = urllib.request.urlopen(url)
  string = "".join(str(uf.read()).split('\\n')[1:-1])
  mtch=[str(m.start(0)+1) for m in re.finditer("(?=N([^P][ST][^P]))", string)]
  if len(mtch)>0:
    print(id)
    print(" ".join(mtch))