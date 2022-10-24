class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for client in accounts:
            summ = sum(client)
            if summ > max:
                max = summ
        return max