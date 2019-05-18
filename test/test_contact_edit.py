
from model.contact import Contact


def test_contact_edit(app):
    app.contact.open_create_contact_page()
    app.contact.edit_contact(Contact(user_firstname="alena_new_1"))

