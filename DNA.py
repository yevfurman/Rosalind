f = open("Files/rosalind_dna.txt")
DNA=(f.read()).rstrip()
f.close()

ans=""
bases=["A","C","G","T"]
for base in bases:
  ans=ans+str(DNA.count(base))+" "
print(ans[:-1])