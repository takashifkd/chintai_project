from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import PropertyCreateForm
from django.urls import reverse_lazy

from .models import RentalProperty


class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = "dashboard_index.html"


# def index(request):
#    return render(request, "dashboard_index.html")

# 物件リスト取得


class PropertyListView(LoginRequiredMixin, generic.ListView):
    model = RentalProperty
    template_name = "property_list.html"
    paginate_by = 10

    def get_queryset(self):
        property_list = RentalProperty.objects.filter(
            user=self.request.user).order_by('-created_at')
        return property_list

# 物件詳細取得


class PropertyDetailView(LoginRequiredMixin, generic.DetailView):
    model = RentalProperty
    template_name = "property_detail.html"
    # pk_url_kwarg = "id"

# 物件情報新規作成


class PropertyCreateView(LoginRequiredMixin, generic.CreateView):
    model = RentalProperty
    template_name = "property_create.html"
    form_class = PropertyCreateForm
    success_url = reverse_lazy("dashboard:list")

    def form_valid(self, form):
        property = form.save(commit=False)
        property.user = self.request.user
        property.save()
        messages.success(self.request, "物件情報を作成しました。")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self, request, "物件情報の作成に失敗しました。")
        return super().form_invalid(form)

# 物件情報更新
class PropertyUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = RentalProperty
    template_name = "property_update.html"
    form_class = PropertyCreateForm

    def get_success_url(self):
        return reverse_lazy("dashboard:detail", kwargs={'pk':self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, "物件情報を更新しました。")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "物件情報の更新に失敗しました。")
        return super().form_invalid(form)

# 物件情報削除
class PropertyDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = RentalProperty
    template_name = "property_delete.html"
    success_url = reverse_lazy("dashboard:list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "物件情報を削除しました。")
        return super().delete(request, *args, **kwargs)
