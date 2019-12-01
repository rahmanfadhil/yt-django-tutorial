"""todo_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from todos.views import home_page, about_page, create_todo, complete_todo, delete_todo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('create-todo/', create_todo, name='create-todo'),
    path('complete-todo/<int:pk>/', complete_todo, name='complete-todo'),
    path('delete-todo/<int:pk>/', delete_todo, name='delete-todo')
]
