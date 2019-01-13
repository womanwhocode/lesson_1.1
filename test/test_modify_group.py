
from model.group import Group


def test_modify_group_name(app):
    app.group.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.modify_first_group(Group(name="new name"))
    app.session.logout()


def test_modify_group_header(app):
    app.group.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.modify_first_group(Group(header="the newest header"))
    app.session.logout()
