import requests
import pandas as pd
from datetime import datetime, timedelta

def getCryptocurrencyBinanceAPI(symbol, interval, limit, endTime):
    url = "https://api.binance.com/api/v3/klines"
    params = {'symbol': symbol, 'interval': interval, 'limit': limit, 'endTime': endTime}
    response = requests.get(url, params=params) # Burada istek atıyoruz
    data = response.json() # Dönen istekleri json olarak alıyoruz
    processedData = [] # json olarak gelen verileri düzenliyoruz
    for item in data:
        date = datetime.fromtimestamp(item[0]/1000)
        processedData.append([date.date(), date.time(), float(item[1]), float(item[2]), float(item[3]), float(item[4]), float(item[5]), symbol])
    return processedData

coins = ['BTCUSDT', 'ETHUSDT', 'SHIBUSDT', 'DOGEUSDT']
interval = '1h' # s-> seconds; m -> minutes; h -> hours; d -> days; w -> weeks; M -> months 
limit = 5
endTime = int((datetime.utcnow() - timedelta(days=3)).timestamp() * 1000)

coinDf = pd.DataFrame(columns=['Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Symbol'])

for coin in coins:
    data = getCryptocurrencyBinanceAPI(coin, interval, limit, endTime)
    coinDf = pd.concat([coinDf, pd.DataFrame(data, columns=['Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Symbol'])], ignore_index=True)

coinDf.to_csv('CryptocurrencyDataBinance.csv', index=False)
