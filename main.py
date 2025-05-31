import yfinance as yf
import pandas as pd
import streamlit as st
from datetime import datetime
import plotly.subplots as sp
import plotly.graph_objs as go
import prophet as pf
from prophet.plot import plot_plotly as prophPlot
from prophet.plot import plot_components_plotly


def main():
    st.title("Stock Market Analyzer")
    st.subheader("Welcome to your all in one stock market analysis platform")

    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 1, 1))
    with col2:
        end_date = st.date_input("End Date", datetime.today())
        
    if start_date >= end_date:
        st.error("End date must be after start date")
        return

    stock_name = symbols()
    if stock_name:
        dat = getting_data(stock_name, start_date, end_date)
        if dat is not None:
            plot_candle(dat, stock_name)
            
            if st.checkbox("Show Price Forecast"):
                forecast(dat)

def symbols():
    option = st.radio("Select stock by:", ["Choose from list", "Enter custom symbol"])
    
    if option == "Choose from list":
        return st.selectbox("Pick any stock:", ["AAPL", "MSFT", "NVDA", "GOOG", "AMZN", "META", "TSLA"])
    else:
        custom_symbol = st.text_input("Enter stock symbol (e.g., AAPL):").upper()
        if custom_symbol:
            return custom_symbol
        else:
            st.warning("Please enter a valid stock symbol")
            return None

@st.cache_data
def getting_data(stock, start_date, end_date):
    try:
        dat = yf.download(stock, start=start_date, end=end_date)
        if dat.empty:
            st.error(f"No data found for ticker symbol: {stock}")
            return None
        dat.reset_index(inplace=True)
        return dat
    except Exception as e:
        st.error(f"Error fetching data for {stock}: {e}")
        return None

def plot_candle(df, stock):
    try:
        if df is None or df.empty:
            st.warning("No data available to plot")
            return

        fig = sp.make_subplots(rows=2, cols=1,
                            shared_xaxes=True,
                            vertical_spacing=0.05,
                            row_heights=[0.7, 0.3],
                            subplot_titles=('Candlestick Chart', 'Moving Averages'))
        
        df['MA5'] = df['Close'].rolling(window=5).mean()
        df['MA20'] = df['Close'].rolling(window=20).mean()
        
        fig.add_trace(go.Candlestick(
            x=df['Date'],
            open=df['Open', stock],  
            high=df['High', stock],  
            low=df['Low', stock],    
            close=df['Close', stock], 
            name='Market Data'
        ), row=1, col=1)
        
        fig.add_trace(go.Scatter(
            x=df['Date'],
            y=df['MA5'],
            opacity=0.7,
            line=dict(color='blue', width=2),
            name='MA 5'
        ), row=2, col=1)

        fig.add_trace(go.Scatter(
            x=df['Date'],
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


    except Exception as e:
        st.error(f"Error creating chart: {e}")


def forecast(df):
    try:
        if 'Date' not in df.columns or 'Close' not in df.columns:
            st.error("Required columns not found in data")
            return

        dates = df['Date'].values.ravel()
        values = df['Close'].values.ravel()
        
        df_fore = pd.DataFrame({
            'ds': dates,
            'y': values
        })

        df_fore['ds'] = pd.to_datetime(df_fore['ds'])
        df_fore['y'] = pd.to_numeric(df_fore['y'])
        
        m = pf.Prophet(
            yearly_seasonality=True,
            weekly_seasonality=True,
            daily_seasonality=False
        )
        m.fit(df_fore)
        
        future = m.make_future_dataframe(periods=365)
        forecast = m.predict(future)
        
        st.subheader("Price Forecast")
        fig1 = prophPlot(m, forecast)
        st.plotly_chart(fig1)
        
        st.subheader("Forecast Components") 
        fig2 = plot_components_plotly(m, forecast)
        st.plotly_chart(fig2)
        
    except Exception as e:
        st.error("Error generating forecast. Please try again.")


if __name__ == "__main__":
    main()

