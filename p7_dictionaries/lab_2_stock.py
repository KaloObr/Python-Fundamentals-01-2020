# Не мутирайте речник докато го обхождате.
def get_stock(raw_data):
    data = raw_data.split(' ')
    return {data[i]: int(data[i+1]) for i in range(0, len(data),2)}


def check_available(stock, search_products):
    result = ''
    for product in search_products:
        if not stock.get(product):
            result += f"Sorry, we don't have that {product}"
        else:
            result += f"We have{stock[product]} of {product}left"
    return result


stock = get_stock(input())
print(check_available(stock, input().split(' ')))


