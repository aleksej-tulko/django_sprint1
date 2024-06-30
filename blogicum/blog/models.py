from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now

from core.models import TitledModel, PublishedAndCreatedModel

User = get_user_model()


# class PublishedPosts(models.QuerySet):
#     def published(self):
#         return self.filter(
#             pub_date__lte=now(),
#             is_published=True,
#             category__is_published=True
#         )


# class PostManager(models.Manager):
#     def get_published_posts(self):
#         return PublishedAndCreatedModel(self.model, using=self._db)

#     def published(self):
#         return self.get_queryset().published()


class Post(TitledModel, PublishedAndCreatedModel):
    """Публикация."""
    text = models.TextField(
        verbose_name="Текст"
    )
    pub_date = models.DateTimeField(
        verbose_name="Дата и время публикации",
        help_text="Если установить дату и время в будущем\
              — можно делать отложенные публикации."
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор публикации",
        related_name="get_author"
    )
    location = models.ForeignKey(
        "Location",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Местоположение",
        related_name="get_location"
    )
    category = models.ForeignKey(
        "Category",
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        related_name="get_category"
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title


class Category(TitledModel, PublishedAndCreatedModel):
    """Тематическая категория"""
    description = models.TextField(
        verbose_name="Описание"
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="Идентификатор",
        help_text="Идентификатор страницы для URL; разрешены символы латиницы,\
            цифры, дефис и подчёркивание."
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Location(PublishedAndCreatedModel):
    """Географическая метка"""
    name = models.CharField(
        max_length=256,
        verbose_name="Название места"
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name
