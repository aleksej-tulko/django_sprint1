from django.urls import path
<<<<<<< HEAD

=======
>>>>>>> 6f61790 (index)
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
=======
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
>>>>>>> 6f61790 (index)
    path(
        'category/<slug:category_slug>/',
        views.category_posts, name='category_posts'
    ),
]
