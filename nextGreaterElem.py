class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        grtr_elems = []
        for n1 in nums1:
            rightElems = nums2.index(n1)
            val = -1 
            for n2 in nums2[rightElems+1:]:
                if n2 > n1:
                    val = n2
                    break
            grtr_elems.append(val)
            print(grtr_elems)
        return grtr_elems