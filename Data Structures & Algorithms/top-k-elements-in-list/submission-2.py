class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lislen = len(nums)
        #if lislen < k:
        #    return []
        #elif lislen == k:
        #    return nums

        freq = {}
        ans = [[] for l in range(lislen + 1)]
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)

        for n, c in freq.items():
            ans[c].append(n)

        res = []

        for i in range(lislen, 0, -1):
            for j in ans[i]:
                res.append(j)
                if len(res) == k:
                    return res

