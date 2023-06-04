# 547. Number of Provinces
# Leetcode Medium
# Date: 4 June 2023
# TC: O(N^2 + E + V)
# SC: O(E + V)
from typing import List


# BFS Approach
class BFSSolution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        adj = {i: [] for i in range(n)}

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    adj[i].append(j)
                    adj[j].append(i)

        vis = [0] * n
        count = 0
        que = deque()

        for i in range(n):
            if vis[i] == 0:
                que.append(i)
                count += 1
            while que:
                node = que.popleft()

                for nod in adj[node]:
                    if vis[nod] == 0:
                        que.append(nod)
                        vis[nod] = 1

        return count


# DFS Approach
class DFSSolution:
    def visit(self, node, adj, vis):
        vis[node] = 1

        for nod in adj[node]:
            if vis[nod] == 0:
                self.visit(nod, adj, vis)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj = {i: [] for i in range(n)}

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    adj[i].append(j)
                    adj[j].append(i)

        vis = [0] * n
        count = 0

        for i in range(n):
            if vis[i] == 0:
                self.visit(i, adj, vis)
                count += 1

        return count
