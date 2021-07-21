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

get_product("espresso")

def get_property(code, property):
    y = products[code][property]
    return y

get_property("espresso","price")

def main():

    formatting_list = {}
    sorted_list = []
    while(True):
        try:
            code, product_quantity = [x for x in input("Input order, quantity: (Please use a comma to separate your answers.) (Input '/' when done) ").split(",")]
            if code != "/":
                price = float(get_property(code,"price"))
                subtotal = price*float(product_quantity)
                name = get_property(code,"name")
                code_details = [code, name, product_quantity.strip(), subtotal]
                formatting_list[code] = code_details

                continue
            continue
        except ValueError:
            sorted_list = list(formatting_list.items())
            sorted_list.sort()
            total = 0
            for x in sorted_list:
                total += x[1][3]
                continue
            break

    file = open("receipt.txt","w")

    file.write('''
==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL
''')

    for x in sorted_list:
        if x[0] == "dalgona":
            file.write(f'''
{x[1][0]}\t\t\t{x[1][1]}\t\t\t{x[1][2]}\t\t\t\t{x[1][3]}''') ## had to insert this because formatting was only different for dalgona
        else:
            file.write(f'''
{x[1][0]}\t\t{x[1][1]}\t\t{x[1][2]}\t\t\t\t{x[1][3]}''')

    file.write(f'''
    
Total:\t\t\t\t\t\t\t\t\t\t{total}
==
    ''')
    file.close()

main()
