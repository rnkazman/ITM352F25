recent_purchases = [36.13, 23.87, 183.35, 22.93, 11.82]
budget = 50
total_spent = 0
for purchase in recent_purchases:
    total_spent += purchase
rounded_total = round(total_spent, 2)
if total_spent > budget:
    print(f"You spent ${total_spent:.2f} which is over budget")
else:
    print(f"You spent ${total_spent:.2f} which is within budget")
