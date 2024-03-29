class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counter = Counter(changed)
        print(counter)
        original = []
        for key in counter.keys():       
            if key == 0:
                if counter[key] % 2 > 0:
                    return []
                original += [0] * (counter[key] // 2)
                
            elif counter[key] > 0:
                x = key
                while x % 2 == 0 and x // 2 in counter:
                    x = x // 2

                while x in counter:
                    if counter[x] > 0:
                        original += [x] * counter[x]
                        if counter[x+x] < counter[x]:
                            return []
                        counter[x+x] -= counter[x]
                        counter[x] = 0
                    x += x
        return original


