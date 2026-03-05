from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='main'),
    path('article/<int:pk>',views.NewsDetail.as_view(),name='article_detail')
]