import streamlit as st
import requests
import json

#streamlit page config
st.set_page_config(
    page_title="Crypto Stonks",
    page_icon="https://cdn-icons-png.flaticon.com/512/4964/4964787.png",
    layout="wide",
    initial_sidebar_state="expanded"
)


# load the data
with open('cryptos.json', 'r') as json_file:
  data = json.load(json_file)

# Crypto Metric Data Display Function
def cyptoMetric(marketCap, price, change):
  st.metric(marketCap, price, change)
  st.write("------")

def main():
    st.title("Crypto Stonks:")
    st.divider()

    for crypto in data['cryptocurrencies']:
        st.subheader(crypto['name'])
        st.write(crypto['label'])
        cyptoMetric(crypto['market_cap'], crypto['price'], crypto['change'])

if __name__ == "__main__":
    main()
