f = open("Files/rosalind_lgis.txt")
a = (f.read()).rstrip()
f.close()

s = a.split("\n")
N=int(s[0])
X=list(map(int," ".join(s[1:]).split( )))

# X=[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
# N=len(X)

P = [0]*N
M = [0]*(N+1)

L = 0
for i in range(N):
    lo = 1
    hi = L
    while lo <= hi:
        mid = -(-(lo+hi)//2)
        if X[M[mid]] < X[i]:
            lo = mid+1
        else:
            hi = mid-1

    newL = lo

    P[i] = M[newL-1]
    M[newL] = i
    
    if newL > L:
        L = newL

S = [0]*L
k = M[L]
for i in range(L-1,-1,-1):
    S[i] = X[k]
    k = P[k]

print(" ".join(map(str,S)))

P = [0]*N
M = [0]*(N+1)

L = 0
for i in range(N):
    lo = 1
    hi = L
    while lo <= hi:
        mid = -(-(lo+hi)//2)
        if X[M[mid]] > X[i]:
            lo = mid+1
        else:
            hi = mid-1

    newL = lo

    P[i] = M[newL-1]
    M[newL] = i
    
    if newL > L:
        L = newL

S = [0]*L
k = M[L]
for i in range(L-1,-1,-1):
    S[i] = X[k]
    k = P[k]

print(" ".join(map(str,S)))