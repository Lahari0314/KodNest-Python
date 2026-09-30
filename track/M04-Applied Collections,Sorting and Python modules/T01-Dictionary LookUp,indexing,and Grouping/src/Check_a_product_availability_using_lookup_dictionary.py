def check(inventory,code):
    if code in inventory:
        if inventory[code]>0:
            return f"Available: {inventory[code]}"
        else:
            return "Out of stock"
    else:
        return "Product not found"

inventory={
    "P01":12,
    "P02":0,
    "P03":10,
    "P04":3,
}
required=input()
print(check(inventory,required))