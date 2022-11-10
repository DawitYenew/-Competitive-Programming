class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dic = Counter(arr)
        sort_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        sum_ = 0
        counter = 0
        print(len(arr))
        for i in sort_dic:
            print(i[0], i[1])
            if sum_ < len(arr)/2:
                sum_ += i[1]
                counter += 1
                if sum_ > len(arr)/2:
                    break
        return counter
