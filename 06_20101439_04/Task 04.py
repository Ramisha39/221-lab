from queue import PriorityQueue
import sys

def network(graph, source, nodes):
    inf = sys.maxsize
    q = PriorityQueue()
    dist = [-inf]*(nodes+1)
    prev = [None]*(nodes + 1)
    dist[source] = inf
    q.put((-1*dist[source], source))

    while not q.empty():

        u = q.get()[1]

        for neighbour in graph[u]:
            alt = min(dist[u], neighbour[1])
            # print("alt", alt)
            print("neighbour[0", dist[neighbour[0]])
            if alt > dist[neighbour[0]]:
                dist[neighbour[0]] = alt
                prev[neighbour[0]] = u
                q.put((-1 * dist[neighbour[0]], neighbour[0]))
                print(q.queue)

            # if alt < dist[neighbour[0]]:
            #
            #     dist[neighbour[0]] = alt
            #     q.put((dist[neighbour[0]], neighbour[0]))

    for i in range(len(dist)):
        if (dist[i] == inf):
            dist[i] = 0
        if (dist[i] == -inf):
            dist[i] = -1

    for ele in dist[1::]:
        # print(ele)
        output.write(str(ele) + " ")
    output.write("\n")


file = open("input 02.txt")
line = file.readline().strip()
output = open("output task 04.txt", "w")
for i in range(int(line)):
    temp = list(map(int, file.readline().split()))
    n = temp[0]
    m= temp[1]
    dict = {}
    for i in range(1, n+1):
        dict[i] = []
    for j in range(m):
        t = list(map(int, file.readline().split()))
        u = t[0]
        v = t[1]
        w = t[2]
        dict[u].append([v, w])
    print(dict)
    src = file.readline().strip()
    if len(dict) < 1:
        output.write("0")
    else:
        network(dict, int(src), n)

