
from model.contact import Contact


def test_modify_contact_user_firstname(app):
    app.contact.open_home_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(user_firstname="alena_new_4"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
