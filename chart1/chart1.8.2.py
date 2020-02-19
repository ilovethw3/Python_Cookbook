prices={'ACME':45.23,'AAPL':612.78,'IBM':205.55,'HPQ':37.20,'FB':10.75}

a=min(zip(prices.values(),prices.keys()))
print(a)