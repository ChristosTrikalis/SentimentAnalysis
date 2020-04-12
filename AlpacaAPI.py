import alpaca_trade_api as tradeapi

#First API ID is specified, then secret key, then api url.
api = tradeapi.REST('PKV2AJARAR0S4IPCR949','A73prhm4caHWRHf5otB2p5bxoeiGcpYA1dp28NGy','https://paper-api.alpaca.markets')

#Gets 15min interval prices for SPY ticker from start to end
barset = api.get_barset('SPY', '15Min', start='2020-02-11T09:30:00-04:00',end='2020-02-12T09:30:00-04:00')
spy_bars = barset['SPY']

print(spy_bars)
