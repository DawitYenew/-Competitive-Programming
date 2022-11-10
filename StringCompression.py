class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0
        left = 0
        while left < len(chars):
            right = left
            while right < len(chars) and chars[right] == chars[left]:
                right += 1
            chars[index] = chars[left]
            index += 1
            count = right - left
            if (count) > 1:
                for num_st in str(count):
                    chars[index] = num_st
                    index += 1
            left = right
        return index

        
