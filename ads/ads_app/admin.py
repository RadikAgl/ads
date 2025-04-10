from django.contrib import admin

from ads_app.models import Ad


class AdAdmin(admin.ModelAdmin):
    """Класс с настройками модели товаров при отображении на админ панели"""

    list_display = [
        "user",
        "title",
        "description",
        "category",
        "image",
        "condition",
        "created_at",
    ]


admin.site.register(Ad, AdAdmin)
