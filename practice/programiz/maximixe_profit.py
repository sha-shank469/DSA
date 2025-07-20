

# def buy_and_sell(prices):
    
#     buy_price = prices[0]
#     profit = 0
    
#     for i in range(1, len(prices)):
#         if prices[i] < buy_price:
#             buy_price = prices[i]
#         else:
#             profit = max(profit, prices[i] - buy_price)
    
#     return profit

# if __name__ == "__main__":
    
#     prices = [100, 180, 260, 310, 40, 535, 695]
#     print(buy_and_sell(prices))


# I want to find the maximum profit by buying at the lowest price and selling at the highest price
# after that (single buy-sell transaction). Here is corrected code



def buy_sell(prices):
    
    min_price = float('inf')
    max_profit = 0
    buy = sell = None
    
    for price in prices:
        if price < min_price:
            min_price = price
        
        if price - min_price > max_profit:
            max_profit = price - min_price
            buy = min_price
            sell = price
    
    if max_profit == 0:
        return (0, 0)
    
    return (buy , sell)

if __name__ == "__main__":
    prices = [100, 180, 260, 310, 40, 535, 695]
    print(buy_sell(prices)) 