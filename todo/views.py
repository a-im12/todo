from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import TodoPostForm
from .models import TodoPost
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class MypageViews(ListView):
    template_name = 'mypage.html'
    
    # paginate_by = 9
    
    def get_queryset(self):
        
        queryset = TodoPost.objects.filter(
            user = self.request.user).order_by('-posted_at')
        
        return queryset

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