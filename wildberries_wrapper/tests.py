import mock 
# Применим мокироваие для запросов requests.get() и requests.patch(), 
# чтобы избежать реальных обращений к внешним ресурсам.

from django.test import TestCase
from wildberries_wrapper.api_wrapper import WildberriesAPIWrapper

import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = 'FAKE-TOKEN-FOR-TESTING' # Мокируем реальный токен фейковым 'FAKE-TOKEN-FOR-TESTING'
BASE_URL='https://content-api.wildberries.ru/content/v2'

class WildberriesAPITest(TestCase):
    """
    Тесты для класса WildberriesAPIWrapper.
    """

    def setUp(self):
        """
        Подготовка среды для тестирования.
        """
        self.base_url = BASE_URL
        self.token = TOKEN
        self.api_wrapper = WildberriesAPIWrapper(base_url=self.base_url, token=self.token)
        
        
    @mock.patch.object(requests, 'get')
    def test_get_prds(self, mock_get):
        """
        Тест метода get_prds.
        """
        # Подготавливаем ответ на моковские запросы
        mock_response = mock.Mock()
        mock_response.json.return_value = {"result": ["product1", "product2"]}
        mock_get.return_value = mock_response
        
        # Выполнение метода
        result = self.api_wrapper.get_prds()
        
        # Проверка, что метод сделал запрос с нужными параметрами
        mock_get.assert_called_once_with(
            f"{self.base_url}/supplier/stocks",
            headers={"Authorization": f"Bearer {self.token}"},
            params={}  # Добавляем пустой словарь параметров
        )
        
        # Проверка, что возвращается корректный результат
        self.assertEqual(result["result"], ["product1", "product2"])

    @mock.patch.object(requests, 'get')
    def test_get_prd(self, mock_get):
        """Тест метода get_prd."""
        product_id = 12345
        mock_response = mock.Mock()
        mock_response.json.return_value = {"product": "product"}
        mock_get.return_value = mock_response
        
        # Выполнение метода
        result = self.api_wrapper.get_prd(product_id)
        
        # Проверка, что метод сделал запрос с нужным продуктом
        mock_get.assert_called_once_with(
            f"{self.base_url}/supplier/cards?nmIds={product_id}",
            headers={"Authorization": f"Bearer {self.token}"}
        )
        
        # Проверка, что возвращается корректный результат
        self.assertEqual(result["product"], "product")

    @mock.patch.object(requests, 'patch')
    def test_set_prd(self, mock_patch):
        """Тест метода set_prd."""
        product_id = 12345
        update_data = {"price": 999}
        mock_response = mock.Mock()
        mock_response.json.return_value = {"message": "updated"}
        mock_patch.return_value = mock_response
        
        # Выполнение метода
        result = self.api_wrapper.set_prd(product_id, update_data)
        
        # Проверка, что метод отправил patch-запрос с нужными данными
        mock_patch.assert_called_once_with(
            f"{self.base_url}/supplier/cards/{product_id}",
            json=update_data,
            headers={
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json"
            }
        )
        
        # Проверка, что возвращается корректный результат
        self.assertEqual(result["message"], "updated")

    @mock.patch.object(requests, 'get')
    def test_get_orders(self, mock_get):
        """
        Тест метода get_orders.
        """
        mock_response = mock.Mock()
        mock_response.json.return_value = {"orders": ["order1", "order2"]}
        mock_get.return_value = mock_response
        
        # Выполнение метода
        result = self.api_wrapper.get_orders()
        
        # Проверка, что метод сделал запрос на получение заказов
        mock_get.assert_called_once_with(
            f"{self.base_url}/supplier/orders",
            headers={"Authorization": f"Bearer {self.token}"},
            params={}  # Добавляем пустой словарь параметров
        )
        
        # Проверка, что возвращается корректный результат
        self.assertEqual(result["orders"], ["order1", "order2"])

    @mock.patch.object(requests, 'get')
    def test_get_commission(self, mock_get):
        """
        Тест метода get_commission.
        """
        start_date = "2023-01-01"
        end_date = "2023-01-31"
        mock_response = mock.Mock()
        mock_response.json.return_value = {"commission": 1000}
        mock_get.return_value = mock_response
        
        # Выполнение метода
        result = self.api_wrapper.get_commission(start_date, end_date)
        
        # Проверка, что метод сделал запрос на получение комиссии
        mock_get.assert_called_once_with(
            f"{self.base_url}/upplier/revenue?dateFrom={start_date}&dateTo={end_date}",
            headers={"Authorization": f"Bearer {self.token}"}
        )
        
        # Проверка, что возвращается корректный результат
        self.assertEqual(result["commission"], 1000)
