
def test_contact_info(app):
    contact_from_home_page = app.contact.get_contact_info_home_page_by_random()
    contact_from_edit__page = app.contact.get_contact_info_edit_page_by_random(contact_from_home_page)
