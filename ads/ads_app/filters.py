"""Фильтры приложения ads_app"""

import django_filters

from ads_app.models import Ad, ExchangeProposal


class AdFilter(django_filters.FilterSet):
    """Фильтрация списка товаров"""

    class Meta:

        model = Ad
        fields = {
            "title": ["icontains"],
            "description": ["icontains"],
            "category": ["iexact"],
            "condition": ["exact"],
        }


class ExchangeProposalFilter(django_filters.FilterSet):
    """Фильтрация списка предложений"""

    class Meta:

        model = ExchangeProposal
        fields = ("ad_sender__user", "ad_receiver__user", "status")

    @property
    def qs(self):
        exchange_proposal = super().qs
        user = getattr(self.request, "user", None)

        return exchange_proposal.filter(
            ad_sender__user=user
        ) | exchange_proposal.filter(ad_receiver__user=user)
