
from model.contact import Contact


def test_modify_contact_user_firstname(app):
    app.contact.open_home_page()
    old_contacts = app.contact.get_contact_list()
    contact = Contact(user_firstname="alena_new_4")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
