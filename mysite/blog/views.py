from django.shortcuts import render, get_object_or_404 #, redirect
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.views.generic import ListView
from django.http import Http404
from .forms import EmailPostForm, CommentForm
from django.views.decorators.http import require_POST


class PostListView(ListView):
    """Альтернативное представление списка постов"""
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/listView.html'


def post_list(request):
    """Представление post_list принимает объект request в качестве единственного параметра."""
    posts_list = Post.published.all()
    # Постраничная разбивка с тремя постами на одной странице
    paginator = Paginator(posts_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # Если page_number не целое число, то
        # выдать первую страницу
        posts = paginator.page(1)
    except EmptyPage:
        # Если page_number находится вне диапазоне, то
        # выдать последнюю страницу
        posts = paginator.page(paginator.num_pages)
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
    # список активных комментариев к эьлму посту
    comments = post.comments.filter(active=True)
    # Форма для комментирования пользователями
    form = CommentForm()
    return render(request,
        'blog/post/detail.html',
        {'post': post,
         'comments': comments,
         'form': form})


def post_share(request, post_id):
    """Генерирование формы электронного письма"""
    # Извлечь пост по id
    post = get_object_or_404(Post,
            id=post_id,
            status=Post.Status.PUBLISHED)
    sent = False
    if request.method == 'POST':
        # Фотма была передана на обработку
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Поля формы успешно прошли валидацию
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n"\
                    f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, cd['email'], [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html',\
            {'post': post, 'form': form, 'sent': sent})


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    # Комментарий был отправлен
    form = CommentForm(data=request.POST)
    if form.is_valid():
        # Создать объект класса Comment, не сохраняя его в БД
        comment = form.save(commit=False)
        # назначить пост комментарию
        comment.post = post
        # Сохранить пост в БД
        comment.save()
    return render(request, 'blog/post/comment.html',
            {'post': post, 'form': form, 'comment': comment})
