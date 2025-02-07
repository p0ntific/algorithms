import sys

class Vertex:
    def __init__(self, vertexes):
        self.flag = -1
        self.vertexes = vertexes

    def add_vertex(self, vertex):
        self.vertexes.append(vertex)

    def change_flag(self, flag):
        self.flag = flag

    def __str__(self):
        return "flag: " + str(self.flag) + " vertexes: " + str(self.vertexes)

def file_read(file_name):
    with open(file_name) as file:
        graph = {}
        n, line = map(int, file.readline().split())
        for i in range(0, line):
            line = file.readline().replace("\n", "").split(" ")
            key = int(line[1])
            value = int(line[0])
            if key in graph:
                vertex = graph.get(key)
                vertex.add_vertex(value)
                graph[key] = vertex
            else:
                vertex = Vertex([value])
                graph[key] = vertex
            if value not in graph:
                vertex = Vertex([])
                graph[value] = vertex
        return graph


def dfs(graph, vertex, way):
    if graph.get(vertex).flag == 1:
        write_ans(way)
        sys.exit()
    graph.get(vertex).change_flag(1)
    for n in graph[vertex].vertexes:
        if graph[n].flag != -1:
            way.append([vertex, n])
            if dfs(graph, n, way):
                sys.exit()
    graph.get(vertex).change_flag(0)
    return False


def write_ans(way):
    cycle = []
    way.reverse()
    vertex = way[0][0]
    start_element = way[0][1]
    cycle.append(start_element)
    cycle.append(vertex)
    for i in way:
        if vertex != start_element:
            if vertex == i[1]:
                cycle.append(i[0])
                vertex = i[0]
    with open("cycle2.out", "w") as f:
        f.write("YES\n")
        f.write(" ".join([str(x) for x in cycle[1:]]))


def main():
    graph = file_read("cycle2.in")
    result = False
    for i in graph:
        if graph.get(i).flag == -1 and graph.get(i).vertexes:
            result = dfs(graph, i, [])
    if not result:
        with open("cycle2.out", "w") as f:
            f.write("NO")


main()