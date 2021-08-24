def sort_products_by(py, sort_name):
    py.get('select.product_sort_container').select(sort_name)

def get_item_names(py):
    items_names = []
    for item in py.find(".inventory_item_name"):
        items_names.append(item.text())
    return items_names

def get_item_prices(py):
    items_prices = []
    for item in py.find(".inventory_item_price"):
        price = item.text().replace('$','')
        items_prices.append(float(price))
    return items_prices