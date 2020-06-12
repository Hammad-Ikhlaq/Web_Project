from django.urls import path
from . import views
from .views import (
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)


urlpatterns = [
    path('', views.home, name='MyHomePage'),
    path('about/', views.about, name='MyAbout'),
    path('cart/', views.cart, name='cart'),
    path('careers/', views.careers, name='MyCareers'),
    path('branches/', views.branches, name='MyBranches'),
    path('products/', views.products, name='MyProducts'),
    path('feedback/',  PostListView.as_view(), name='MyFeedback'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]