# Task 1

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('Beetroot is a great academy'))


# Task 2

def calculate_total_stock_price(stock, prices):
    total_price = 0
    for item, quantity in stock.items():
        if item in prices:
            total_price += prices[item] * quantity
    return total_price

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_price = calculate_total_stock_price(stock, prices)
print("Total Price of Stock: ", total_price)


# Task 3

result = []
for i in range(1, 11):
    result.append((i, i ** 2))

print(result)

