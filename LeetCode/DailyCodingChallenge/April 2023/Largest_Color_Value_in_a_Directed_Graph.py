# 1857. Largest Color Value in a Directed Graph
# Leetcode Hard
# Date: 9 April 2023
# TC: O(V+E)
# SC: O(N*26)


class Solution(object):
    def largestPathValue(self, colors, edges):
        n = len(colors)
        al = [[] for _ in range(n)]
        cnt = [[0] * 26 for _ in range(n)]
        indeg = [0] * n

        for e in edges:
            al[e[0]].append(e[1])
            indeg[e[1]] += 1

        que = []
        for i in range(n):
            if indeg[i] == 0:
                que.append(i)

        res, processed = 0, 0
        while que:
            que1 = []
            for i in que:
                processed += 1
                res = max(res, cnt[i][ord(colors[i]) - ord('a')] + 1)
                cnt[i][ord(colors[i]) - ord('a')] += 1
                for j in al[i]:
                    for k in range(26):
                        cnt[j][k] = max(cnt[j][k], cnt[i][k])
                    indeg[j] -= 1
                    if indeg[j] == 0:
                        que1.append(j)
            que = que1

        return res if processed == n else -1