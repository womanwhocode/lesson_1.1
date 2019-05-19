
from model.contact import Contact
from random import randrange


def test_modify_contact_user_firstname(app):
    app.contact.open_home_page()
    if app.contact.count == 0:
        app.contact.create(Contact(user_firstname="alena new new"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(user_firstname="alena_new_4")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
