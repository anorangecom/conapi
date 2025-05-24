# from django.shortcuts import render

# Create your views here.

# Импортируйте его во views.py для применения
from api_wrapper import WildberriesAPIWrapper

# Пример создания экземпляра и вызова методов
api = WildberriesAPIWrapper()

# Проверка работоспособности токена
# is_valid = api.check_creds()
# print(is_valid)

# # Получение списка товаров
products = api.get_prds()
# for product in products:
print(products)

# # Получение деталей товара
# product_details = api.get_prd('NM_ID')
# print(product_details)

# # Получение заказа
# orders = api.get_orders({'take': 1})
# print(orders)

# Получение комиссии за определенный период
# commission = api.get_commission('2023-01-01', '2023-01-31')
# print(commission)