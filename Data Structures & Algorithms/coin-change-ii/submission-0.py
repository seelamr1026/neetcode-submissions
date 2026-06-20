class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dpArr = [0]*(amount+1)
        dpArr[0] = 1

        for coin in coins:
            for a in range(coin,amount+1):
                dpArr[a] += dpArr[a-coin]

        return dpArr[amount] 
        