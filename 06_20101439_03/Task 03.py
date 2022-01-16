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

visited = []
color = {}
parent = {}
traversal_time = {}
printed = []

for vertices in adj_dict.keys():
    color[vertices] = "W"
    parent[vertices] = None
    traversal_time[vertices] = [-1, -1]

time = 0

def DFS(adj_dict):
    for v in adj_dict.keys():
        # global time
        if color[v] == "W":
            DFS_visit(v, endpoint)

def DFS_visit(u, endpoint):
    string = ""
    global time
    color[u] = "G"
    time += 1
    traversal_time[u][0] = time
    printed.append(u)
    for node in adj_dict[u]:
        if color[node] == "W":
            parent[node] = u
            DFS_visit(node, endpoint)

    color[u] = "B"
    time += 1
    traversal_time[u][1] = time

    output = open("output task 03.txt", "w")
    string = ""

    for i in printed:
        string += str(i) + " "
        if i == endpoint:
            break

    output.write(string)


DFS_visit(1, 12)






