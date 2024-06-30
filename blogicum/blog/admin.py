from django.contrib import admin

from .models import Post, Category

admin.site.empty_value_display = 'Не задано'


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'pub_date',
        'is_published',
        'created_at',
        'author',
        'category',
        'location'
    )
    list_editable = (
        'text',
        'author',
        'is_published',
        'category'
    )
    search_fields = ('title',) 
    list_filter = ('category',)
    list_display_links = ('title',)


class PostInline(admin.TabularInline):
    model = Post
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
