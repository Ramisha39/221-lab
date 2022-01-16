f = open("input problem 04.txt")

x = f.read()

temp = x.split("\n")

t = temp[1].split(" ")

arr = []
for k in t:
    k = int(k)
    arr.append(k)
print(arr)
