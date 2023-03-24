# 1466. Reorder Routes to Make All Paths Lead to the City Zero
from typing import List


class Solution:
    def dfs(self, node, adj, vis):
        vis[node] = 1
        count = 0
        for nod in adj[node]:
            if vis[abs(nod)] == 0:
                if nod > 0:
                    count += 1
                count += self.dfs(abs(nod), adj, vis)
        return count

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        vis = [0] * n

        for u, v in connections:
            adj[u].append(v)
            adj[v].append(-u)

        return self.dfs(0, adj, vis)
