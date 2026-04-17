import streamlit as st
from bot.validators import validate_order
from bot.logging_config import setup_logger
from bot.orders import place_order
from bot.client import get_client
import logging

st.set_page_config(page_title="Futures Trading bot", layout="centered")

st.markdown("<h1 style='text-align:center; color:RGB(200,200,0);'>Binance Futures Trading Bot</h1>", unsafe_allow_html=True)
# st.title("Binance Futures Trading Bot", anchor=False)

st.markdown("---")

symbol = st.text_input("Symbol",value="BTCUSDT")

side = st.selectbox("Side",["BUY","SELL"])

order_type = st.selectbox("Order type", ["MARKET","LIMIT"])

quantity = st.number_input("Quantity", min_value=0.0, step=0.000100, format="%.6f")

price=None
if order_type == "LIMIT":
    price = st.number_input("Price", min_value=0.0, format='%.2f')

st.markdown("---")

if "logger_initialized" not in st.session_state:
    setup_logger()
    st.session_state.logger_initialized = True

if st.button("Place Order", type="primary", use_container_width=True):
    try:
        #normalize
        symbol = symbol.upper()
        side = side.upper()
        order_type = order_type.upper()
        
        validate_order(symbol, side, order_type, quantity, price)
        
        client = get_client()
        
        logging.info(
            "Order Request: %s",
            {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity,
                "price": price
            }
        )
        with st.spinner("Placing order..."):
            order = place_order(client, symbol, side, order_type, quantity, price)
        
        st.success("Order placed successfully")
        
        logging.info(f"Order Response: {order}")

        st.subheader("📊 Order Details")
        st.write(f"OrderID: {order['orderId']}")
        st.write(f"Symbol :{order['symbol']}")
        st.write(f"Status :{order['status']}")
        st.write(f"Executed Qty :{order['executedQty']}")
        if 'price' in order:
            st.write(f"Price :{order['price']}")
        if 'avgPrice' in order:
            st.write(f"Average Price: {order['avgPrice']}")
 

    except Exception as e:
        st.error(f"Error:{str(e)}")
        logging.error(f"Error: {str(e)}")
