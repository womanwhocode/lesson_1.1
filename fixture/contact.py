from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re
from random import randrange


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/index.php")

    def open_create_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//img[@alt='Edit'])[2]").click()
        wd.find_element_by_xpath("//div[@id='nav']/ul/li[2]/a").click()

    def create(self, contact):
        wd = self.app.wd
        self.fill_contact_form(contact)
        self.send_photo(contact)
        self.choose_data(contact)
        self.submit_add_contact()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field("firstname", contact.user_firstname)
        self.change_field("middlename", contact.user_middlename)
        self.change_field("lastname", contact.user_lastname)
        self.change_field("nickname", contact.user_nickname)
        self.change_field("title", contact.user_title)
        self.change_field("company", contact.company_name)
        self.change_field("address", contact.address)
        self.change_field("home", contact.home_phone)
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

    def submit_add_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def send_photo(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("photo").clear()
        wd.find_element_by_name("photo").send_keys(contact.photo_path)

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
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # wd.find_element_by_name("selected[]").click()
        # wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        #self.open_home_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//td[8]/a/img").click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def modify_first_group(self):
        wd = self.app.wd
        self.modify_contact_by_index(0)

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            contacts = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                id = element.find_element_by_xpath("./td[1]/input").get_attribute('value')
                firstname = element.find_element_by_xpath("./td[3]").text
                all_phones = element.find_element_by_xpath("./td[6]").text
                contacts.append(Contact(id=id, user_firstname=firstname, all_phones_from_home_page=all_phones))
            return list(contacts)

    def get_contact_info_home_page_by_random(self):
        wd = self.app.wd
        self.open_home_page()
        contacts = wd.find_elements_by_xpath("//tr[@name='entry']")
        random_index = randrange(len(contacts))
        contact = contacts[random_index]
        id = contact.find_element_by_xpath("./td[1]/input").get_attribute('value')
        first_name = contact.find_element_by_xpath("./td[3]").text
        last_name = contact.find_element_by_xpath("./td[2]").text
        address = contact.find_element_by_xpath("./td[4]").text
        all_emails = contact.find_element_by_xpath("./td[5]").text
        all_phones = contact.find_element_by_xpath("./td[6]").text
        contact.append(Contact(id=id, user_firstname=first_name, user_lastname=last_name, address=address,
                               all_emails_from_home_page=all_emails,
                               all_phones_from_home_page=all_phones))
        return Contact(id=id, user_firstname=first_name, user_lastname=last_name, address=address,
                               all_emails_from_home_page=all_emails,
                               all_phones_from_home_page=all_phones)

    def get_contact_info_edit_page_by_random(self, contact_from_home_page):
        wd = self.app.wd
        contacts = wd.find_elements_by_xpath("//tr[@name='entry']")
        index = contacts.index(contact_from_home_page)
        self.open_home_page()
        wd.find_element_by_xpath("//td["+index+"]/a/img").click()


    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//td[8]/a/img").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        fax_phone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(user_firstname=firstname, user_lastname=lastname, home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone, fax_phone=fax_phone, id=id)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        fax_phone = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone, fax_phone=fax_phone, id=id)



