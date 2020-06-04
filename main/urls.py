from django.urls import path
from . import views as main_views
from django.contrib.auth import views as auth_views
from .models import Brand, ClothesType, Item, Review

urlpatterns = [
    path('', main_views.index, name='index'),
    path('index/', main_views.index, name='index'),
    path('about/', main_views.about, name='about'),
    path('cart/', main_views.cart, name='cart'),
    # /<int:item_id>/
    path('item/', main_views.item, name='item'),
    path('profile/', main_views.profile, name='profile'),
    path('shop/', main_views.shop, name='shop'),
    path('support/', main_views.support, name='support'),
    path('terms/', main_views.terms, name='terms'),
    path('login/', auth_views.LoginView.as_view(extra_context={
        "men_clothes_types": ClothesType.objects.filter(sex__in=["Man", "Universal"]),
        "men_brands": Brand.objects.filter(sex__in=["Man", "Universal"]),
        "women_clothes_types": ClothesType.objects.filter(sex__in=["Woman", "Universal"]),
        "women_brands": Brand.objects.filter(sex__in=["Woman", "Universal"])
    }), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', main_views.signup, name='signup'),
]
