from ubidots import ApiClient
import random
import time

api = ApiClient(token='VaECzrPu75Kx0JvRaIF042z5gexlcI')
my_variable = api.get_variable('5848c8d37625422d640ad3c0')

dato = 100

while True:
    dato = random.randrange(48, 80)
    print(dato)
    new_value = my_variable.save_value({'value': dato})
    time.sleep(2)