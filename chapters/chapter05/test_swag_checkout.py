import chapters.chapter05.swag_actions as Swag

def test_checkout_success_with_one_item(py, login):
    Swag.add_first_item_to_cart(py)
    Swag.start_checkout(py)
    Swag.enter_shipping_info(py, 'Jonathan', "Brull Schroeder", "7600")
    Swag.confirm_checkout(py)
    assert py.contains('THANK YOU FOR YOUR ORDER')