class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(words)
        order_map = {}
        for i in range(len(order)):
            order_map[order[i]] = i
        
        for i in range(0, n - 1):
            j = 0
            k = 0
            left = words[i]
            right = words[i + 1]
            while j <= len(left) and k <= len(right):
                if k == len(right):
                    return False
                elif j == len(left):
                    break
                elif left[j] == right[k]:
                    j += 1
                    k += 1
                else:
                    if order_map[left[j]] > order_map[right[k]]:
                        return False
                    else:
                        break
                
        return True