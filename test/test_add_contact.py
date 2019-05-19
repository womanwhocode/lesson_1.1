# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.open_create_contact_page()
    contact = Contact(user_firstname="alena_3", user_middlename="z", user_lastname="y", user_nickname="alenaomg", photo_path="/Users/alyona_zaytseva/Downloads/IMG_5814.JPG", user_title="piter", company_name="nestle", address="tujx", home_address="derlin", mobile_phone="7788",
                       work_phone="ksl;", fax_phone="dksls", email_1="almc c", email_2="fdnjdl", email_3="mdldsl", homepage="dnmdd", b_day="11", b_month="October", b_year="7777", a_day="13",
                       a_month="July", a_year="666", address_2="tetst", phone_2="ydhn", notes="jdkld")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_add_empty_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     app.contact.open_create_contact_page()
#     contact = Contact(user_firstname="", user_middlename="", user_lastname="", user_nickname="",
#                       user_title="",
#                       company_name="", address="", home_address="", mobile_phone="",
#                       work_phone="", fax_phone="", email_1="", email_2="", email_3="",
#                       homepage="", b_day="", b_month="", b_year="", a_day="",
#                       a_month="", a_year="", address_2="", phone_2="", notes="")
#     app.contact.fill_contact_form(contact)
#     app.contact.submit_add_contact()
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
