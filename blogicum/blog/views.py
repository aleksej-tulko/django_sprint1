<<<<<<< HEAD
from typing import Union

from django.shortcuts import render
from django.http import Http404

posts: list[dict[str, Union[str, int]]] = [
    {
        'id': 0,
        'location': 'Остров отчаянья',
        'date': '30 сентября 1659 года',
        'category': 'travel',
        'text': '''Наш корабль, застигнутый в открытом море
                страшным штормом, потерпел крушение.
                Весь экипаж, кроме меня, утонул; я же,
                несчастный Робинзон Крузо, был выброшен
                полумёртвым на берег этого проклятого острова,
                который назвал островом Отчаяния.''',
    },
    {
        'id': 1,
        'location': 'Остров отчаянья',
        'date': '1 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Проснувшись поутру, я увидел, что наш корабль сняло
                с мели приливом и пригнало гораздо ближе к берегу.
                Это подало мне надежду, что, когда ветер стихнет,
                мне удастся добраться до корабля и запастись едой и
                другими необходимыми вещами. Я немного приободрился,
                хотя печаль о погибших товарищах не покидала меня.
                Мне всё думалось, что, останься мы на корабле, мы
                непременно спаслись бы. Теперь из его обломков мы могли бы
                построить баркас, на котором и выбрались бы из этого
                гиблого места.''',
    },
    {
        'id': 2,
        'location': 'Остров отчаянья',
        'date': '25 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Всю ночь и весь день шёл дождь и дул сильный
                порывистый ветер. 25 октября.  Корабль за ночь разбило
                в щепки; на том месте, где он стоял, торчат какие-то
                жалкие обломки,  да и те видны только во время отлива.
                Весь этот день я хлопотал  около вещей: укрывал и
                укутывал их, чтобы не испортились от дождя.''',
    },
]
posts_dict = {post['id']: post for post in posts}


def index(request):
    return render(
        request, 'blog/index.html',
        context={'list_of_blogs': reversed(posts)}
    )


def post_detail(request, post_id):
    if post_id not in posts_dict:
        raise Http404("Страница не найдена")
    return render(
        request, 'blog/detail.html',
        context={'post': posts_dict[post_id]}
    )


def category_posts(request, category_slug):
    return render(
        request, 'blog/category.html',
        context={'category': category_slug}
    )
=======
from django.shortcuts import get_object_or_404, render

from .models import Post, Category


def index(request):
    posts = Post.objects.select_related(
        'location', 'author', 'category').filter(
        pub_date__lte=now(),
        is_published=True,
        category__is_published=True
    )
    return render(request, 'blog/index.html', {'post_list': posts})


def post_detail(request, id):
    posts = get_object_or_404(
        Post.objects.select_related('location', 'author', 'category').filter(
            pub_date__lte=now(),
            is_published=True,
            category__is_published=True
        ), id=id)
    return render(request, 'blog/detail.html', {'post': posts})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category.objects.filter(
            slug=category_slug,
            is_published=True
        )
    )
    post_list = Post.objects.filter(
        pub_date__lte=now()
    )
    return render(request, 'blog/category.html',
                  {'category': category, 'post_list': post_list})
>>>>>>> 6f61790 (index)
