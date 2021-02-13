from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf.urls import static
from django.conf import settings

from .views import (
    HapusMenuView,
    IndexView,
    LoginView,
    LogoutView,
    ManageMenuView,
    OrderMenuView,
    TambahMenuView,
    OrderingView,
    UpdateMenuView,
    OrderCompleteView,
)
app_name = 'restoran'
urlpatterns = [
    path('managemenu/', ManageMenuView.as_view(), name='managemenu'),
    path('ordermenu/', OrderMenuView.as_view(), name='ordermenu'),
    path('tambahmenu/', TambahMenuView.as_view(), name='tambahmenu'),
    path('ubahmenu', UpdateMenuView.as_view(), name='ubahmenu'),
    path('hapusmenu/<pk>', HapusMenuView.as_view(), name='hapusmenu'),
    path('ordering/', OrderingView.as_view(), name='ordering'),
    path('ordercomplete/<id>',
         OrderCompleteView.as_view(), name='ordercomplete'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('', IndexView.as_view(), name='index'),
]
