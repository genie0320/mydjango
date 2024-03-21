from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.post_list, name='list'),
    path('new-post/', views.post_new, name='new-post'), # 반드시 slug 설정 위로 와야 함.
    path('<slug:slug>', views.post_page, name='page'), #<>사이에 빈칸이 있으면 에러난다.
]