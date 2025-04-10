from typing import Tuple

from django.http import HttpRequest

from ads_app.models import Ad


def get_full_path_of_request_without_param_page(
    request: HttpRequest,
) -> Tuple[str, bool]:
    """Возвращает полый url запроса"""
    url = request.get_full_path()
    return relative_url(url)


def relative_url(url: str) -> Tuple[str, bool]:
    """Создание url для отображения страниц пагинации с фильтрацией"""
    if "?" not in url:
        return url, False
    if "page" not in url:
        return url, True
    params = url.split("?")[1].split("&")
    params = [param for param in params if not param.startswith("page")]
    return url.split("?")[0] + "?" + "&".join(params), True


def have_user_ads(request: HttpRequest):
    """Проверка наличия товаров для обмена у пользователя"""
    if request.user.is_authenticated:
        user = request.user
        q = Ad.objects.filter(user=user)
        if q:
            return True
