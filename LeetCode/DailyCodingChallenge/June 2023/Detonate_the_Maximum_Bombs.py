# 2101. Detonate the Maximum Bombs
# Leetcode Medium
# Date: 2 June 2023
# TC: O(N^2)
# SC: O(N + E + V)
from typing import List


class Solution:

    def visit(self, node, adj, vis):
        vis[node] = 1
        ans = 1
        for nod in adj[node]:
            if vis[nod] == 0:
                ans += self.visit(nod, adj, vis)
        return ans

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        adj = {i: [] for i in range(n)}

        for i in range(n):
            x1, y1, r1 = bombs[i][0], bombs[i][1], bombs[i][2]
            for j in range(i, n):
                x2, y2, r2 = bombs[j][0], bombs[j][1], bombs[j][2]
                d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                if d <= r1:
                    adj[i].append(j)
                if d <= r2:
                    adj[j].append(i)

        ans = 0

        for i in range(n):
            vis = [0] * n
            if vis[i] == 0:
                ans = max(ans, self.visit(i, adj, vis))
        return ans
