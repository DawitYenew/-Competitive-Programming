class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        hash_mapP, hash_mapS = {}, {}
        for i in range(len(p)):
            hash_mapP[p[i]] = 1 + hash_mapP.get(p[i], 0)
            hash_mapS[s[i]] = 1 + hash_mapS.get(s[i], 0)
        
        if hash_mapP == hash_mapS:
            res = [0]
        else:
            res = []
        
        st = 0
        for j in range(len(p), len(s)):
            hash_mapS[s[j]] = 1 + hash_mapS.get(s[j], 0)
            hash_mapS[s[st]] -= 1

            if hash_mapS[s[st]] == 0:
                hash_mapS.pop(s[st])
            st += 1
            if hash_mapP == hash_mapS:
                res.append(st)
        return res

