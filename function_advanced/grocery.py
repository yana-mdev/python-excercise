def grocery_store(**kwargs):
    sorted_kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

    result = []
    for product_name, product_quantity in sorted_kwargs:
        result.append(f"{product_name}: {product_quantity}")

    return "\n".join(result)




print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
