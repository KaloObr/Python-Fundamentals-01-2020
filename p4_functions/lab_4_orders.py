def order_calc(order, rep):
    result = 0
    if order == 'coffee':
        result += rep * 1.50
    elif order == 'water':
        result += rep * 1.00
    elif order == 'coke':
        result += rep * 1.40
    else:
        result += rep * 2.00
    return result


product = input()
quontity = int(input())

print(f'{order_calc(product, quontity):.2f}')
