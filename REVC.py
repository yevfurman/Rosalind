f = open("Files/rosalind_revc.txt")
DNA=(f.read()).rstrip()
f.close()
bond={"A":"T","T":"A","C":"G","G":"C"}
RNA=""
for nb in DNA:
  RNA+=bond[nb]
RNA=RNA[::-1]
print(RNA)