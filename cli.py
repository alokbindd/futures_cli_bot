import argparse
import logging
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logger

def main():
    setup_logger()

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot CLI")

    parser.add_argument("--symbol", required=False, help="Trading pair symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=False, help="Order side: BUY or SELL")
    parser.add_argument("--type", required=False, help="Order type: MARKET or LIMIT")
    parser.add_argument("--quantity", required=False, help="Order quantity (e.g., 0.001)")
    parser.add_argument("--price", required=False, help="Price required for LIMIT orders (e.g., 60000)")
    
    args = parser.parse_args()
    
    if not all([args.symbol, args.side, args.type, args.quantity]):
        print("\nSome inputs are missing. Please provide them: ")
        print("------------------------------------------------")

    if not args.symbol:
        args.symbol = input("Enter symbol (e.g., BTCUSDT): ")
    if not args.side:
        args.side = input("Enter side (BUY/SELL): ")
    if not args.type:
        args.type = input("Enter type (MARKET/LIMIT): ").upper()
        print(args.type)
    if not args.quantity:
        args.quantity = input("Enter Quantity (e.g., 0.001): ")
    
    if args.type.upper() == "LIMIT" and not args.price:
        args.price = input("Enter price: ")

    # if not all([args.symbol, args.side, args.type, args.quantity]):
    #     print("Missing arguments. Switching to interactive mode...\n")

    #     args.symbol = input("Enter Symbol: ")
    #     args.side = input("Enter side (BUY/SELL): ")
    #     args.type = input("Enter type (MARKET/LIMIT): ")
    #     args.quantity = input("Enter quantity: ")
    #     if args.type.upper() == "LIMIT": 
    #         args.price = input("Enter Price: ")
    
    try:
        if args.quantity:
            args.quantity = float(args.quantity)
        if args.price:
            args.price = float(args.price)
    except ValueError as v :
        print("Quantity and price must be valid numbers")
        logging.error("Invalid numeric input for quantity or price")
        return
    
    args.symbol = args.symbol.upper()
    args.side = args.side.upper()
    args.type = args.type.upper()
    
    try:
        validate_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price,
        )
        
        client = get_client()

        print("------------------------------------------------")

        print("Order request summary")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")

        if args.price:
            print(f"Price: {args.price}")
        print("------------------------------------------------")

        logging.info(f"Order Request: {vars(args)}")

        while True:
            confirmation = input("Are you sure you want to place this order? (y/n):").upper() 
            if confirmation in ["Y","N"]:
                break
            else:
                print("Enter a valid input! (y/n)")

        if confirmation == "Y":        
            order = place_order(
                client,
                args.symbol,
                args.side,
                args.type,
                args.quantity,
                args.price,
            )
            print("------------------------------------------------")

            print("Order Placed successfully")
            print(f"Order ID: {order['orderId']}")
            print(f"Symbol: {order['symbol']}")
            print(f"Status: {order['status']}")
            print(f"Executed Qty: {order['executedQty']}")
            if "avgPrice" in order:
                print(f"Average Price: {order['avgPrice']}")
            print("------------------------------------------------")
                
            logging.info(f"Order Response: {order}")

        elif confirmation == "N":
            print("Order cancelled by user")
            logging.info(f"Order cancelled by user")


    except Exception as e:
        print("\n Error:", str(e))
        logging.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()