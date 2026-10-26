class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = {}
        def dfs(m, i, alice_turn, diff):
            if i >= n:
                return diff
            
            if (m, i, alice_turn) in dp:
                return diff + dp[(m, i, alice_turn)]
            if alice_turn:
                alice = -float('inf')
                for x in range(1, 2*m + 1):
                    if i + x > n: break
                    alice = max(alice, dfs(max(x, m), i + x, False, diff + sum(piles[i : i + x])))
                res = alice

            else:
                bob = float('inf')
                for x in range(1, 2*m + 1):
                    if i + x > n: break
                    bob = min(bob, dfs(max(x, m), i + x, True, diff - sum(piles[i : i + x])))
                res = bob

            dp[(m, i, alice_turn)] = res - diff
            return res

        return (sum(piles) + dfs(1, 0, True, 0))//2