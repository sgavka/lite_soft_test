import json


def filter(numbers: set, products: list[dict]):
    return [product for product in products if len(set(str(product['productCode'])).intersection(numbers)) > 0]


if __name__ == '__main__':
    numbers = input('Enter numbers to filter (or just press enter for default: 9, 3, 8, 2): ')
    numbers = ''.join([char for char in numbers if char.isdigit()])
    numbers = set(numbers)

    filename = 'product_test.json'
    products = json.load(open(filename, 'r'))

    result = filter(numbers, products)

    print(f'Filtered products: {len(result)}.')
    for product in result:
        print(f'Product: {product["name"]}, Number: {product["productCode"]}')
