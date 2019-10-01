from django.shortcuts import render
from django.utils import timezone #20191001追加
from .models import Post #20191001追加

# Create your views here.

#20191001追加
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    