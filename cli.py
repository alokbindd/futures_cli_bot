import argparse
import logging
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logger

def main():
    setup_logger()

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot CLI")

    parser.add_argument("--symbol", required=True, help="Trading pair symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="Order side: BUY or SELL")
    parser.add_argument("--type", required=True, help="Order type: MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, help="Order quantity (e.g., 0.001)")
    parser.add_argument("--price", required=False, help="Price required for LIMIT orders (e.g., 60000)")
    
    args = parser.parse_args()

    try:
        validate_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price,
        )
        
        client = get_client()

        print("\nOrder request summary")
        print(f"Symbol: {args.symbol.upper()}")
        print(f"Side: {args.side.upper()}")
        print(f"Type: {args.type.upper()}")
        print(f"Quantity: {args.quantity}")
        if args.price:
            print(f"Price: {args.price}")

        logging.info(f"Order Request: {vars(args)}")
        
        order = place_order(
            client,
            args.symbol.upper(),
            args.side.upper(),
            args.type.upper(),
            args.quantity,
            args.price,
        )
        print("\n-------------------------------")
        print("\nOrder successful!")
        print(f"Order ID: {order['orderId']}")
        print(f"Symbol: {order['symbol']}")
        print(f"Status: {order['status']}")
        print(f"Executed Qty: {order['executedQty']}")
        if "avgPrice" in order:
            print(f"Average Price: {order['avgPrice']}")
        
        logging.info(f"Order Response: {order}")
    except Exception as e:
        print("\n Error:", str(e))
        logging.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()