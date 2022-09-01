from django.urls import path
from . import views

app_name = 'articles'
# url의 name space
urlpatterns = [
    path('index/', views.index, name='index'),
    # articles안에 있는 views 함수를 발동(이름은 index)
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    # 수정할 수 있는 페이지
    path('<int:pk>/edit/', views.edit, name='edit'),
    # 수정 기능을 할 페이지
    path('<int:pk>/update/', views.update, name='update'),
]