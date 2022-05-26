from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
# Create your views here.

class SignupView(CreateView):
    
    form_class=CustomUserCreationForm
    
    template_name='signup.html'
    
    success_url = reverse_lazy('acounts:signup_success')
    
    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)

class SignupSuccessView(TemplateView):
    template_name = 'signup_success.html'