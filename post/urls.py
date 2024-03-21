from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post'),
    path('<slug:slug>', views.post_page, name='page'), #<>사이에 빈칸이 있으면 에러난다.
]