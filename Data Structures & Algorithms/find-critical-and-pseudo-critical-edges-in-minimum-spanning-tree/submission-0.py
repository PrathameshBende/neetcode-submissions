
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[self.parent[i]]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.count -= 1
            return True
        return False

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        new_edges = [(w, u, v, i) for i, (u, v, w) in enumerate(edges)]
        new_edges.sort()

        def get_mst_weight(block_idx=-1, force_idx=-1):
            uf = UnionFind(n)
            weight = 0
            if force_idx != -1:
                u, v, w = edges[force_idx]
                uf.union(u, v)
                weight += w
            for w, u, v, i in new_edges:
                if i == block_idx:
                    continue
                if uf.union(u, v):
                    weight += w
            if uf.count > 1:
                return float('inf')
            return weight

        base_weight = get_mst_weight()
        critical = []
        pseudo_critical = []

        for i in range(len(edges)):
            if get_mst_weight(block_idx=i) > base_weight:
                critical.append(i)
            elif get_mst_weight(force_idx=i) == base_weight:
                pseudo_critical.append(i)

        return [critical, pseudo_critical]