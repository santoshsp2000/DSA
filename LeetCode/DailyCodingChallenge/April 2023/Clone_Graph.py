# 133. Clone Graph
# Leetcode Medium
# Date: 8 April 2023
# TC: O(N)
# SC: O(N)


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def dfs(self, node, vis):
        new_node = Node(node.val)
        vis[node.val] = new_node
        for nod in node.neighbors:
            if nod.val in vis:
                new_node.neighbors.append(vis[nod.val])
            else:
                new_node.neighbors.append(self.dfs(nod, vis))
        return new_node

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return
        vis = {}

        return self.dfs(node, vis)
