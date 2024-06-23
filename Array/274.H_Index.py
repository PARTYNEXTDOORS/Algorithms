class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort()
        a = len(citations)
        
        for i in range(len(citations)):
            if citations[i] >= a - i:
                return a - i
        return 0
