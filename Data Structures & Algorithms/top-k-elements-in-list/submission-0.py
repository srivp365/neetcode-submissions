class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}  # first loop through to create a frequency table

        # keeps track of the number of times a given element shows up
        anskey = [[] for i in range(len(nums) + 1)]

        # tracks count + num
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            anskey[c].append(n)

        res = []
        for j in range(len(nums), 0, -1):
            for l in range(len(anskey[j])):
                if len(res) < k:
                    res.append(anskey[j][l])
                if len(res) >= k:
                    return res
