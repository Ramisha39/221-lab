file = open("input task 01.txt")
n = file.readline()
x = file.readline().strip()
y = file.readline().strip()

def LCS(n, x, y):
    dict = {'Y':"Yasnaya",'P':"Pochinki",'S':"School",'R':"Rozhok",'F':"Farm",'M':"Mylta",'H':"Shelter",'I':"Prison"}

    m = len(x)+1
    n = len(y)+1
    c = {}

    for i in range(m):
        c[i, 0] = 0
    for j in range(n):
        c[0, j] = 0
    for i in range(1, m):
        for j in range(1, n):
            if x[i-1] == y[j-1]:
                c[i, j] = c[(i-1, j-1)] + 1
            elif c[(i-1), j] >= c[(i, j-1)]:
                c[(i, j)] = c[(i-1, j)]
            else:
                c[(i, j)] = c[(i, j-1)]

    percentage = (c[(m-1), (n-1)]*100)//(n-1)

    i = m-1
    j = n-1
    li = []
    while i > 0 and j > 0:
        if x[i-1] == y[j-1]:
            li.append(x[i-1])
            i -= 1
            j -= 1
        else:
            if c[(i-1, j)] > c[(i, j-1)]:
                i -= 1
            else:
                j -= 1

    string = ""
    output = open("output task 01.txt", "w")
    for i in li[-1::-1]:
        if i in dict:
            string += str(dict[i]) + " "
    output.write(string)
    output.write("Correctness of prediction: " + str(percentage) + "%")

LCS(n, x, y)

