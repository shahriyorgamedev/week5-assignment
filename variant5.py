


def add_product(products, prices, new_product, new_price):
    if new_product not in products:
        products.append(new_product)
        prices.append(new_price)



def remove_product(products, prices, product_to_remove):
    if product_to_remove in products:
        index = products.index(product_to_remove)
        products.pop(index)
        prices.pop(index)
        return True
    return False



def get_most_valuable(products, prices, count):
    result = []

    product_copy = products[:]
    price_copy = prices[:]

    for time in range(count):
        highest = max(price_copy)
        index = price_copy.index(highest)

        result.append((product_copy[index], highest))

        price_copy.pop(index)
        product_copy.pop(index)
    return result



def manage_inventory(initial_products, initial_prices, new_product_data, product_to_remove, top_count):
    new_price = new_product_data[1]
    new_product = new_product_data[0]
    add_product(initial_products,initial_prices,new_product,new_price)
    remove_product(initial_products,initial_prices,product_to_remove)
    top_products = get_most_valuable(initial_products,initial_prices,top_count)

    return f'Final Products: {initial_products}\n Top Products: {top_products}'



products = ["Watch", "Ring", "Bag", "Scarf", "Pen"]
prices = [5500.00, 7200.00, 3100.00, 800.00, 1200.00]
new_product = ["Statue", 6800.00]
remove_name = "Scarf"
count = 3

print(manage_inventory(products,prices,new_product,remove_name,count))
