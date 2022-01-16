file = open("input problem 03.txt")

x = file.read()
temp = x.split("\n")

li1 = temp[1].split(" ")
id = []
for i in range(len(li1)):
    id.append(int(li1[i]))

li2 = temp[2].split(" ")
mark = []
for i in range(len(li2)):
    mark.append(int(li2[i]))

def insertion_sort(id, mark):

    i = 1
    while i < len(mark):
        val = id[i]
        temp = mark[i]
        j = i - 1

        while j >= 0 and mark[j] < temp:
            mark[j+1] = mark[j]
            id[j+1] = id[j]
            j -= 1
        mark[j+1] = temp
        id[j+1] = val
        i += 1


insertion_sort(id, mark)

output = open("output problem 03.txt", "w")
string = ""
for k in range(len(id)):
    string += str(id[k]) + " "
output.write(string)