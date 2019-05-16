# -*- coding: utf-8 -*-

from model.contact import Contact
from sys import maxsize


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.open_contact_page()
    contact = Contact(user_firstname="alena_2", user_middlename="z", user_lastname="y", user_nickname="alenaomg", photo_path="/Users/alyona_zaytseva/Downloads/IMG_5814.JPG", user_title="piter", company_name="nestle", address="tujx", home_address="derlin", mobile_phone="7788",
                       work_phone="ksl;", fax_phone="dksls", email_1="almc c", email_2="fdnjdl", email_3="mdldsl", homepage="dnmdd", b_day="11", b_month="October", b_year="7777", a_day="13",
                       a_month="July", a_year="666", address_2="tetst", phone_2="ydhn", notes="jdkld")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    def id_or_max(con):
        if con.id:
            return int(con.id)
        else:
            return maxsize
    assert sorted(old_contacts, key=id_or_max) == sorted(new_contacts, key=id_or_max)

