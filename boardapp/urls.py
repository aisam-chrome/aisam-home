from django.urls import path
from .views import signupfunc, loginfunc, listfunc, logoutfunc, detailfunc, goodfunc, readfunc, BoardCreate, deletefunc, topfunc, homefunc, List, profilefunc, mydetailfunc


urlpatterns = [
    path('top/', topfunc, name='top'),
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('logout/', logoutfunc, name='logout'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('good/<int:pk>', goodfunc, name='good'),
    path('read/<int:pk>', readfunc, name='read'),
    path('create/', BoardCreate.as_view(), name='create'),
    path('delete/<int:pk>', deletefunc, name='delete'),
    path('home/', homefunc, name='home'),
    path('items/', List.as_view(), name = 'items'),
    path('profile/', profilefunc, name='profile'),
    path('mydetail/<int:pk>', mydetailfunc, name='mydetail'),
]
