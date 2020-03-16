from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='MyHomePage'),
    path('about/', views.about, name='MyAbout'),
    path('careers/', views.careers, name='MyCareers'),
    path('branches/', views.branches, name='MyBranches'),
    path('products/', views.products, name='MyProducts'),
    path('feedback/', views.feedback, name='MyFeedback'),
]