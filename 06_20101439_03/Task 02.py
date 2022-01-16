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
queue = []
output = open("output task 02.txt", "w")

def BFS(visited, graph, node, endpoint):
    string = ""
    visited.append(node)
    queue.append(node)

    while queue:
        u = queue.pop(0)
        string += str(u) + " "
        if u == endpoint:
            break
        for neighbour in graph[u]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    output.write(string)
BFS(visited, adj_dict, 1, 12)