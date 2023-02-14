balance = int(input())
to_cash = int(input())

money_left = balance - to_cash if (to_cash >= 500 and to_cash < balance) else "Error"

print(money_left)