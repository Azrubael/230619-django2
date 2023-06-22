from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator
from django.http import Http404

def post_list(request):
    """Представление post_list принимает объект request в качестве единственного параметра."""
    posts_list = Post.published.all()
    # Постраничная разбивка с тремя постами на одной странице
    paginator = Paginator(posts_list, 3)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})


def post_detail_try(request, id):
    """Представление детальной информации о посте."""
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404("No Post Found.")
    
    return render(request,
        'blog/post/detail.html',
        {'post': post})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day)
    return render(request,
        'blog/post/detail.html',
        {'post': post})