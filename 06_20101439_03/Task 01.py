file = open("input task 01.txt")
x = file.read()
line = x.split("\n")
temp = []

for i in line:
    t = list(map(int, i.split()))
    temp.append(t)

adj_dict = {}
for j in temp[1::]:
    adj_dict[j[0]] = j[1::]

output = open("output task 01.txt", "w")
string = ""
for u, v in adj_dict.items():
    string = string + str(u) + "-->" + str(v) + "\n"
output.write(string)



