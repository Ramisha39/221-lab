from queue import PriorityQueue
import sys

def dijkstra(graph, source):
    inf = sys.maxsize
    q = PriorityQueue()
    dist = [inf]*(len(graph)+1)
    visited = [False]*(len(graph)+1)
    prev = [None]*(len(graph)+1)
    dist[source] = 0
    q.put((dist[source], source))

    while not q.empty():

        u = q.get()[1]
        if visited[u]:
            continue
        visited[u] = True

        for neighbour in graph[u]:

            alt = dist[u] + neighbour[1]


            if alt < dist[neighbour[0]]:

                dist[neighbour[0]] = alt
                prev[neighbour[0]] = u
                q.put((dist[neighbour[0]], neighbour[0]))

    print(prev)
    i = len(prev) - 1
    li = []

    while i != 1:
        li.append(i)
        print(li)
        i = prev[i]
        print(i)
    li.append(1)

    for j in range(len(li)-1, -1, -1):
        output.write(str(li[j]) + "  ")
    output.write("\n")


file = open("input 01.txt")
line = file.readline().strip()
output = open("output task 02.txt", "w")
for i in range(int(line)):
    temp = list(map(int, file.readline().split()))
    n = temp[0]
    m= temp[1]
    dict = {}

    for j in range(m):
        t = list(map(int, file.readline().split()))
        u = t[0]
        v = t[1]
        w = t[2]
        dict.setdefault(u, []).append([v,w])
        dict.setdefault(v, []).append([u, w])

    if m == 0:
        output.write(str(n) + "\n")
    else:
        dijkstra(dict, 1)


