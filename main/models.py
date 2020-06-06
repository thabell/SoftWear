from django.db import models


# Create your models here.
class Brand(models.Model):
    name = models.CharField("Название", max_length=30)
    sex = models.CharField("Пол", max_length=10, default="Universal",
                           choices=[("Universal", "Universal"), ("Man", "Man"), ("Woman", "Woman")])

    class Meta:
        ordering = ['name']
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"

    def __str__(self):
        return self.name


class ClothesType(models.Model):
    name = models.CharField("Название", max_length=30)
    sex = models.CharField("Пол", max_length=10, default="Universal",
                           choices=[("Universal", "Universal"), ("Man", "Man"), ("Woman", "Woman")])

    class Meta:
        ordering = ['name']
        verbose_name = "Тип одежды"
        verbose_name_plural = "Типы одежды"

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField("Название", max_length=300)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="item", null=True)
    clothes_type = models.ManyToManyField(ClothesType, related_name="item")
    new = models.BooleanField("Новое", default=False)
    sex = models.CharField("Пол", max_length=10, default="Man", choices=[("Man", "Man"), ("Woman", "Woman")])
    cost_int = models.IntegerField("Цена, руб.")
    cost_fractional = models.IntegerField("Цена, коп.", default=0)
    sale = models.IntegerField("Скидка", default=0)
    photo = models.ImageField('Фото', upload_to='main/item/photo')

    class Meta:
        ordering = ['-new', 'name']
        verbose_name = "Вещь"
        verbose_name_plural = "Вещи"

    def __str__(self):
        return self.name


from django.contrib.auth.models import User


class CartPiece(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart_piece")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="cart_item")

    @classmethod
    def create(cls, user, item):
        piece = cls(user=user, item=item)
        return piece

    class Meta:
        verbose_name = "Покупка в корзине"
        verbose_name_plural = "Покупки в корзине"

    def __str__(self):
        return "В корзине " + str(self.item)


class OrderPiece(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order_piece")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="order_item")
    date = models.DateTimeField("Дата", auto_now_add=True)
    done = models.BooleanField("Выполнен", default=False)

    @classmethod
    def create(cls, user, item):
        piece = cls(user=user, item=item)
        return piece

    class Meta:
        verbose_name = "Покупка заказанная"
        verbose_name_plural = "Покупки заказанные"

    def __str__(self):
        if self.done:
            status = ". Статус заказа: Выполнен"
        else:
            status = ". Статус заказа: Выполняется"
        return "Заказ № " + str(self.id) + " от " + self.date.strftime('%Y-%m-%d %H:%M') + ". Вещь: " + str(self.item) + status


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review", null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="review_item", null=True, blank=True,
                             verbose_name="Вещь")
    comment = models.TextField('Комментарий')
    date = models.DateTimeField("Дата", auto_now_add=True)
    viewed = models.BooleanField("Просмотрен", default=False)

    class Meta:
        ordering = ['viewed', '-date']
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return "Отзыв № " + str(self.id) + " от " + self.date.strftime('%Y-%m-%d %H:%M') + ". Вещь: " + str(self.item)


class Refund(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="refund", null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="refund_item", null=True, blank=True,
                             verbose_name="Вещь")
    comment = models.TextField('Комментарий')
    date = models.DateTimeField("Дата", auto_now_add=True)
    done = models.BooleanField("Выполнен", default=False)

    class Meta:
        ordering = ['done', '-date']
        verbose_name = "Заявка на возврат"
        verbose_name_plural = "Заявки на возврат"

    def __str__(self):
        return "Заявка № " + str(self.id) + " от " + self.date.strftime('%Y-%m-%d %H:%M') + ". Вещь: " + str(self.item)
