from index import Base

base = Base('hktwlab', 'cx')

print(base.url())
result = base.login()
print(result)
