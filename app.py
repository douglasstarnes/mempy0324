from datetime import datetime

def new_investment(coin, quantity, buy=True):
    return {
        "coin": coin,
        "quantity": quantity,
        "buy": buy,
        "timestamp": datetime.now()
    }

portfolio = [
    new_investment("bitcoin", 1.3), 
    new_investment("ethereum", 13.4), 
    new_investment("ethereum", 3.4, False)
]

for investment in portfolio:
    if investment["buy"]:
        buy_sell = "bought"
    else:
        buy_sell = "sold"
    ts = investment["timestamp"].strftime("%Y/%m/%d %H:%M:%S")
    print(f"You {buy_sell} {investment['quantity']} {investment['coin']} on {ts}")