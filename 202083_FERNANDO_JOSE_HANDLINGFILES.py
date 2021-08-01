products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

def get_product(code):
    x = products[code]
    return x

def get_property(code, property):
    y = products[code][property]
    return y

def main():

    formatting_list = {}
    order_dict = {}
    sorted_list = []
    while(True):
        try:
            code, product_quantity = [x for x in input("Input order, quantity: (Please use a comma to separate your answers.) (Input '/' when done) ").split(",")]
            if code != "/":
                price = float(get_property(code,"price"))
                subtotal = price*float(product_quantity)
                name = get_property(code,"name")
                if code in order_dict:
                    order_dict[code]["quantity"] += int(product_quantity.strip())
                    order_dict[code]["subtotal"] += float(subtotal)
                    continue
                else:
                    order_dict[code] = {"code":code,"name":name, "quantity": int(product_quantity.strip()), "subtotal": float(subtotal) }
                    continue
                continue
            continue
        except ValueError:
            sorted_list.append(order_dict)
            sorted_list = list(sorted_list[0].items())
            sorted_list.sort()
            total = 0
            for x in sorted_list:
                total += x[1]["subtotal"]
                continue
            break

    file = open("receipt.txt","w")

    file.write('''
==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL''')

    for x in sorted_list:
        if x[0] == "dalgona":
            file.write(f'''
{x[1]["code"]}\t\t\t{x[1]["name"]}\t\t\t{x[1]["quantity"]}\t\t\t\t{x[1]["subtotal"]}''') ## had to insert this because formatting was only different for dalgona
        else:
            file.write(f'''
{x[1]["code"]}\t\t{x[1]["name"]}\t\t{x[1]["quantity"]}\t\t\t\t{x[1]["subtotal"]}''')

    file.write(f'''
    
Total:\t\t\t\t\t\t\t\t\t\t{total}
==
    ''')

main()
