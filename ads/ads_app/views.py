from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

from ads_app.filters import AdFilter, ExchangeProposalFilter
from ads_app.models import Ad, ExchangeProposal
from ads_app.services import get_full_path_of_request_without_param_page, have_user_ads


class AdListView(FilterView):
    """Представление для отображения списка всех товаров"""

    template_name = "ads_list.html"
    model = Ad
    filterset_class = AdFilter
    context_object_name = "ads"
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        relative_url = get_full_path_of_request_without_param_page(self.request)
        context["is_params"] = relative_url[1]
        context["cur_url"] = relative_url[0]
        context["have_user_ads"] = have_user_ads(self.request)
        return context


class AdCreateView(LoginRequiredMixin, CreateView):
    template_name = "create.html"
    model = Ad
    fields = ["title", "description", "category", "condition", "image"]
    success_url = "/ads/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AdUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "ad_update.html"
    model = Ad
    fields = ["title", "description", "category", "condition", "image"]
    success_url = "/ads/"


class AdDeleteView(DeleteView):
    model = Ad
    context_object_name = "ad"
    success_url = reverse_lazy("ads_app:ads-list")
    template_name = "ad_confirm_delete.html"


class ExchangeProposalCreateView(LoginRequiredMixin, CreateView):
    template_name = "exchange_proposal_create.html"
    model = ExchangeProposal
    fields = ["ad_sender", "ad_receiver", "comment"]
    success_url = "/ads/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"].fields["ad_sender"].queryset = Ad.objects.filter(
            user=self.request.user
        )
        context["form"].fields["ad_receiver"].queryset = Ad.objects.exclude(
            user=self.request.user
        )
        return context

    def form_valid(self, form):
        form.instance.status = "w"
        return super().form_valid(form)


class ExchangeProposalListView(LoginRequiredMixin, FilterView):
    """Представление для отображения списка всех предложений пользователя"""

    template_name = "expr_list.html"
    model = ExchangeProposal
    filterset_class = ExchangeProposalFilter
    context_object_name = "exproposals"
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        relative_url = get_full_path_of_request_without_param_page(self.request)
        context["is_params"] = relative_url[1]
        context["cur_url"] = relative_url[0]
        context["have_user_ads"] = have_user_ads(self.request)
        return context

    def form_valid(self, form):
        status = form.instance.status
        ep_id = form.instance.ep_id
        ep = ExchangeProposal.objects.get(id=int(ep_id))
        if status == "accept":
            ep.status = "принято"
        elif status == "reject":
            ep.status = "отклонено"
        ep.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        status = request.POST.get("status")
        ep_id = request.POST.get("ep_id")

        ep = ExchangeProposal.objects.get(id=int(ep_id))
        if status == "accept":
            ep.status = "a"
        elif status == "reject":
            ep.status = "r"
        ep.save()
        return HttpResponseRedirect(reverse("ads_app:ads-exprs"))
