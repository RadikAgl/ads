from django.urls import path

from .views import (
    AdListView,
    AdCreateView,
    AdUpdateView,
    AdDeleteView,
    ExchangeProposalCreateView,
    ExchangeProposalListView,
)

urlpatterns = [
    path("", AdListView.as_view(), name="ads-list"),
    path("add/", AdCreateView.as_view(), name="ads-create"),
    path("update/<int:pk>", AdUpdateView.as_view(), name="ads-update"),
    path("delete/<int:pk>/", AdDeleteView.as_view(), name="ads-delete"),
    path("add_ex_pr/", ExchangeProposalCreateView.as_view(), name="ads-expr-create"),
    path("exchange_proposals/", ExchangeProposalListView.as_view(), name="ads-exprs"),
]
