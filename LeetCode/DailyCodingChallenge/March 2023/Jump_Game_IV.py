# 1345. Jump Game IV
from collections import deque
from typing import List


class Solution:

    def minJumps(self, arr: List[int]) -> int:
        d = {}
        n = len(arr)
        que = deque()
        steps = 0

        for i in range(n):
            if arr[i] in d:
                d[arr[i]].append(i)
            else:
                d[arr[i]] = deque([i])
        vis = [0] * n
        que.append(0)
        vis[0] = 1
        dist = [-1] * n
        dist[0] = 0

        while que:
            m = len(que)
            i = que.popleft()
            if n - 1 == i:
                break

            if i - 1 >= 0 and dist[i - 1] == -1:
                dist[i - 1] = dist[i] + 1
                que.append(i - 1)

            if i + 1 < n and dist[i + 1] == -1:
                dist[i + 1] = dist[i] + 1
                que.append(i + 1)

            while d[arr[i]]:
                j = d[arr[i]].popleft()
                if dist[j] == -1:
                    dist[j] = dist[i] + 1
                    que.append(j)

        return dist[n - 1]

