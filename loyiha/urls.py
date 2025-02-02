from django.urls import path

from .views import (
    HomePageView,
    AboutPageView, BasePageView,
    MainPageView,
    SalomPageView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('base/', BasePageView.as_view(), name='base'),
    path('main/', MainPageView.as_view(), name='main'),
    path('salom/', SalomPageView.as_view(), name='salom')
]