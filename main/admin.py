from django.contrib import admin
from .models import Brand, ClothesType, Item, CartPiece, OrderPiece, Review, Refund
from django.contrib.auth.models import User


class ItemInline(admin.TabularInline):
    model = Item


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex')
    inlines = [ItemInline]


@admin.register(ClothesType)
class ClothesTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'brand', 'new', 'sex', 'cost_int', 'cost_fractional', 'sale', 'photo')


@admin.register(CartPiece)
class CartPieceAdmin(admin.ModelAdmin):
    list_display = ('user', 'item')


@admin.register(OrderPiece)
class OrderPieceAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'date', 'done')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'comment', 'date', 'viewed')


@admin.register(Refund)
class RefundAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'comment', 'date', 'done')


class OrderPieceInline(admin.TabularInline):
    model = OrderPiece


class CartPieceInline(admin.TabularInline):
    model = CartPiece


class ReviewInline(admin.TabularInline):
    model = Review


class RefundInline(admin.TabularInline):
    model = Refund


admin.site.unregister(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [OrderPieceInline, ReviewInline, RefundInline, CartPieceInline]
