from flask import Flask, render_template, jsonify
import urllib3
import json
import datetime
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chart1')
def data():
    url = "https://min-api.cryptocompare.com/data/histohour?fsym=BTC&tsym=USD&e=bitfinex&limit=23"
    http = urllib3.PoolManager()
    r = http.request('GET',url)
    data = json.loads(r.data)
    data = data["Data"]
    date_col = []
    close_col = []
    for item in data:
        ts = item["time"]
        close = item["close"]
        date_col.append(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S').split(" ")[1])
        close_col.append(close)
    return jsonify( {"date" : date_col, "close" : close_col })

@app.route('/chart2')
def data2():
    url = "https://min-api.cryptocompare.com/data/histohour?fsym=ETH&tsym=USD&e=bitfinex&limit=23"
    http = urllib3.PoolManager()
    r = http.request('GET',url)
    data = json.loads(r.data)
    data = data["Data"]
    date_col = []
    close_col = []
    for item in data:
        ts = item["time"]
        close = item["close"]
        date_col.append(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S').split(" ")[1])
        close_col.append(close)
    return jsonify( {"date" : date_col, "close" : close_col })

@app.route('/chart3')
def data3():
    url = "https://min-api.cryptocompare.com/data/histohour?fsym=XRP&tsym=USD&e=bitfinex&limit=23"
    http = urllib3.PoolManager()
    r = http.request('GET',url)
    data = json.loads(r.data)
    data = data["Data"]
    date_col = []
    close_col = []
    for item in data:
        ts = item["time"]
        close = item["close"]
        date_col.append(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S').split(" ")[1])
        close_col.append(close)
    return jsonify( {"date" : date_col, "close" : close_col })


@app.route('/tableBTC')
def chart1():
    url = "https://min-api.cryptocompare.com/data/histohour?fsym=BTC&tsym=USD&e=bitfinex&limit=23"
    http = urllib3.PoolManager()
    r = http.request('GET',url)
    data = json.loads(r.data)
    data = data["Data"]
    date_col = []
    close_col = []
    open_col = []
    volume_from_col = []
    volume_to_col = []
    high_col = []
    low_col = []
    dic = {}
    for item in data:
        ts = item["time"]
        close = item["close"]
        open = item["open"]
        volume_from = item["volumefrom"]
        volume_to = item["volumeto"]
        high = item["high"]
        low = item["low"]
        date_col.append(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
        close_col.append(close)
        open_col.append(open)
        volume_from_col.append(volume_from)
        volume_to_col.append(volume_to)
        high_col.append(high)
        low_col.append(low)
    dic["Date"] = date_col
    dic["Close"] = close_col
    dic["Open"] = open_col
    dic["VolumeFrom"] = volume_from_col
    dic["VolumeTo"] = volume_to_col
    dic["High"] = high_col
    dic["low"] = low_col
    df = pd.DataFrame(data=dic)
    out = df.to_dict('records')
    return jsonify( {"data" : out })

@app.route('/tableETH')
def chart2():
    url = "https://min-api.cryptocompare.com/data/histohour?fsym=ETH&tsym=USD&e=bitfinex&limit=23"
    http = urllib3.PoolManager()
    r = http.request('GET',url)
    data = json.loads(r.data)
    data = data["Data"]
    date_col = []
    close_col = []
    open_col = []
    volume_from_col = []
    volume_to_col = []
    high_col = []
    low_col = []
    dic = {}
    for item in data:
        ts = item["time"]
        close = item["close"]
        open = item["open"]
        volume_from = item["volumefrom"]
        volume_to = item["volumeto"]
        high = item["high"]
        low = item["low"]
        date_col.append(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
        close_col.append(close)
        open_col.append(open)
        volume_from_col.append(volume_from)
        volume_to_col.append(volume_to)
        high_col.append(high)
        low_col.append(low)
    dic["Date"] = date_col
    dic["Close"] = close_col
    dic["Open"] = open_col
    dic["VolumeFrom"] = volume_from_col
    dic["VolumeTo"] = volume_to_col
    dic["High"] = high_col
    dic["low"] = low_col
    df = pd.DataFrame(data=dic)
    out = df.to_dict('records')
    return jsonify( {"data" : out })

@app.route('/tableXRP')
def chart3():
    url = "https://min-api.cryptocompare.com/data/histohour?fsym=XRP&tsym=USD&e=bitfinex&limit=23"
    http = urllib3.PoolManager()
    r = http.request('GET',url)
    data = json.loads(r.data)
    data = data["Data"]
    date_col = []
    close_col = []
    open_col = []
    volume_from_col = []
    volume_to_col = []
    high_col = []
    low_col = []
    dic = {}
    for item in data:
        ts = item["time"]
        close = item["close"]
        open = item["open"]
        volume_from = item["volumefrom"]
        volume_to = item["volumeto"]
        high = item["high"]
        low = item["low"]
        date_col.append(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
        close_col.append(close)
        open_col.append(open)
        volume_from_col.append(volume_from)
        volume_to_col.append(volume_to)
        high_col.append(high)
        low_col.append(low)
    dic["Date"] = date_col
    dic["Close"] = close_col
    dic["Open"] = open_col
    dic["VolumeFrom"] = volume_from_col
    dic["VolumeTo"] = volume_to_col
    dic["High"] = high_col
    dic["low"] = low_col
    df = pd.DataFrame(data=dic)
    out = df.to_dict('records')
    return jsonify( {"data" : out })
    


if __name__ == "__main__":
    app.run()






















