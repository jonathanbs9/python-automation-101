def login_with(py, username, password):
    py.visit("https://www.saucedemo.com/")
    py.get("input[id='user-name'").type(username)
    py.get("input[id='password'").type(password)
    py.get("input[id='login-button'").click()

def add_first_item_to_cart(py):
    #py.get("buton[id='add-to-cart-sauce-labs-backpack'").click()
    py.contains("Add to cart").click()

def start_checkout(py):
    py.get("div[id='shopping_cart_container'").click()
    py.contains("Checkout").click()
    
def enter_shipping_info(py, first_name, last_name, zip_code):
    py.get('#first-name').type(first_name)
    py.get('#last-name').type(last_name)
    py.get('#postal-code').type(zip_code)
    py.get('[value="Continue"]').click()

def confirm_checkout(py):
    py.contains('Finish').click()