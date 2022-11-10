class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_basket = {}
        start = 0
        max_so_far = 0
        for r in range(len(fruits)):
            if fruits[r] not in fruit_basket:
                fruit_basket[fruits[r]] = 1
            else:
                fruit_basket[fruits[r]] += 1
            
            # print("out")
            # print(fruit_basket)
            while len(fruit_basket) > 2:
                fruit_basket[fruits[start]] -= 1
                if fruit_basket[fruits[start]] == 0:
                    del fruit_basket[fruits[start]]
                start += 1
                # print("in wile loop")
                # print(fruit_basket)
            max_so_far = max(max_so_far, r - start +1)
        return max_so_far



