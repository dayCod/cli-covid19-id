from api import *

api = indonesia_api.json()
ina_api = api[0]
print(ina_api["name"])