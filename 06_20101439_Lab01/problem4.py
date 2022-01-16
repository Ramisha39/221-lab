file = open("input_problem4.txt")
a = []
b = []

mat = a

for line in file:
    if "," not in line:
        mat = b
    else:
        mat.append([])
        for l in line.split(','):
            mat[len(mat) - 1].append(int(l))


def multiply_matrix(a, b):

    n = len(a)
    c = []
    for i in range(len(a)):
        m = []
        for j in range(len(a)):
            m.append(0)
        c.append(m)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]

    output = open("output_problem4.txt", 'w')

    for i in c:
        for j in i:
            output.write(str(j) + " ")
        output.write("\n")
    output.close()

call = multiply_matrix(a, b)
file.close()



