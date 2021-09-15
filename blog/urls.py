from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('form/create/', views.createView),
    path('form/edit/<int:id>', views.editView),
    path('create/', views.createBlog),
    path('edit/<int:id>', views.editBlog),
    path('delete/<int:id>', views.deleteBlog),
]
