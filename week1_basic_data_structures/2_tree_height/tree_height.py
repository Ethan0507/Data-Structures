# python3

import sys
import threading
def fill_height(parents, visited, height, node):
    if parents[node] == -1:
        visited[node] = 1
        return 1
    if visited[node]:
        return height[node]

    visited[node] = 1
    height[node] = 1 + fill_height(parents, visited, height, parents[node])
    return height[node]

def compute_height(n, parents):
    max_height = 0
    visited = [0] * n
    height = [0] * n
    for i in range(n):
        if not visited[i]:
            height[i] = fill_height(parents, visited, height, i)
        max_height = max(max_height, height[i])
    return max_height

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
