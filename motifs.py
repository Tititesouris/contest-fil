'''
mot = input()
n = int(input())
motifs = [input() for _ in range(n)]
'''
mot = "abba"
n = 11
motifs = ["*", "a*", "*a", "*b*", "abb*a", "a*b*a", "a*b*b*a*", "*bab*", "*b", "b*", "*bbb*a"]

for i in range(n):
    motif =  motifs[n]
    motifLen = len(motif)
    fit = ""
    for j in range(motifLen):
        c = motif[j]
        if c == "*":
            if j == motifLen-1:
                print("oui" if motifs[n].startswith(fit) else "non")
        else:
            fit += c