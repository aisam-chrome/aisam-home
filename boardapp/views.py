from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import BoardModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, TemplateView, DetailView
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.db.models import Q
from django.shortcuts import render,get_object_or_404
from django.views import generic
from functools import reduce
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



#　top機能
def topfunc(request):
    return render(request, 'top.html')

# 新規会員登録機能
def signupfunc(request):
    # POSTメソッドで入って来た場合既存のuserか確認
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        try:
            #　userが既にいた場合
            User.objects.get(username=username2)
            return render(request, 'signup.html', {'error':'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(username2, '', password2)
            return redirect('login')
    return render(request, 'signup.html', {'some' :100})

#　ログイン機能
def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'login.html')

#　ログイン認証
@login_required
def listfunc(request):
    object_list = BoardModel.objects.order_by('-created_date')
    return render(request, 'list.html', {'object_list':object_list})

# logout機能
def logoutfunc(request):
    logout(request)
    return redirect('login')

# ぼやき詳細
def detailfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object':object})

@login_required
def mydetailfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    return render(request, 'mydetail.html', {'object':object})

#　いいね機能
def goodfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post2 = request.user.get_username()
    if post2 in post.readtext:
        return redirect('home')
    else:
        post.good = post.good + 1
        post.goodtext = post.goodtext + ' ' + post2
        post.save()
        return redirect('home')

#　既読機能
def readfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post2 = request.user.get_username()
    if post2 in post.readtext:
        return redirect('home')
    else:
        post.read += 1
        post.readtext = post.readtext + ' ' + post2
        post.save()
        return redirect('home')

# 新規ぼやき投稿機能
class BoardCreate(CreateView):
    template_name = 'create.html'
    model = BoardModel
    fields = ('title', 'content', 'author', 'images')
    success_url = reverse_lazy('list')

#　ぼやき削除機能(ぼやいたユーザーのみ削除可能に変更する)
@require_POST
def deletefunc(request, pk):
    boyaki = BoardModel.objects.get(pk=pk)
    boyaki.delete()
    return redirect('profile')

#　home画面
def homefunc(request):
    #　投稿最新順
    object_list = BoardModel.objects.order_by('-created_date')
    return render(request, 'home.html', {'object_list':object_list})

#　検索機能
class List(generic.ListView):
    model = BoardModel
    template_name = 'list.html'

    def get_queryset(self):
        products = BoardModel.objects.all()
        if 'q' in self.request.GET and self.request.GET['q'] != None:
            q = self.request.GET['q']
            products = products.filter(title__icontains = q)
        return products

#　ログイン中のuserが投稿したぼやきのみ表示
def profilefunc(request):
    #　ログイン中のユーザー情報取得
    user = request.user
    user_list = BoardModel.objects.filter(author__exact = user).order_by('-created_date')
    return render(request, 'profile.html', {'user_list':user_list})


