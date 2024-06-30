from django.urls import path
<<<<<<< HEAD

=======
>>>>>>> 6f61790 (index)
from . import views

app_name = 'pages'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules'),
<<<<<<< HEAD
]
=======
]
>>>>>>> 6f61790 (index)
