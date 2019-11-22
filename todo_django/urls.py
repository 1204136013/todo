"""todo_django URL Configuration

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
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('todo/', views.index_all, name='todo_index_all'),
    path('todo/incomplete', views.index_incomplete, name='todo_index_incomplete'),
    path('todo/completed', views.index_completed, name='todo_index_completed'),
    path('todo/add', views.add, name='todo_add'),
    path('todo/delete/<int:todo_id>', views.delete, name='todo_delete'),
    path('todo/update', views.update, name='todo_update'),
    path('todo/complete/<int:todo_id>', views.complete, name='todo_complete'),
    path('todo/all/complete', views.all_complete, name='todo_all_complete'),
    path('todo/all/not/complete', views.all_not_complete, name='todo_all_not_complete'),
    path('login/view', views.login_view, name='login_view'),
    path('login', views.login, name='login'),
    path('register/view', views.register_view, name='register_view'),
    path('register', views.register, name='register'),
]
