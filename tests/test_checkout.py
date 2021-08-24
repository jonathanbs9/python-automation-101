from swag.actions import actions

def test_checkout_success_with_one_item(py, login):
    actions.add_first_item_to_cart(py)
    actions.start_checkout(py)
    actions.enter_shipping_info(py, 'Jonathan', "Brull Schroeder", "7600")
    actions.confirm_checkout(py)
    assert py.contains('THANK YOU FOR YOUR ORDER')