class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        boolarray=[]
        for i in range(0,len(l)):
            newnums=nums[l[i]:r[i]]
            newnums.append(nums[r[i]])
            newnums.sort()
            result = [b - a for a,b in zip(newnums[:-1], newnums[1:])]
            s3=set(result)
            if len(s3)==1:
                boolarray.append(True)
            else:
                boolarray.append(False)
        return boolarray
