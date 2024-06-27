import public_and_private_classes
from public_and_private_classes import NotPrivate

test = public_and_private_classes.NotPrivate('name')
test2 = NotPrivate('name2')
test.display()