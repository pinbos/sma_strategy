from sma_strategy import macdStrat
from sma_strategy import strat


# Append stocks here. These are just the securities that comprise the DOW index
stocks = ["MMM", "AXP", "AAPL", "BA", "CAT", "CVX", "CSCO", "KO", "DOW", "XOM", "GS", "HD", "IBM", "INTC", "JNJ", "JPM", "MCD", "MRK", "MSFT", "NKE", "PFE", "PG", "TRV", "UNH", "UTX", "VZ", "V", "WMT", "WBA", "DIS"]


for i in stocks:
    x = strat(i)
    y = macdStrat(i)
    time.sleep(25)
    print(x)
    time.sleep(15)
    print(y)
    print('-------------------------')
