
def validate_order(symbol, side, order_type, quantity, price=None):
    side = side.upper()
    order_type = order_type.upper()

    if side not in ["BUY","SELL"]:
        raise ValueError("Side must be BUY or SELL")
    
    if order_type not in ["MARKET","LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")
    
    try:
        quantity = float(quantity)
        if quantity < 0:
            raise ValueError("Quantity must be greater than 0")
    except:
        raise ValueError("Quantity must be a valid number")
    
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for Limit order")
        try:
            price = float(price)
            if price < 0:
                raise ValueError("Price must be greater than 0")
        except:
            raise ValueError("Price must be a valid number")