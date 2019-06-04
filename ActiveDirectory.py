class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
child_user = "child_user"
parent.add_user(child_user)

def is_user_in_group(user, group, testedGroups = []):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if group.get_name() in testedGroups:
        return False
    else:
        testedGroups.append(group.get_name())
    
    directUsers = group.get_users()

    for aUser in directUsers:
        if aUser == user:
            return True
    
    groups = group.get_groups()

    for aGroup in groups:
        if is_user_in_group(user, aGroup, list(testedGroups)):
            return True
        else:
            testedGroups.append(aGroup.get_name)

            

    return False

print(is_user_in_group(sub_child_user, parent)) #True
print(is_user_in_group(sub_child_user, sub_child)) #True
print(is_user_in_group(child_user, sub_child)) #False

sub_child.add_group(parent)

print(is_user_in_group('not a user', sub_child)) #False should also not do an infinite loop