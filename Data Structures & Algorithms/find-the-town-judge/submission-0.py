class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_by = [0] * (n + 1)
        trustee = [0] * (n + 1)
        for i in range(len(trust)):
            tmp1, tmp2 = trust[i]
            trusted_by[tmp2] += 1
            trustee[tmp1] += 1

        for j in range(n + 1):
            if trusted_by[j] == n - 1:
                if trustee[j] == 0:
                    return j

        return -1