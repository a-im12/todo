from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import TodoPostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class IndexViews(TemplateView):
    template_name = 'mypage.html'

@method_decorator(login_required, name='dispatch')
class CreatePostView(CreateView):
    form_class = TodoPostForm
    
    template_name = 'post_todo.html'
    
    success_url = reverse_lazy('todo:post_done')
    
    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        
        postdata.save()
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    template_name = 'post_success.html'