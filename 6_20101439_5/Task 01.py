def assignment_selection(schedule, arr):
    # print(schedule)
    max_num = 0
    finish = 0
    for j in schedule:
        if finish <= j[0]:
            finish = j[1]
            max_num += 1
            arr.append(j)
    output.write(str(max_num)+"\n")

    for ele in arr:
        for e in ele:
            output.write(str(e) + " ")
        output.write("\n")


file = open("input Task 01.txt")
line = file.readline()
schedule = []
output = open("output Task 01.txt", "w")
for i in range(int(line)):
    temp = list(map(int, file.readline().split()))
    schedule.append(temp)

schedule.sort(key = lambda x: x[1])
arr = []
call = assignment_selection(schedule, arr)
