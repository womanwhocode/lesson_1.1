# -*- coding: utf-8 -*-

from model.contact import Contact


def test_untitled_test_case(app):
    app.group.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.open_contact_page()
    app.contact.create(Contact(user_firstname="alena", user_middlename="z", user_lastname="y", user_nickname="alenaomg", photo_path="/Users/alyona_zaytseva/Downloads/IMG_5814.JPG", user_title="piter", company_name="nestle", address="tujx", home_address="derlin", mobile_phone="7788",
                       work_phone="ksl;", fax_phone="dksls", email_1="almc c", email_2="fdnjdl", email_3="mdldsl", homepage="dnmdd", b_day="11", b_month="October", b_year="7777", a_day="13",
                       a_month="July", a_year="666", address_2="tetst", phone_2="ydhn", notes="jdkld"))
    app.group.open_home_page()
    app.session.logout()
