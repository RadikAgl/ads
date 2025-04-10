from django.test import TestCase

from ads_app.services import relative_url


class ServicesTest(TestCase):
    """Класс для тестирования сервисов"""

    def test_relative_url_without_page_parameter(self) -> None:
        """Тест метода получения относительного url с параметрами"""
        url = "/ads?param1=1&param2=2"
        res, are_params = relative_url(url)
        self.assertTrue(are_params)
        self.assertEqual(res, "/ads?param1=1&param2=2")

    def test_relative_url_with_page_parameter(self) -> None:
        """Тест метода получения относительного url с параметрами"""
        url = "/ads?page=1&param1=1&param2=2"
        res, are_params = relative_url(url)
        self.assertTrue(are_params)
        self.assertEqual(res, "/ads?param1=1&param2=2")

    def test_relative_url_without_parameters(self) -> None:
        """Тест метода получения относительного url с параметрами"""
        url = "/ads"
        res, are_params = relative_url(url)
        self.assertFalse(are_params)
        self.assertEqual(res, "/ads")
