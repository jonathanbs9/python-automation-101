from chapters.chapter05 import swag_product_page

# Z to A
def test_sort_by_name_from_z_to_a(py, login):
    # 1 Select Z to A
    swag_product_page.sort_products_by(py,'Name (Z to A)' )
    
    # 2 Get a list of all items names
    items_names = swag_product_page.get_item_names(py)

    # 3 Check if it's in right order
    expected_item_names = items_names.copy()
    expected_item_names.sort(reverse=True)

    assert expected_item_names == items_names

# A to Z
def test_sort_by_name_from_a_to_z(py, login):
    # 1 Select Z to A
    swag_product_page.sort_products_by(py,'Name (A to Z)' )
    
    # 2 Get a list of all items names
    items_names = swag_product_page.get_item_names(py)

    # 3 Check if it's in right order
    expected_item_names = items_names.copy()
    expected_item_names.sort(reverse=False)
    
    assert expected_item_names == items_names

# High to Low
def test_sort_by_price_from_high_to_low(py, login):
    # 1 Select High to Low
    swag_product_page.sort_products_by(py,'Price (high to low)' )
    
    # 2 Get a list of all items prices
    items_prices = swag_product_page.get_item_prices(py)

    # 3 Check if it's in right order
    expected_item_prices = items_prices.copy()
    expected_item_prices.sort(reverse=True)

    assert expected_item_prices == items_prices

# Low to High
def test_sort_by_price_from_low_to_high(py, login):
    # 1 Select High to Low
    swag_product_page.sort_products_by(py,'Price (low to high)' )
    
    # 2 Get a list of all items prices
    items_prices = swag_product_page.get_item_prices(py)

    # 3 Check if it's in right order
    expected_item_prices = items_prices.copy()
    expected_item_prices.sort(reverse=False)

    assert expected_item_prices == items_prices