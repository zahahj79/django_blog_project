from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Post
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.models import User
from .forms import NewPostForm
from django.views import generic


class PostListView(generic.ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_modified')


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostCreateView(generic.CreateView):
    form_class = NewPostForm
    template_name = 'blog/post_create.html'


class PostUpdateView(generic.UpdateView):
    form_class = NewPostForm
    template_name = 'blog/post_create.html'
    model = Post


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')




# def post_list_view(request):
#     post_list = Post.objects.filter(status='pub').order_by('-datetime_modified')
#     return render(request, 'blog/post_list.html', {'post_list': post_list})

#
# def post_detail_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})


# def post_create_view(request):
#     if request.method == 'POST':
#         sent_form = NewPostForm(request.POST)
#         if sent_form.is_valid():
#             sent_form.save()
#             return redirect('post_list')
#
#     else:   # Get Request
#         form = NewPostForm()
#
#     return render(request, 'blog/post_create.html', {'form': form})

    # if request.method=='POST':
    #     post_title=request.POST.get('title')
    #     post_text=request.POST.get('text')
    #
    #     user=User.objects.all()[0]
    #     Post.objects.create(title=post_title,text=post_text,author=user,status='pub')
    #
    # return render(request,'blog/post_create.html')


# def post_update_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = NewPostForm(request.POST or None, instance=post)
#
#     if form.is_valid():
#         form.save()
#         return redirect('post_list')
#
#     return render(request, 'blog/post_create.html', {'form': form})


# def post_delete_view(request, pk):
#     post=get_object_or_404(Post,pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('post_list')
#     return render(request, 'blog/post_delete.html', {'post': post})
