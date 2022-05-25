from django.shortcuts import render
from django.views.generic import TemplateView

class IndexViews(TemplateView):
    template_name = 'mypage.html'
