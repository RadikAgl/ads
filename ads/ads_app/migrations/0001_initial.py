# Generated by Django 4.2.20 on 2025-04-08 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Ad",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=100, verbose_name="название товара"),
                ),
                ("description", models.TextField(verbose_name="описание товара")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="images/%Y/%m/%d/",
                        verbose_name="изображение",
                    ),
                ),
                (
                    "category",
                    models.CharField(max_length=100, verbose_name="название товара"),
                ),
                (
                    "condition",
                    models.CharField(
                        choices=[("n", "новый"), ("d", "уцененный"), ("u", "б/у")],
                        max_length=50,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="время создания товара"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "товар",
                "verbose_name_plural": "товары",
                "ordering": ("-created_at",),
            },
        ),
        migrations.CreateModel(
            name="ExchangeProposal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("comment", models.TextField(verbose_name="комментарий")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("w", "ожидает"),
                            ("a", "принято"),
                            ("r", "отклонено"),
                        ],
                        max_length=50,
                        verbose_name="статус предложения",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        verbose_name="время создания предложения обмена",
                    ),
                ),
                (
                    "ad_receiver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ad_receivers",
                        to="ads_app.ad",
                        verbose_name="ожидаемый товар",
                    ),
                ),
                (
                    "ad_sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ad_senders",
                        to="ads_app.ad",
                        verbose_name="предлагаемый товар",
                    ),
                ),
            ],
            options={
                "verbose_name": "предложение обмена",
                "verbose_name_plural": "предложения обмена",
                "ordering": ("-created_at",),
            },
        ),
    ]
