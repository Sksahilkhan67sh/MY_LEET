from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        answer = 0

        def dfs(node):

            visited[node] = True

            component.append(node)

            for nxt in graph[node]:
                if not visited[nxt]:
                    dfs(nxt)

        for i in range(n):

            if visited[i]:
                continue

            component = []

            dfs(i)

            vertices = len(component)

            edgeCount = 0

            for node in component:
                edgeCount += len(graph[node])

            edgeCount //= 2

            if edgeCount == vertices * (vertices - 1) // 2:
                answer += 1

        return answer