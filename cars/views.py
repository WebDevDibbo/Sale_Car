from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.utils.decorators import method_decorator 
from django.contrib.auth.decorators import login_required  
from django.urls import reverse_lazy
from . import models
from . import forms
# Create your views here.

@method_decorator(login_required, name='dispatch')
class AddPostCreateView(CreateView):
    model = models.PostCar
    form_class = forms.CarPostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('add_post')

    def form_valid(self,form):
        return super().form_valid(form)
    
@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    model = models.PostCar
    form_class = forms.CarPostForm
    template_name = 'add_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('add_post')

@method_decorator(login_required, name='dispatch')
class DeletePost(DeleteView):
    model = models.PostCar
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'


class DetailPost(DetailView):
    model = models.PostCar
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'
    context_object_name = 'car' 

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data = self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        print(context)
        return context