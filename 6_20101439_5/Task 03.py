from queue import PriorityQueue

q = PriorityQueue()
file = open("input Task 03.txt")
n = file.readline().split()
temp = list(map(int, file.readline().split()))
temp.sort()

string = file.readline()
sequence = []
jack = []
jill = []
i = 0
j = 0

while i < len(string):
    if string[i] == "J":
        q.put(-(temp[j]))
        sequence.append(temp[j])
        jack.append(temp[j])
        j += 1
    elif string[i] == "j":
        u = q.get()
        u = (-1)*u
        sequence.append(u)
        jill.append(u)
    i += 1

output = open("output Task 03.txt", "w")
for i in sequence:
    output.write(str(i))
output.write("\n")

jack_hour = 0
for j in jack:
    jack_hour += j
output.write("Jack will work for "+ str(jack_hour) + " hours \n")

jill_hour = 0
for k in jill:
    jill_hour += k
output.write("Jill will work for " + str(jill_hour) + " hours \n")
