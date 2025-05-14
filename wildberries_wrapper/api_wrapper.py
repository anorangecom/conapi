import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('WB_API_TOKEN')
# BASE_URL='https://content-api.wildberries.ru/content/v1' нужно проверить
BASE_URL='https://content-api.wildberries.ru/content/v2'

class WildberriesAPIWrapper:
    def __init__(self, base_url=BASE_URL, token=TOKEN):
        self.token = token 
        self.base_url = base_url
    

    def check_creds(self):
        """
        Метод проверяет возможность взаимодействия с API Wildberries с использованием переданного токена
        """
        # headers = {'Authorization': f'Bearer {self.token}'}
        # response = requests.get(f'{self.url}/auth/check', headers=headers) # /auth/check здесь и далее проверить на реальный эндпоинт
        # return response.status_code
        pass # У API Wildberries нет эндпоинта для проверки доступности токена - 
            # можно попробовать сделать простой запрос, например, на получение товаров пока pass.


    def get_prds(self, filter=None):
        """
        Метод запрашивает список товаров продавца на платформе Wildberries
        """
        params = {}
        if filter is not None:
            params.update(filter)
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.get(f'{self.base_url}/supplier/stocks', headers=headers, params=params)
        return response.json()
    

    def get_prd(self, prd_id):
        """
        Получение полной информации о товаре по id
        """
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.get(f'{self.base_url}/supplier/cards?nmIds={prd_id}', headers=headers)
        return response.json()
    
    
    def set_prd(self, prd_id, data):
        """
        Изменение атрибута товара
        """
        headers = {'Authorization': f'Bearer {self.token}', 'Content-Type': 'application/json'}
        response = requests.patch(f'{self.base_url}/supplier/cards/{prd_id}', json=data, headers=headers) # с демо токеном (работает только GET) работать не будет 
        return response.json()
    

    def get_categories(self, filter=None):
        """
        Получение списка категорий
        """
        # params = {}
        # if filter is not None:
        #     params.update(filter)
        # headers = {'Authorization': f'Bearer {self.token}'}
        # response = requests.get(f'{self.base_url}/categories/', headers=headers, params=params)
        # return response.json()
        pass # логика метода рабочая но такого эндпоинта у WB нет поэтому заглушка
    
    
    def get_orders(self, filter=None):
        """
        Получение списка заказов
        """
        params = {}
        if filter is not None:
            params.update(filter)
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.get(f'{self.base_url}/supplier/orders', headers=headers, params=params)
        return response.json()
    
    
    def get_commission(self, date_from, date_to):
        """
        Получение комисси за товар
        """
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.get(f'{self.base_url}/upplier/revenue?dateFrom={date_from}&dateTo={date_to}', headers=headers)
        return response.json()