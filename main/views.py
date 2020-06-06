from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Brand, ClothesType, Item, OrderPiece, Review, CartPiece

from random import randint


# Create your views here.
def index(request):
    men_clothes_types = ClothesType.objects.filter(sex__in=["Man", "Universal"])
    men_brands = Brand.objects.filter(sex__in=["Man", "Universal"])
    women_clothes_types = ClothesType.objects.filter(sex__in=["Woman", "Universal"])
    women_brands = Brand.objects.filter(sex__in=["Woman", "Universal"])
    lasts = Item.objects.filter(new=True)[0:3]
    brands = Brand.objects.all()[0:5]

    id_plus_count = [0, 0]
    mas = [[]] * Item.objects.all().count()
    # [[], [], [], [], []]
    print(mas)
    for i in range(len(mas)):
        mas[i] = id_plus_count.copy()  # создаем пары id - количество вхождений
        # [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        mas[i][0] = Item.objects.all()[i].id  # получаем id очередной вещи
        # [[5, 0], [3, 0], [2, 0], [7, 0], [14, 0]]
        mas[i][1] += OrderPiece.objects.filter(item__id=mas[i][0]).count()
        # считаем, сколько таких объектов лежит в корзинах пользователей
        mas[i][1] += CartPiece.objects.filter(item__id=mas[i][0]).count()
        # считаем, сколько таких объектов лежит в заказах пользователей
        # [[5, 4], [3, 0], [2, 1], [7, 0], [14, 0]]
    print(mas)
    mas.sort(key=lambda it: -it[1])  # сортируем по количеству вхождений с наибольшего
    # [[5, 4], [6, 2], [2, 1], [4, 1], [20, 1]]
    print(mas)
    popul_ids = [mas[0][0], mas[1][0], mas[2][0]]  # вытаскиваем id популярных
    print(popul_ids)
    popular_items = Item.objects.filter(id__in=popul_ids)  # получаем по id объекты
    print(popular_items)
    return render(request, 'main/index.html', {
        "men_clothes_types": men_clothes_types,
        "men_brands": men_brands,
        "women_clothes_types": women_clothes_types,
        "women_brands": women_brands,
        "lasts": lasts,
        "brands": brands,
        "popular_items": popular_items
    })


def about(request):
    men_clothes_types = ClothesType.objects.filter(sex__in=["Man", "Universal"])
    men_brands = Brand.objects.filter(sex__in=["Man", "Universal"])
    women_clothes_types = ClothesType.objects.filter(sex__in=["Woman", "Universal"])
    women_brands = Brand.objects.filter(sex__in=["Woman", "Universal"])
    return render(request, 'main/about.html', {
        "men_clothes_types": men_clothes_types,
        "men_brands": men_brands,
        "women_clothes_types": women_clothes_types,
        "women_brands": women_brands
    })


from django.http import HttpResponseRedirect
from django.urls import reverse


@login_required(login_url='login')
def cart(request):
    men_clothes_types = ClothesType.objects.filter(sex__in=["Man", "Universal"])
    men_brands = Brand.objects.filter(sex__in=["Man", "Universal"])
    women_clothes_types = ClothesType.objects.filter(sex__in=["Woman", "Universal"])
    women_brands = Brand.objects.filter(sex__in=["Woman", "Universal"])
    if request.method == "POST":
        if "bye_from_cart" in request.POST:
            print("bye_from_cart")
            for piece in request.user.cart_piece.all():
                new_order_piece = OrderPiece.create(request.user, piece.item)
                new_order_piece.save()
                piece.delete()
            return HttpResponseRedirect('{}?sent=True'.format(reverse('cart', kwargs={})))
        elif "delete_from_cart" in request.POST:
            print("delete_from_cart")
            request.user.cart_piece.filter(item__id=request.POST.get("delete_from_cart")).last().delete()
            return HttpResponseRedirect('{}'.format(reverse('cart', kwargs={})))
    else:
        if "id" in request.GET:
            new_cart_piece = CartPiece.create(request.user, Item.objects.get(id=request.GET.get("id")))
            new_cart_piece.save()
    return render(request, 'main/cart.html', {
        "men_clothes_types": men_clothes_types,
        "men_brands": men_brands,
        "women_clothes_types": women_clothes_types,
        "women_brands": women_brands,
        "sent": request.GET.get("sent", False)
    })


def item(request):
    men_clothes_types = ClothesType.objects.filter(sex__in=["Man", "Universal"])
    men_brands = Brand.objects.filter(sex__in=["Man", "Universal"])
    women_clothes_types = ClothesType.objects.filter(sex__in=["Woman", "Universal"])
    women_brands = Brand.objects.filter(sex__in=["Woman", "Universal"])
    curr_item = None
    if request.method == "GET":
        if "id" in request.GET:
            curr_item = Item.objects.get(id=request.GET.get("id"))
    return render(request, 'main/item.html', {
        "men_clothes_types": men_clothes_types,
        "men_brands": men_brands,
        "women_clothes_types": women_clothes_types,
        "women_brands": women_brands,
        "curr_item": curr_item
    })


@login_required(login_url='login')
def profile(request):
    men_clothes_types = ClothesType.objects.filter(sex__in=["Man", "Universal"])
    men_brands = Brand.objects.filter(sex__in=["Man", "Universal"])
    women_clothes_types = ClothesType.objects.filter(sex__in=["Woman", "Universal"])
    women_brands = Brand.objects.filter(sex__in=["Woman", "Universal"])
    return render(request, 'main/profile.html', {
        "men_clothes_types": men_clothes_types,
        "men_brands": men_brands,
        "women_clothes_types": women_clothes_types,
        "women_brands": women_brands
    })


def shop(request):
    all_clothes_types = ClothesType.objects.all()
    men_clothes_types = all_clothes_types.filter(sex__in=["Man", "Universal"])
    women_clothes_types = all_clothes_types.filter(sex__in=["Woman", "Universal"])
    all_brands = Brand.objects.all()
    men_brands = all_brands.filter(sex__in=["Man", "Universal"])
    women_brands = all_brands.filter(sex__in=["Woman", "Universal"])
    items = Item.objects.all()
    if "new" in request.GET:
        req_new = request.GET.get("new")
        if req_new == "all":
            pass
        elif req_new == "True":
            items = items.filter(new="True")
        elif req_new == "False":
            items = items.filter(new="False")
    if "sex" in request.GET:
        req_sex = request.GET.get("sex")
        if req_sex == "all":
            pass
        elif req_sex == "Man":
            items = items.filter(sex="Man")
        elif req_sex == "Woman":
            items = items.filter(sex="Woman")
    clothes_type_ids = ClothesType.objects.values_list('id', flat=True)
    if "clothes_type_id" in request.GET:
        clothes_type_ids = request.GET.getlist("clothes_type_id")
        items = items.filter(clothes_type__id__in=clothes_type_ids)  # получить из поля clothes_type объект ClothesType,
        # у него получить id и сравнить его со списком допустимых
        clothes_type_ids = ClothesType.objects.filter(id__in=clothes_type_ids).values_list('id', flat=True)
        # на странице будем расставлять checked на inputы.
        # if id in id_list работает только с таким объектом:
        # <QuerySet [7, 2, 5, 10, 6, 3, 8, 9, 4, 1, 11]>
    brand_ids = Brand.objects.values_list('id', flat=True)
    if "brand_id" in request.GET:
        brand_ids = request.GET.getlist("brand_id")
        items = items.filter(brand__id__in=brand_ids)
        brand_ids = Brand.objects.filter(id__in=brand_ids).values_list('id', flat=True)
    if "sale" in request.GET:
        req_sale = request.GET.get("sale")
        if req_sale == "all":
            pass
        elif req_sale == "True":
            items = items.exclude(sale=0)  # исключить те товары, у которых нет скидки
        elif req_sale == "False":
            items = items.filter(sale=0)  # оставить только те товары, у которых нет скидки
    items = items.distinct()  # удаляет дубликаты, если они добавились, например платье-анорак
    return render(request, 'main/shop.html', {
        "all_clothes_types": all_clothes_types,
        "men_clothes_types": men_clothes_types,
        "women_clothes_types": women_clothes_types,
        "all_brands": all_brands,
        "men_brands": men_brands,
        "women_brands": women_brands,
        "items": items,
        "clothes_type_ids": clothes_type_ids,
        "brand_ids": brand_ids
    })


from .forms import ReviewForm, RefundForm


def support(request):
    review_form = ReviewForm()
    refund_form = RefundForm()
    men_clothes_types = ClothesType.objects.filter(sex__in=["Man", "Universal"])
    men_brands = Brand.objects.filter(sex__in=["Man", "Universal"])
    women_clothes_types = ClothesType.objects.filter(sex__in=["Woman", "Universal"])
    women_brands = Brand.objects.filter(sex__in=["Woman", "Universal"])
    if request.method == "POST":
        if "review_submit" in request.POST:
            review_form = ReviewForm(request.POST)
            new_review = review_form.save(commit=False)
            if request.user.is_authenticated:
                new_review.user = request.user
            new_review.save()
            return HttpResponseRedirect('{}?review_sent=True'.format(reverse('support', kwargs={})))
        elif "refund_submit" in request.POST:
            refund_form = RefundForm(request.POST)
            new_refund = refund_form.save(commit=False)
            if request.user.is_authenticated:
                new_refund.user = request.user
            new_refund.save()
            return HttpResponseRedirect('{}?refund_sent=True'.format(reverse('support', kwargs={})))
    return render(request, 'main/support.html', {
        "men_clothes_types": men_clothes_types,
        "men_brands": men_brands,
        "women_clothes_types": women_clothes_types,
        "women_brands": women_brands,
        "review_form": review_form,
        "refund_form": refund_form,
        "review_sent": request.GET.get("review_sent", False),
        "refund_sent": request.GET.get("refund_sent", False)
    })


def terms(request):
    men_clothes_types = ClothesType.objects.filter(sex__in=["Man", "Universal"])
    men_brands = Brand.objects.filter(sex__in=["Man", "Universal"])
    women_clothes_types = ClothesType.objects.filter(sex__in=["Woman", "Universal"])
    women_brands = Brand.objects.filter(sex__in=["Woman", "Universal"])
    return render(request, 'main/terms.html', {
        "men_clothes_types": men_clothes_types,
        "men_brands": men_brands,
        "women_clothes_types": women_clothes_types,
        "women_brands": women_brands
    })


from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def signup(request):
    men_clothes_types = ClothesType.objects.filter(sex__in=["Man", "Universal"])
    men_brands = Brand.objects.filter(sex__in=["Man", "Universal"])
    women_clothes_types = ClothesType.objects.filter(sex__in=["Woman", "Universal"])
    women_brands = Brand.objects.filter(sex__in=["Woman", "Universal"])
    user_form = UserForm()
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            User.objects.create_user(user_form.cleaned_data['username'],
                                     user_form.cleaned_data['email'],
                                     user_form.cleaned_data['password'])
            user = authenticate(
                username=user_form.cleaned_data['username'],
                password=user_form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
            else:
                print('User login failed')
            return redirect('../')
    return render(request, 'registration/signup.html', {
        "men_clothes_types": men_clothes_types,
        "men_brands": men_brands,
        "women_clothes_types": women_clothes_types,
        "women_brands": women_brands,
        "user_form": user_form
    })
