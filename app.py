import yfinance as yf
import streamlit as st 
from PIL import Image
from urllib.request import urlopen


#TITLES
st.title("Cryptocurrency Price Analysis")
st.header("Main Dashboard")
st.subheader("This app retrieves cryptocurrency prices")

Bitcoin = 'BTC-USD'
Ethereum = 'ETH-USD'
Ripple='XRP-USD'
BitcoinCash = 'BCH-USD'

BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)
XRP_Data = yf.Ticker(Ripple)
BCH_Data = yf.Ticker(BitcoinCash)

BTCHis = BTC_Data.history(period="max")
ETHHis = BTC_Data.history(period="max")
XRPHis = BTC_Data.history(period="max")
BCHHis = BTC_Data.history(period="max")

#
BTC = yf.download(Bitcoin, start="2022-07-19", end="2022-07-19")
ETH = yf.download(Ethereum, start="2022-07-19", end="2022-07-19")
XRP = yf.download(Ripple, start="2022-07-19", end="2022-07-19")
BCH = yf.download(BitcoinCash, start="2022-07-19", end="2022-07-19")

#Bitcoin
st.write("BITCOIN ($)")
imageBTC = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))

st.image(imageBTC)

st.table(BTC)

st.bar_chart(BTCHis.Close)

#Etherum
st.write("Etherum ($)")
imageETH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png'))

st.image(imageETH)

st.table(ETH)

st.bar_chart(ETHHis.Close)

#Ripple
st.write("Ripple ($)")
imageXRP = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/52.png'))

st.image(imageXRP)

st.table(XRP)

st.bar_chart(XRPHis.Close)

#BitcoinCash
st.write("BITCOIN CASH ($)")
imageBCH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1831.png'))

st.image(imageBCH)

st.table(BCH)

st.bar_chart(BCHHis.Close)


