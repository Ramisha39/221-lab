file = open("input problem 02.txt")
x = file.read()
temp = x.split("\n")
n, m = temp[0].split(" ")

t = temp[1].split(" ")
arr = []
for ele in t:
    ele = int(ele)
    arr.append(ele)

for i in range(int(n)-1):
    min = i
    for j in range(i+1, int(n)):
        if arr[j] < arr[min]:
            min = j

    if min != i:
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp

string = ""
count = 0
for k in range(int(m)):
    if count != 0:
        string += " " + str(arr[k])
    else:
        string += str(arr[k])
    count += 1

output = open("output problem 02.txt", "w")
output.write(string)