def assignment_selection(schedule, arr, m):
    max_num = 0
    finish = 0

    for i in range(int(m)):
        for j in schedule:
            if finish <= j[0] and j not in arr:
                finish = j[1]
                max_num += 1
                arr.append(j)
        finish = 0

    output.write(str(max_num))

file = open("input Task 02.txt")
n, m = file.readline().split()
schedule = []
output = open("output Task 02.txt", "w")
for i in range(int(n)):
    temp = list(map(int, file.readline().split()))
    schedule.append(temp)


schedule.sort(key = lambda x: x[1])
arr = []
call = assignment_selection(schedule, arr, m)