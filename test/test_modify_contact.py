from model.contact import Contact

def test_modify_contact_name(app):
    old_contacts = app.contact.get_contact_list()
