'''
股票计算小程序
'''

name = "黑马程序员"
stock_price = 19.98
stock_code = 25588
stock_growth = 1.2
growth_days = 7
print(f"公司: {name}, 股票代码: {stock_code}, 当前股价: {stock_price}")
print("每日增长系数: %.2f, 经过 %d 天的增长后, 股价达到了: %.2f" %(stock_growth, growth_days, stock_price * (stock_growth ** growth_days)))