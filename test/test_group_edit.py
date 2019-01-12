
from model.group import Group


def test_group_edit(app):
    app.group.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.edit_first_group(Group(name="new_edit", header="kek", footer=""))
    app.group.return_to_group_page()
    app.session.logout()
