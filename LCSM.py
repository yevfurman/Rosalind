def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and is_substr(data[0][i:i+j], data):
                    substr = data[0][i:i+j]
    return substr

def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True

f = open("Files/rosalind_lcsm.txt")
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

print (long_substr(strings))