from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@given("I am on the Demo Login Page")
def step_open_login_page(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open_login_page()

@when("I fill the account information for account {username} into the Username field and {password} into the Password field")
def step_fill_credentials(context, username, password):
    context.login_page.fill_credentials(username, password)

@when("I click the Login Button")
def step_click_login(context):
    context.login_page.click_login_button()

@then("I am redirected to the Demo Main Page")
def step_verify_inventory_page(context):
    assert context.driver.current_url == "https://www.saucedemo.com/inventory.html"

@then("I verify the App Logo exists")
def step_verify_logo(context):
    assert context.login_page.is_logo_displayed()

@then("I verify the error message \"{error_message}\"")
def step_verify_error(context, error_message):
    assert context.login_page.get_error_message() == error_message

@given("I am logged in")
def step_logged_in(context):
    context.login_page.login("standard_user", "secret_sauce")

@when("I am on the inventory page")
def step_on_inventory_page(context):
    context.inventory_page = InventoryPage(context.driver)
    assert context.inventory_page.is_on_inventory_page()

@then("I extract content from the web page And save it to a text file")
def step_extract_content(context):
    context.inventory_page.extract_inventory_data("inventory_data.txt")

@then("I log out")
def step_logout(context):
    context.inventory_page.logout()

@then("I verify I am on the Login page again")
def step_verify_login_page(context):
    assert context.driver.current_url == "https://www.saucedemo.com/"