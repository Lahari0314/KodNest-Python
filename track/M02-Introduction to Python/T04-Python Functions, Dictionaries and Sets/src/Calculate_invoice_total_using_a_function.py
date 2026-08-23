def invoice_total(price,quantity):
    total=price*quantity
    print("Total:",total)

price=int(input())
quantity=int(input())
invoice_total(price,quantity)