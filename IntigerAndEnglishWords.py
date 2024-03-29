class Solution:
    def numberToWords(self,num: int) -> str:
        one_to_19 = "One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
        tens = "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()
        
        if num == 0:
            return "Zero"
        def recursion(num):
            if num == 0:
                return ""
            if num <= 19:
                return one_to_19[num-1]
            if num <= 99:
                return (tens[(num//10)-2] + " " + recursion(num%10)).rstrip()
            if num <= 999:
                return (one_to_19[(num//100)-1] + " Hundred " + recursion(num%100)).rstrip()
            if num <= 10**6 - 1:
                return (recursion(num//1000) + " Thousand " + recursion(num%1000)).rstrip()
            if num <= 10**9 - 1:
                return (recursion(num//10**6) + " Million " + recursion(num%10**6)).rstrip()
            else:
                return (recursion(num//10**9) + " Billion " + recursion(num%10**9)).rstrip()
        return recursion(num)
number = 123
print(Solution().numberToWords(number))