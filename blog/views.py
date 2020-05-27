from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm
from taggit.models import Tag

# Create your views here.


def post_list(request, tag_slug=None):
    if tag_slug:
        tag = Tag.objects.filter(slug=tag_slug).first()
        posts_list = Post.objects.filter(tags__in=[tag])
    else:
        posts_list = Post.objects.all()
    # 上一頁與下一頁
    # https://docs.djangoproject.com/en/3.0/topics/pagination/
    # 下面為更進階的用法
    # https://ivanjo39191.pixnet.net/blog/post/192870713-python-django-%E5%AD%B8%E7%BF%92%E7%B4%80%E9%8C%84%EF%BC%9A%E6%9E%B6%E8%A8%AD%E5%80%8B%E4%BA%BA%E9%83%A8%E8%90%BD%E6%A0%BC%28%E4%BA%8C%29-%EF%BC%8C
    paginator = Paginator(posts_list, 3)
    tag_list = Tag.objects.all()
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)  # 第一次一定是沒有數值
    except PageNotAnInteger:  # 如果返回
        posts = paginator.page(1)
    except EmptyPage:  # 如果超過最大頁數
        # paginator.unm_pages = 最後一頁
        posts = paginator.page(paginator.unm_pages)
    return render(request, 'blog/post/list.html', locals())


def post_detail(request, year, month, day, slug):
    post = Post.objects.filter(
        publish__year=year,
        publish__month=month,
        publish__day=day,
        slug=slug
    ).first()

    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm

    return render(request, 'blog/post/detail.html', locals())
