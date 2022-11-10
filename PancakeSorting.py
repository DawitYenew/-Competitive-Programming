class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        def flip(end):
            st = 0
            while st < end:
                arr[st], arr[end] = arr[end], arr[st]
                st += 1
                end -= 1
        for i in range(len(arr)-1,-1,-1):
                max_i = i
                for j in range(i,-1,-1):
                    if arr[j] > arr[max_i]: max_i = j
                if max_i != i:
                    flip(max_i)
                    flip(i)
                    result.append(max_i+1)
                    result.append(i+1)
        return result

        
            
