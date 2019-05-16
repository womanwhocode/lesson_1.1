from selenium.webdriver.support.ui import Select
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/index.php")

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//img[@alt='Edit'])[2]").click()
        wd.find_element_by_xpath("//div[@id='nav']/ul/li[2]/a").click()

    def create(self, contact):
        wd = self.app.wd
        self.fill_contact_form(contact)
        self.choose_data(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field("firstname", contact.user_firstname)
        self.change_field("middlename", contact.user_middlename)
        self.change_field("lastname", contact.user_lastname)
        self.change_field("nickname", contact.user_nickname)
        wd.find_element_by_name("photo").clear()
        wd.find_element_by_name("photo").send_keys(contact.photo_path)
        self.change_field("title", contact.user_title)
        self.change_field("company", contact.company_name)
        self.change_field("address", contact.address)
        self.change_field("home", contact.home_address)
        self.change_field("mobile", contact.mobile_phone)
        self.change_field("work", contact.work_phone)
        self.change_field("fax", contact.fax_phone)
        self.change_field("email", contact.email_1)
        self.change_field("email2", contact.email_2)
        self.change_field("email3", contact.email_3)
        self.change_field("homepage", contact.homepage)
        self.change_field("byear", contact.b_year)
        self.change_field("ayear", contact.a_year)
        self.change_field("address2", contact.address_2)
        self.change_field("phone2", contact.phone_2)
        self.change_field("notes", contact.notes)

    def choose_data(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.b_day)
        wd.find_element_by_xpath("//option[@value='11']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.b_month)
        wd.find_element_by_xpath("//option[@value='October']").click()
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.a_day)
        wd.find_element_by_xpath("(//option[@value='13'])[2]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.a_month)
        wd.find_element_by_xpath("(//option[@value='July'])[2]").click()

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def edit_contact(self, app):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit'])[2]").click()
        app.contact.create()
        wd.find_element_by_name("update").click()

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_home_page()
        contacts = []
        for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
            id = element.find_element_by_xpath("./td[1]/input").get_attribute('value')
            text = element.find_element_by_xpath("./td[3]").text
            contacts.append(Contact(id=id, user_firstname=text))
        return contacts



