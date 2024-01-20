def buy_and_sell_stock_once(prices):
    minPrice = prices[0]
    maxProfit = 0

    for i in range(len(prices)):
        print(i)
        if prices[i] - minPrice > maxProfit:
            maxProfit = prices[i] - minPrice
            print("\033[1;20;40m minimum price = ", minPrice)
            print("\033[1;32;40m maximum profit = ", maxProfit)
        minPrice = min(minPrice, prices[i] )
    return maxProfit

prices_array = [310,315,275,295,260,270,290,230,255,250]

print("\033[1;35;50m max profit = ",buy_and_sell_stock_once(prices_array))