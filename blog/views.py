from django.shortcuts import render

# Create your views here.

#20191001追加
def post_list(request):
    return render(request, 'blog/post_list.html', {})