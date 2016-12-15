from ubidots import ApiClient

api = ApiClient(token='VaECzrPu75Kx0JvRaIF042z5gexlcI')
my_variable = api.get_variable('5848c8d37625422d640ad3c0')
new_value = my_variable.save_value({'value': 25})

