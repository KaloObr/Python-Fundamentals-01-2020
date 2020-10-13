def validate_key_existing(dictionary, key, def_value):
    if key not in dictionary:
        dictionary[key] = def_value
    else:
        dictionary[key] += def_value


def print_k_v_dictionary(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(k, v))


products_quantity = {}
products_prices = {}
final_products = {}

while True:
    stock = input()
    if stock == "buy":
        break
    name, price, quantity = stock.split()

    validate_key_existing(products_quantity, name, float(quantity))
    validate_key_existing(products_prices, name, float(price))
    products_prices[name] = float(price)

    for key in products_prices.keys():
        final_price = products_quantity[key] * products_prices[key]
        final_products[key] = final_price

print_k_v_dictionary(final_products, "{} -> {:.2f}")
