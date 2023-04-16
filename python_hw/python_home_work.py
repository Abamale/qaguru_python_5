from datetime import time


def test_dark_theme():
    current_time = time(hour=23)
    is_dark_theme = current_time.hour > 22 or current_time.hour < 6

    assert is_dark_theme is True


def test_chenging_dark_theme():
    current_time = time(hour=16)
    dark_theme_enabled = True
    is_dark_theme = current_time.hour > 22 or current_time.hour < 6 or dark_theme_enabled

    assert is_dark_theme is True


def test_find_suitable_user():
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]
    suiable_user = None
    for i in users:
        if i["name"] == 'Olga':
            suiable_user = i

    assert suiable_user == {"name": "Olga", "age": 45}


def test_find_yangest_user():
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]
    suiable_users = [i for i in users if i['age'] < 20]

    assert suiable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login",
                                           button_text="Register")


def my_function(func, *args):
    func_name = func.__name__.replace('_', ' ').title()
    exact_args = ', '.join(args)

    return f"{func_name} [{exact_args}]"


def open_browser(browser_name):
    actual_result = my_function(open_browser, browser_name)

    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = my_function(go_to_companyname_homepage, page_url)

    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = my_function(find_registration_button_on_login_page, page_url, button_text)

    assert actual_result == """Find Registration Button On Login Page 
    [https://companyname.com/login, Register]"""