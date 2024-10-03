import re

m=re.match('^([a-zA-Z]|[0-9]|[_])*$', 'ab_@d120ef')
print(m)
if m:
    print('illeszkedik')
else:
    print('NEM illeszkedik')