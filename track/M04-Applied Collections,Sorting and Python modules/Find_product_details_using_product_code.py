def find(products,code):
    if code in products:
        return products[code]
    return None

products={
    "P01":{"name":"KeyBoard","price":1200},
    "P02":{"name":"Mouse","price":600},
    "P03":{"name":"Monitor","price":8500},
    "P04":{"name":"HeadPhones","price":1500}
}
code=input()
result=find(products,code)
if result is not None:
    print(result["name"])
    print(result["price"])
else:
    print("Product not Found")