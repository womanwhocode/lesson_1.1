
from model.group import Group


def test_modify_group_name(app):
    app.group.open_home_page()
    app.group.open_groups_page()
    app.group.modify_first_group(Group(name="new name"))


# comment
def test_modify_group_header(app):
    app.group.open_home_page()
    app.group.open_groups_page()
    app.group.modify_first_group(Group(header="the newest header"))
