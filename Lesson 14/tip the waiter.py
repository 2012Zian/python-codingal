def total(bill_amount,tip_percentage):
    result = bill_amount * (1+0.01* tip_percentage)
    result = round(result,2)
    print("please pay the bill",result)

total(700,30)