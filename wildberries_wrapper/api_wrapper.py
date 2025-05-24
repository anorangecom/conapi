import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('WB_API_TOKEN')
BASE_URL='https://content-api.wildberries.ru'

class WildberriesAPIWrapper:
    def __init__(self, base_url=BASE_URL, token=TOKEN):
        self.token = token 
        self.base_url = base_url
    

    def check_creds(self):
        """
        Метод проверяет возможность взаимодействия с API Wildberries с использованием переданного токена
        """
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.get(f'https://content-api.wildberries.ru/ping', headers=headers)
        return response.json()


    def get_prds(self, filter=None):
        """
        Метод запрашивает список товаров продавца на платформе Wildberries
        """
        params = {}
        if filter is not None:
            params.update(filter)
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.get(f'{self.base_url}/content/v2/object/parent/all', headers=headers, params=params)
        return response.json()
    

    def get_prd(self, prd_id):
        """
        Получение полной информации о товаре по id
        """
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.get(f'{self.base_url}/content/v2/supplier/cards?nmIds={prd_id}', headers=headers)
        return response.json()
    
    
    def set_prd(self, prd_id, data):
        """
        Изменение атрибута товара
        """
        headers = {'Authorization': f'Bearer {self.token}', 'Content-Type': 'application/json'}
        response = requests.patch(f'{self.base_url}/content/v2/supplier/cards/{prd_id}', json=data, headers=headers) # с демо токеном (работает только GET) работать не будет 
        return response.json()
    

    def get_categories(self, filter=None):
        """
        Получение списка категорий
        """
        # params = {}
        # if filter is not None:
        #     params.update(filter)
        # headers = {'Authorization': f'Bearer {self.token}'}
        # response = requests.get(f'{self.base_url}/content/v2/categories/', headers=headers, params=params)
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
        response = requests.get(f'{self.base_url}/content/v2/supplier/orders', headers=headers, params=params)
        return response.json()
    
    
    def get_commission(self, date_from, date_to):
        """
        Получение комисси за товар
        """
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.get(f'{self.base_url}/content/v2/upplier/revenue?dateFrom={date_from}&dateTo={date_to}', headers=headers)
        return response.json()