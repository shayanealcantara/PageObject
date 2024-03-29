from POMProjectDemo.Locators.locators import Locators

class LoginPage():

    # constructor with objects and its locators
    def __init__(self, driver):
        self.driver = driver

        # in case of changes, they will be made here
        # self.username_textbox_id = "txtUsername" ou
        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = "txtPassword"
        self.login_button_id = "btnLogin"
        self.invalidUsername_message_xpath = "//span[@id='spanMessage']"

    # actions
    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        # self.driver.find_element_by_id(self.username_textbox_id).send_keys(username) ou
        self.driver.find_element_by_id(Locators.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def check_invalid_username_message(self):
        msg = self.driver.find_element_by_xpath(self.invalidUsername_message_xpath).text
        return msg