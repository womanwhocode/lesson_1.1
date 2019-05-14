from model.contact import Contact


def test_delete_some_contact(app):
    if app.contact.count == 0:
        app.contact.create(Contact(user_firstname="alena new new"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
