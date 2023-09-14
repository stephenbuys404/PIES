#pandas
#plotly
#yfinance
import pandas
import yfinance as yf
import plotly.graph_objs as go

ticker='IBM'
fig:go._figure.Figure=go.Figure()
data:pandas.core.frame.DataFrame=yf.download(tickers=ticker, period='1d', interval='1m')
fig.add_trace(go.Candlestick(x=data.index,open=data['Open'],high=data['High'],low=data['Low'],close=data['Close'],name='market-data'))
fig.update_layout(title='live share price evolution',yaxis_title='Stock Price(USD per Shares)')
fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=5, label='5m', step='minute', stepmode='backward'),
            dict(count=15, label='15m', step='minute', stepmode='backward'),
            dict(count=45, label='45m', step='minute', stepmode='backward'),
            dict(count=1, label='HTD', step='hour', stepmode='todate'),
            dict(count=3, label='3h', step='hour', stepmode='backward'),
            dict(count=5, label='5h', step='hour', stepmode='backward'),
            dict(count=7, label='7h', step='hour', stepmode='backward'),
            dict(step='all')])))
fig.show()
