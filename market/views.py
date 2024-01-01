from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.contrib.auth.views import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Products


class ProductHome(ListView):
    model = Products
    template_name = 'market/home.html'
    context_object_name = 'products'

class ProductDetail(DetailView):
    model = Products
    template_name = 'market/detail.html'

class CreateProduct(LoginRequiredMixin,CreateView):
    model = Products
    template_name = 'market/add_product.html'
    fields = ['product_image', 'title','price', 'product_info']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_authenticated


class ProductUpdate(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Products
    template_name = 'market/update.html'
    fields = ['product_image', 'title','price', 'product_info']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        else:
            return False


class DeleteProudct(DeleteView):
    model = Products
    success_url = reverse_lazy('home-page')
    template_name = 'market/delete.html'


def search_product(request):
    query = request.GET.get('q')
    if query:
        results = Products.objects.filter(title__icontains=query)
    else:
        results = []

    return render(request, 'base.html', {'results': results, 'query': query})
