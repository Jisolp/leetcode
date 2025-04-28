
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        oldToNew = {}

        def dfs (curr):
            if curr in oldToNew:
                return oldToNew[curr]
            copy = Node(curr.val)
            oldToNew[curr] = copy
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node)
        # if not node:
        #     return None 
        
        # oldToNew = {}

        # q = deque([node])
        # oldToNew[node] = Node(node.val)

        # while q:
        #     curr = q.popleft()
        #     for neighbor in curr.neighbors:
        #         if neighbor not in oldToNew:
        #             oldToNew[neighbor] = Node(neighbor.val)
        #             q.append(neighbor)
        #         oldToNew[curr].neighbors.append(oldToNew[neighbor])
        # return oldToNew[node]