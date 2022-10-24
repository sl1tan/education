class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        weight = dict()
        id = 0
        for row in mat:
            count = 0
            for man in row:
                if man == 1:
                    count += 1
            weight[id] = count
            id += 1
        result = []
        for x in range(k):
            index = min(weight, key = weight.get)
            result.append(index)
            weight.pop(index)
        return result