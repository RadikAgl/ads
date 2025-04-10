"""Теыты представлений приложения ads_app"""

from django.test import TestCase
from django.urls import reverse


class AdListViewTest(TestCase):
    """
    Класс тестирования представления списка товаров
    """

    fixtures = [
        "01_users.json",
        "02_ads.json",
    ]

    def test_ads_list_view(self) -> None:
        """Тестирование представления списка товаров."""
        response = self.client.get(reverse("ads_app:ads-list"))
        response_with_url_params = self.client.get(
            f"{reverse('ads_app:ads-list')}?condition=d"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_with_url_params.status_code, 200)

        if response.context is not None:
            self.assertTrue("is_params" in response.context)
            self.assertTrue("cur_url" in response.context)
            self.assertTrue("have_user_ads" in response.context)
            self.assertEqual(len(response.context["ads"]), 3)

        if response_with_url_params.context:
            self.assertEqual(len(response_with_url_params.context["ads"]), 1)
