# Stock Market Analyzer

A full-fledged stock market analysis application developed with Python and Streamlit that enables users to visualize past stock data, study price trends through moving averages, and predict future price movement. This tool connects intricate financial data to easy visualization, enabling both beginner investors and veteran traders to easily analyze stocks.

### Video Demo:

[Link to Video Demo](https://youtu.be/HkBlB1I2stE?si=hxQY4HwG636BzkA-)

## Features

-   **Stock Selection**: Select from widely followed stocks such as AAPL, MSFT, NVDA, GOOG, AMZN, META, and TSLA, or insert any valid global market ticker symbol. The adaptable input system permits the analysis of stocks, ETFs, and other securities traded on Yahoo Finance.

-   **Interactive Date Range Selection**: Examine stock performance for any arbitrary time frame using a user-friendly date picker interface.

-   **Candlestick Visualization**: Visualize OHLC (Open-High-Low-Close) price data using interactive charts driven by Plotly. Hover over candlesticks for exact price levels, zoom in on a chosen time span, and save charts as pictures for analysis or sharing.

-   **Technical Indicators**: Automatically compute and display moving averages (5-day and 20-day) to determine trend directions and possible support/resistance levels. These indicators assist users in detecting trend reversals, continuation patterns, and price momentum.

-   **Price Predictions**: Create future price forecasts with the help of Facebook Prophet algorithm, which is used for time series forecasting with high seasonal patterns. Both point forecasts and confidence intervals are given by the model up to 365 days in the future.

-   **Data Caching**: Maximized performance through data caching for stock data retrieval with Streamlit's data caching facility to load frequently accessed stocks much faster, enhancing the overall user experience.

-   **Error Handling**: Proper error validation prevents the application from crashing due to incorrect inputs, missing data, or API connectivity problems.

## Requirements

The project needs the following Python libraries:

-   streamlit
-   yfinance
-   pandas
-   plotly
-   prophet
-   datetime

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/stockMarketAnalyzer.git
cd stockMarketAnalyzer
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

Or install individual packages:

```bash
pip install streamlit yfinance pandas plotly prophet
```

## Usage

1. Launch the Streamlit application:

```bash
streamlit run main.py
```

2. The web interface will open in your default browser with the title "Stock Market Analyzer" and a welcome message.

3. Choose a start date and end date for your analysis period from the date pickers available. The system will ensure that the end date is later than the start date.

4. Select a stock either from the list of predefined stocks (AAPL, MSFT, etc.) or switch to "Enter custom symbol" and enter any valid ticker symbol that Yahoo Finance recognizes.

5. View the candlestick chart and moving averages for your selected stock. The upper panel shows the price action while the lower panel displays the technical indicators for trend analysis.

6. Optionally, check the "Show Price Forecast" checkbox to generate and display future price predictions based on historical patterns.

7. Interact with the charts by hovering, zooming, and panning to focus on areas of interest.

## Project Structure

-   **main.py**: Main application file with all functionality

    -   `main()`: Main entry point that initiates the Streamlit interface and controls the workflow
    -   `symbols()`: Manages stock symbol selection with preconfigured ones and user input
    -   `getting_data()`: Retrieves stock data from Yahoo Finance API with caching to improve performance

-   `plot_candle()`: Interactive candlestick charts with moving averages made using Plotly

    -   `forecast()`: Price forecast made using Prophet and visualization of predictions

-   **test_stockMarketAnalyzer.py**: Unit tests for components of the application
    -   Function existence and behavior tests
    -   Validation of data structure for correct format of financial information
-   Validation of moving averages calculations
-   Validation of the date for selecting the proper time range

## How It Works

1. **Data Retrieval**:

    - The yfinance library is utilized by the application to call Yahoo Finance's large financial data API
    - Upon a user's selection of a stock and date range, the `getting_data()` function retrieves historical data

-   The data fetching process is optimized using Streamlit's `@st.cache_data` decorator to cache results in memory
-   The system manages possible exceptions that occur while fetching data and returns sensible error messages
-   Data fetched includes Date, Open, High, Low, Close prices, and trading Volume for complete analysis

2. **Data Processing and Visualization:**

-   The raw data is preprocessed to compute technical indicators such as moving averages
    -   A 5-day moving average (MA5) displays short-run price trends whereas the 20-day moving average (MA20) represents medium-run trends
    -   The app employs Plotly to display an interactive dual-panel graph:
-   The upper panel displays candlestick patterns showing price action and volatility - The lower panel plots the moving averages to highlight trend direction and potential crossovers
    -   The visualization is fully interactive, allowing users to zoom, pan, and hover for detailed information
-   A bespoke layout guarantees the best possible rendering of price data with appropriate scaling and labels

3. **Forecasting**:

    - In the case of enabling forecasting, the system converts the historical data to a form that is appropriate for time series analysis
    - Facebook Prophet is used to detect patterns in the data, including:

-   Seasonality yearly: Yearly trends in stock performance - Seasonality weekly: Day-of-the-week influence on price movement - Trends overall: Directional long-term movement
    -   The model makes predictions for 365 days ahead with confidence intervals
    -   Two plots are created:
-   The plot of the forecast with predicted values and historical data with ranges of uncertainty
-   Component plots to decompose the forecast into trend, yearly, and weekly components
-   It helps users not only to comprehend what the future price could be but also why the model is expecting those values

4. **User Experience Flow:**

-   Step-by-step guidance through the analysis process is facilitated by the intuitive interface of the application
    -   Users are prompted to input compatible date ranges and proper stock symbols by input validation
    -   The user interface adjusts to varying screen sizes for desktop and mobile use with responsive design
    -   Real-time feedback is given at every step, ranging from data loading to chart creation
-   Error handling mechanisms give precise instructions when problems occur, enhancing user experience

## Acknowledgments

-   Yahoo Finance API for free stock market data provision
-   Facebook Prophet for time series forecasting functionality
-   Streamlit for the interactive web app framework
-   Plotly for interactive financial visualizations
-   The Python community for the development and maintenance of the necessary libraries utilized in this project
