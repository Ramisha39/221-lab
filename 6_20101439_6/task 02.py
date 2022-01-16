file = open("input task 02.txt")
s1 = file.readline().strip()
s2 = file.readline().strip()
s3 = file.readline().strip()

def LCS(s1, s2, s3):
    m = len(s1) + 1
    n = len(s2) + 1
    o = len(s3) + 1
    c = []
    for i in range(m):
        c.append([])
        for j in range(n):
            c[i].append([])
            for k in range(o):
                c[i][j].append(0)

    for i in range(1, m):
        for j in range(1, n):
            for k in range(1, o):
                if i == 0 or j == 0 or k == 0:
                    c[i][j][k] = 0
                else:
                    if s1[i-1] == s2[j-1] and s2[j-1] == s3[k-1]:
                        c[i][j][k] = c[i-1][j-1][k-1] + 1
                    else:
                        c[i][j][k] = max({c[i-1][j][k], c[i-1][j-1][k], c[i][j-1][k-1], c[i][j-1][k], c[i][j][k-1], c[i-1][j][k-1]})

    ans = c[m - 1][n - 1][o - 1]
    output = open("output task 02.txt", "w")
    output.write(str(ans))

LCS(s1, s2, s3)
