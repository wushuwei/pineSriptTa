from tradingview_ta import TA_Handler, Interval, Exchange
list1 = {'QQQ',  'NIU', 'AAPL', 'AMZN', 'COIN', 'TSLA', 'ROKU'}
intervals = {Interval.INTERVAL_15_MINUTES, Interval.INTERVAL_1_HOUR}
for interval in intervals:
    print(interval + '--------')
    for stock in list1:
        sym = TA_Handler(
            symbol=stock,
            screener="america",
            exchange="NASDAQ",
            interval=interval
        )
        print(sym.symbol + ': ' + sym.get_analysis().summary.get('RECOMMENDATION'))
    # print(sym.get_analysis().summary.get('RECOMMENDATION'))
# Example output: {"RECOMMENDATION": "BUY", "BUY": 8, "NEUTRAL": 6, "SELL": 3}