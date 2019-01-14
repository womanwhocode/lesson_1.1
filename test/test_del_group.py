
def test_delete_first_group(app):
    app.group.open_home_page()
    app.group.open_groups_page()
    app.group.delete_first_group()
    app.session.logout()
