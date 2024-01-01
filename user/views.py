from audioop import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView, UpdateView

from market.models import Products
from .forms import RegistUserForm, ProfileUpdateForm, UserUpdateForm


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'user/login.html'
    next_page = '/'

class Logout(LogoutView):
    next_page = 'login-page'


class RegisterUser(CreateView):
    form_class = RegistUserForm
    template_name = 'user/signup.html'
    success_url = reverse_lazy('login-page')

class ProfileUser(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'user/profile.html'

from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Customer, CustomerForm


class ProfileUser(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'user/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        customer = Customer.objects.get_or_create(user=user)[0]
        context['user'] = user
        context['customer'] = customer
        return context



class EditProfileView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        form = CustomerForm(instance=customer)
        return render(request, 'user/update-profile.html', {'form': form})

    def post(self, request):
        customer = Customer.objects.get(user=request.user)
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Замените 'profile' на ваш URL для отображения профиля
        return render(request, 'user/update-profile.html', {'form': form})


def my_products(request):
    form = Products.objects.filter(author=request.user)
    return render(request, 'user/my_products.html', {'form':form})

