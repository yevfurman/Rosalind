f = open("Files/rosalind_lexf.txt")
a = (f.read()).rstrip()
f.close()

s = a.split("\n")

alphabet=s[0].replace(" ","")
n=int(s[1])
import itertools

for x in sorted(["".join(list(tup)) for tup in [p for p in itertools.product(alphabet,repeat=n)]], key=lambda word: [alphabet.index(c) for c in word]):
    print(x)
