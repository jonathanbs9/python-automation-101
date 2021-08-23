from selenium.webdriver.common.keys import Keys

def test_search_for_ovejeros_alemanes(py):
    py.visit('https://www.google.com')
    py.get("input[name='q'").type('ovejero aleman', Keys.ENTER)


    assert py.should().contain_title("ovejero aleman")
    
    