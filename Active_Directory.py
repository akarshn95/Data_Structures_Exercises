
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


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    users=group.get_users()
    if user in users:
        return True
    
    is_user=False
    groups=group.get_groups()
    for each_group in groups:
        is_user=is_user_in_group(user,each_group)
        if is_user:
            break
    return is_user


# TEST CASES 

#TEST CASE 1
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group("sub_child_user",parent)) #returns True
print(is_user_in_group("sub_child",sub_child))    #returns False

#TEST CASE 2
new_group=Group("Empty")

print(is_user_in_group("user",new_group))    #returns False

#TEST CASE 3
a = Group("A")
b = Group("B")
c = Group("C")
d = Group("D")
e = Group("E")
f = Group("F")
g = Group("G")
h = Group("H")
i = Group("I")

a.add_group(b)
a.add_group(c)
b.add_group(d)
b.add_group(e)
c.add_group(f)
f.add_group(g)
f.add_group(h)
f.add_group(i)

b.add_user('bo')
d.add_user('do')
h.add_user('ho')
i.add_user('io')

print(is_user_in_group('bo',b))    #returns True
print(is_user_in_group('do',b))   #returns True
print(is_user_in_group('ho',c) )    #returns True
print(is_user_in_group('do', c))   #returns False
print(is_user_in_group('io',h))    #returns False

