import yfinance as yf
import pandas as pd
import streamlit as st
from datetime import datetime
import plotly.subplots as sp
import plotly.graph_objs as go
import prophet as pf
from prophet.plot import plot_plotly as prophPlot


def main():
    st.title("Stock Market Analyzer")

    st.subheader("Welcome to your all in one stock market analysis platform")

    stock_name = symbols()

    dat = getting_data(stock_name)

    plot_candle(dat, stock_name)

    st.write("forecast data")

    forecast(dat)

def symbols():
    return st.selectbox("Pick any stock: ", ["AAPL", "MSFT", "NVDA", "GOOG"])

@st.cache_data
def getting_data(stock):
    dat = yf.download(stock, start="2022-01-01", end=datetime.today())
    dat.reset_index(inplace=True)
    return dat

def plot_candle(df, stock):
    fig = go.Figure()

    df['MA5'] = df['Close'].rolling(window=5).mean()
    df['MA20'] = df['Close'].rolling(window=20).mean()

    fig=go.Figure()

    fig = sp.make_subplots(rows=2, cols=1,
                        shared_xaxes=True,
                        vertical_spacing=0.05,
                        row_heights=[0.7, 0.3],
                        subplot_titles=('Candlestick Chart', 'Moving Averages'))

    fig.add_trace(go.Candlestick(
        x=df.index,
        open=df['Open', stock],
        high=df['High', stock],
        low=df['Low', stock],
        close=df['Close', stock],
        name='Market Data'
    ), row=1, col=1)

    fig.add_trace(go.Scatter(
        x=df.index,
        y=df['MA5'],
        opacity=0.7,
        line=dict(color='blue', width=2),
        name='MA 5'
    ), row=2, col=1)

    fig.add_trace(go.Scatter(
        x=df.index,
        y=df['MA20'],
        opacity=0.7,
        line=dict(color='orange', width=2),
        name='MA 20'
    ), row=2, col=1)

    fig.update_layout(
        height=800,
        showlegend=True,
        xaxis_rangeslider_visible=False,
        title_text=f"{stock} - Candlestick with Moving Averages"
    )
    st.plotly_chart(fig)


def forecast(df):
    df = df[["Date", "lose"]]
    df = df.rename(columns={"Date": "ds", "Close": "y"})

    m = pf.Prophet()
    m.fit(df)
    future = m.make_future_dataframe(periods="2y")
    forecast = m.predict(future)

    st.subheader("forecast data")
    
    fig1 = prophPlot(m, forecast)
    st.plotly_chart(fig1)

    fig2 = m.plot_components(forecast)
    st.write(fig2)


if __name__ == "__main__":
    main()

