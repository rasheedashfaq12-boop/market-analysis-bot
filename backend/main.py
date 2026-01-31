from fastapi import FastAPI
import yfinance as yf
import pandas as pd
import numpy as np
import ta

app = FastAPI()

def analyze_market(symbol: str, interval: str):
    df = yf.download(tickers=symbol, period="1d", interval=interval)

    df['rsi'] = ta.momentum.RSIIndicator(df['Close']).rsi()
    df['ema'] = ta.trend.EMAIndicator(df['Close'], window=20).ema_indicator()
    df['macd'] = ta.trend.MACD(df['Close']).macd()

    latest = df.iloc[-1]

    score = 0

    if latest['rsi'] < 30:
        score += 1
    if latest['Close'] > latest['ema']:
        score += 1
    if latest['macd'] > 0:
        score += 1

    confidence = (score / 3) * 100

    if score >= 2:
        signal = "UP"
    else:
        signal = "DOWN"

    return signal, round(confidence, 2)

@app.get("/signal")
def get_signal(symbol: str = "EURUSD=X", interval: str = "1m"):
    signal, confidence = analyze_market(symbol, interval)
    return {
        "signal": signal,
        "confidence": confidence
    }
