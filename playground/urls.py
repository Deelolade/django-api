from django.urls import path;
from . import views

# URL config
urlpatterns = [
    # path('hello/', views.say_hello),
    # path('user/', views.get_user_data),
    path('', views.home),
    path('post/<int:id>/', views.post)
]
