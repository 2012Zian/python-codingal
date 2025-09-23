actualcost = float(input("enter your first price"))
sellingcost = float(input("enter your selling price"))

if sellingcost>actualcost:
    profit = sellingcost - actualcost
    print("this is the profit ",profit)

else:
    print("your in loss")