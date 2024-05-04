from datetime import datetime

name = input("Enter your name:")

lists = '''
rice            Rs 30/kg
sugar           Rs 20/kg
salt            Rs 15/kg
chicken masala  Rs 200/kg
garam masala    Rs 200/kg 
colgate         Rs 50/each
dhaniya masala  Rs 100/kg
brush           Rs 20/each
'''

items = {
    "rice": 30,
    "sugar": 20,
    "salt": 15,
    "chicken masala": 200,
    "garam masala": 200,
    "colgate": 50,
    "dhaniya masala": 100,
    "brush": 20
}

price_list = []
ilist = []
qlist = []
plist = []

total_price = 0

option = int(input("For list of items press 1: "))

if option == 1:
    print(lists)
    while True:
        order = input("Enter the items you want to buy and their quantities (item1 quantity1, item2 quantity2, ...): ")
        order_items = order.split(",")
        try:
            for order_item in order_items:
                item, quantity = order_item.strip().split()
                if item in items:
                    quantity = int(quantity)
                    price = quantity * items[item]
                    price_list.append((item, quantity, items[item], price))
                    total_price += price
                    ilist.append(item)
                    qlist.append(quantity)
                    plist.append(price)
                else:
                    print(f"The item '{item}' is not available")
        except ValueError:
            print("please check once again and enter items and quantities separated by spaces.")

        ruhi = input("Can I bill the items? (yes/no): ")
        if ruhi.lower() == 'yes':
            break

    gst = (total_price * 5) / 100
    final_price = gst + total_price

    print(26 * "=", "Amma Supermarket", 30 * "=")
    print("Name:", name, 30 * " ", "Date:", datetime.now())
    print(75 * "-")
    print("sno", 15 * " ", "items", 15 * " ", "quantity", 15 * " ", "price")
    for i in range(len(price_list)):
         print(1 * "", i, 17 * " ", ilist[i], 18 * " ", qlist[i], 19 * " ", plist[i])
    print(75 * "-")
    print("TotalAmount  :", 5 * " ", 'Rs', total_price)
    print("GST Amount   :", 5 * " ", 'Rs', gst)
    print(75 * "-")
    print("FinalAmount  :", 5 * " ", "Rs", final_price)
    print(37 * "=-")
    print(26 * " ", "Thanks for Visiting", 26 * " ")
    print(37 * "=-")
