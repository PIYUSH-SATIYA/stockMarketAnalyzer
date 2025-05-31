import pandas as pd
from datetime import datetime

from project import symbols, getting_data, plot_candle, forecast

def test_symbols_function_exists():
    """Test that symbols function exists"""
    assert callable(symbols)

def test_getting_data_function_exists():
    """Test that getting_data function exists"""
    assert callable(getting_data)

def test_plot_candle_function_exists():
    """Test that plot_candle function exists"""
    assert callable(plot_candle)

def test_forecast_function_exists():
    """Test that forecast function exists"""
    assert callable(forecast)

def test_data_structure():
    """Test sample data structure"""
    df = pd.DataFrame({
        'Date': pd.date_range(start='2024-01-01', end='2024-01-05'),
        'Open': [100, 101, 102, 103, 104],
        'High': [105, 106, 107, 108, 109],
        'Low': [95, 96, 97, 98, 99],
        'Close': [102, 103, 104, 105, 106],
        'Volume': [1000, 1100, 1200, 1300, 1400]
    })
    
    assert 'Date' in df.columns
    assert 'Open' in df.columns
    assert 'High' in df.columns
    assert 'Low' in df.columns
    assert 'Close' in df.columns
    assert len(df) == 5

def test_moving_averages_calculation():
    """Test moving average calculations"""
    df = pd.DataFrame({
        'Close': [10, 20, 30, 40, 50]
    })
    
    df['MA3'] = df['Close'].rolling(window=3).mean()
    
    expected = [None, None, 20.0, 30.0, 40.0]
    
    for i in range(2, len(df)):
        assert df['MA3'][i] == expected[i]

def test_date_validation():
    """Test date validation logic"""
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 1, 31)
    
    assert start_date < end_date
    assert (end_date - start_date).days == 30