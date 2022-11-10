class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if k > len(s):
            return []
        vowel = {'a', 'e', 'i', 'o', 'u'}
        v_counter = 0

        for i in range(k):
            if s[i] in vowel: 
                v_counter += 1
        left = 0
        right = k - 1
        max_vowel_cnt = v_counter
        while right < len(s)-1:
            if s[left] in vowel:
                v_counter -= 1
            left += 1
            right += 1
            if s[right] in vowel:
                v_counter += 1
            max_vowel_cnt = max(max_vowel_cnt, v_counter)
        return max_vowel_cnt





        
