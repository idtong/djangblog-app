from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Post


# Create your views here.
# def post_list(request):
#     name = "이경훈"
#     return HttpResponse('''<h1>Hello!! {myname}</h1>'''.format(myname=name));

def post_list(request):
    name = "이경훈11"

    #쿼리 셋을 사용하여 글목록 가져오기
    posts = Post.objects.filter(create_at__lte=timezone.now()).order_by('create_at')

    return render(request, 'blog/post_list.html',{'posts':posts});
