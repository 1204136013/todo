from django.contrib import messages
import django.contrib.auth as auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import (
    render,
    redirect,
)

# Create your views here.
from todo.models import Todo


# 用内置的权限系统来判断是否登陆
# 没登陆会跳转到 /login/view
@login_required(login_url='/login/view')
def index(request):
    return redirect('todo_index_all')


@login_required(login_url='/login/view')
def index_all(request):
    todos = Todo.objects.all()
    incomplete = Todo.objects.filter(completed=False).count()
    context = {
        'todos': todos,
        'active_index': True,
        'incomplete': incomplete,
    }
    return render(request, 'todo_index.html', context)


@login_required(login_url='/login/view')
def index_incomplete(request):
    todos = Todo.objects.filter(completed=False).all()
    incomplete = Todo.objects.filter(completed=False).count()
    context = {
        'todos': todos,
        'active_incomplete': True,
        'incomplete': incomplete,
    }
    return render(request, 'todo_index.html', context)


@login_required(login_url='/login/view')
def index_completed(request):
    todos = Todo.objects.filter(completed=True).all()
    incomplete = Todo.objects.filter(completed=False).count()
    context = {
        'todos': todos,
        'active_complete': True,
        'incomplete': incomplete,
    }
    return render(request, 'todo_index.html', context)


def add(request):
    title = request.POST['title']
    t = Todo(title=title, completed=False)
    print('todo add 1 <{}> <{}> <{}>'.format(t.__dict__, title, request.POST))
    t.save()
    print('todo add 2 <{}>'.format(t.__dict__))
    return redirect('todo_index_all')


def delete(request, todo_id):
    # todo_id 是一个 int，在 urls.py 里面设置
    t = Todo.objects.get(id=todo_id)
    t.delete()
    return redirect('todo_index_all')


def update(request):
    todo_id = request.POST['id']
    todo_title = request.POST['title']
    t = Todo.objects.get(id=todo_id)
    print('todo update', todo_id, todo_title, t, t.completed, t.title)
    t.title = todo_title
    t.save()
    return redirect('todo_index_all')


def complete(request, todo_id):
    t = Todo.objects.get(id=todo_id)
    t.completed = not t.completed
    t.save()
    return redirect('todo_index_all')


def all_complete(request):
    Todo.objects.all().update(completed=True)
    return redirect('todo_index_all')


def all_not_complete(request):
    Todo.objects.all().update(completed=False)
    return redirect('todo_index_all')


def login_view(request):
    user = request.user
    context = dict(
        username=user.username
    )
    return render(request, 'login.html', context)


def register_view(request):
    return render(request, 'register.html')


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(request, username=username, password=password)
    if user is not None:
        auth.login(request, user)
        messages.info(request, '登陆成功 {}'.format(user))
    else:
        messages.info(request, '用户名或者密码错误')
    return redirect('login_view')


def register(request):
    username = request.POST['username']
    password = request.POST['password']
    # django 有内置的 User 类
    user = User(username=username)
    # 密码哈希后加盐
    user.set_password(password)
    user.save()
    # 类似 flask flash
    messages.info(request, '注册成功 {}'.format(user))
    return redirect('register_view')
