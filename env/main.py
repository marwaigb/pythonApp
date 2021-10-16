from flask import Flask
import requests


app = Flask(__name__)


@app.route('/')
def BitcoinPrice():
    answer = ""
    responseGetCURR = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = responseGetCURR.json()
    CurrentPrice = data["bpi"]["USD"]["rate"]
    responseGetAvg = requests.get('https://min-api.cryptocompare.com/data/v2/histominute?fsym=BTC&tsym=USD&limit=10')
    last10min = responseGetAvg.json()
    answer += "the current Bitcoin price now is "
    answer +=str(CurrentPrice)
    sum = 0
    for i in range(10):
        sum = sum + (last10min['Data']["Data"][i]['close'])
    # average in last 10 minutes
    AvgPrice = sum / 10
    
    answer += " the Average Price for the last 10 minutes is " + str(AvgPrice)

    return answer


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
    