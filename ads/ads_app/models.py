"""Модели приложения ads_app"""

from django.contrib.auth.models import User
from django.db import models


class Ad(models.Model):
    """Модель товаров"""

    CHOICES = (
        ("n", "новый"),
        ("d", "уцененный"),
        ("u", "б/у"),
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="пользователь"
    )
    title = models.CharField(max_length=100, verbose_name="название товара")
    description = models.TextField(verbose_name="описание товара")
    image = models.ImageField(
        upload_to="images/%Y/%m/%d/", null=True, blank=True, verbose_name="изображение"
    )
    category = models.CharField(max_length=100, verbose_name="категория товара")
    condition = models.CharField(
        max_length=50, choices=CHOICES, verbose_name="состояние товара"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name="время создания товара"
    )

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
        ordering = ("-created_at",)

    def __str__(self):
        return self.title


class ExchangeProposal(models.Model):
    """Модель обменов"""

    CHOICES = (
        ("w", "ожидает"),
        ("a", "принято"),
        ("r", "отклонено"),
    )

    ad_sender = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE,
        related_name="ad_senders",
        verbose_name="предлагаемый товар",
    )
    ad_receiver = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE,
        related_name="ad_receivers",
        verbose_name="ожидаемый товар",
    )
    comment = models.TextField(verbose_name="комментарий")
    status = models.CharField(
        max_length=50, choices=CHOICES, verbose_name="статус предложения"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name="время создания предложения обмена",
    )

    class Meta:
        verbose_name = "предложение обмена"
        verbose_name_plural = "предложения обмена"
        ordering = ("-created_at",)

    def __str__(self):
        return f"Обмен {self.ad_sender} на {self.ad_receiver}"
