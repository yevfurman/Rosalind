f = open("Files/rosalind_prot.txt")
s=f.read()
f.close()

codon={"UUU":"F","CUU":"L","AUU":"I","GUU":"V","UUC":"F","CUC":"L","AUC":"I","GUC":"V","UUA":"L","CUA":"L","AUA":"I","GUA":"V","UUG":"L","CUG":"L","AUG":"M","GUG":"V","UCU":"S","CCU":"P","ACU":"T","GCU":"A","UCC":"S","CCC":"P","ACC":"T","GCC":"A","UCA":"S","CCA":"P","ACA":"T","GCA":"A","UCG":"S","CCG":"P","ACG":"T","GCG":"A","UAU":"Y","CAU":"H","AAU":"N","GAU":"D","UAC":"Y","CAC":"H","AAC":"N","GAC":"D","UAA":"Stop","CAA":"Q","AAA":"K","GAA":"E","UAG":"Stop","CAG":"Q","AAG":"K","GAG":"E","UGU":"C","CGU":"R","AGU":"S","GGU":"G","UGC":"C","CGC":"R","AGC":"S","GGC":"G","UGA":"Stop","CGA":"R","AGA":"R","GGA":"G","UGG":"W","CGG":"R","AGG":"R","GGG":"G"}
ans=""
i=0
while(codon[s[i:i+3]]!="Stop"):
  ans+=codon[s[i:i+3]]
  i+=3
print(ans)