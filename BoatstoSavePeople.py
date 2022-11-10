class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        start, end = 0, len(people)-1
        boat_num = 0
        while start <= end:
            if people[end] + people[start] <= limit:
                start += 1
            end -= 1
            boat_num += 1
        return boat_num
