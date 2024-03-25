from heapq import heappush, heappop
from copy import deepcopy
import io
import os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

class Tourist:
    graph = []
    times = [[]]
    def __init__(self, n, m, teleports, times):
        self.n = n
        self.m = m
        self.graph = [[] for _ in range(n + 1)]
        
        for teleport in teleports:
            a, b, c = teleport
            self.graph[a].append((b, c))
            self.graph[b].append((a, c))
        for i in times:
            self.times.append(i)


    def solve(self):
        distances = [10**12] * (self.n + 1)
        distances[1] = 0
        stack = [(0, 1)]

        while stack:
            dist, current_town = heappop(stack)

            if dist != distances[current_town]:
                continue

            current_time = distances[current_town]

            for t in self.times[current_town]:
                current_time += (t == current_time)

            for data in self.graph[current_town]:
                neighbor, cost = data
                if distances[neighbor] - cost > distances[current_town]:
                    distances[neighbor] = min(distances[neighbor], current_time + cost)
                    heappush(stack, (distances[neighbor], neighbor))
        return distances[self.n]
        

def main():
    # with open('tourist.in') as f:
    #     n, m = map(int, f.readline().split())

    #     teleports = [tuple(map(int, f.readline().split())) for _ in range(m)]
    #     times = [list(map(int, f.readline().split()))[1:] for _ in range(n)]
    n, m = map(int, input().split())

    teleports = [tuple(map(int, input().split())) for _ in range(m)]
    times = [list(map(int, input().split()))[1:] for _ in range(n)]

    tourist = Tourist(n, m, teleports, times)
    ans = tourist.solve()
    print(ans if ans != 10**12 else -1)

if __name__ == "__main__":
    main()
