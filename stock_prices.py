"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


SOLUTION:
1. Initialize `min_price` to the first price in the array and `max_profit` to 0.
2. Iterate over the array and for each day:
    * If the current price is less than `min_price`, update `min_price` and reset `max_profit` to 0.
    * Otherwise, calculate the potential profit by subtracting `min_price` from the current price and update `max_profit` if the new profit is higher.
"""
def max_profit(prices):
    min_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    return max_profit
