class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}

        for _ in s:
            dict1[_] = dict1.get(_,0) + 1

        for _ in t:
            dict2[_] = dict2.get(_,0) + 1

        if dict1 == dict2:
            return True
        return False