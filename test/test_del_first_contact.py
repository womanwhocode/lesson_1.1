

def test_delete_first_contact(app):
    app.contact.open_group_page()
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()
