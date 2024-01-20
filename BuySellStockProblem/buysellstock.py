def buy_and_sell_stock_once(prices):
    maxProfit = 0
    buyingPrice = 0
    sellingPrice = 0

    for i in range(len(prices)):
        print("\033[1;31;40m comparing with Bp of \n", prices[i])
        for j in range(i+1,len(prices)):
            print("\033[1;33;40m Comparing with SP of \n", prices[j])
            jprofit = prices[j]-prices[i]
            if jprofit > maxProfit:
                maxProfit = jprofit
                buyingPrice = prices[i]
                sellingPrice = prices[j]
    return maxProfit, buyingPrice, sellingPrice

prices_array = [310,315,275,295,260,270,290,230,255,250]

print("\033[1;37;40m",buy_and_sell_stock_once(prices_array))