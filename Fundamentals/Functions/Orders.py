product = input()
quantity = int(input())


def solve(product, quantity):
    result = None
    if product == "coffee":
        result = quantity * 1.50
    elif product == "coke":
        result = quantity * 1.40
    elif product == "water":
        result = quantity * 1.00
    elif product == "snacks":
        result = quantity * 2.00
    return (f"{result:.2f}")


print(solve(product,quantity))