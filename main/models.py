from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Dish(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(verbose_name='Изображение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'


class Review(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name='Оценка')
    review = models.TextField(verbose_name='Отзыв')

    def __str__(self):
        return self.name + ' - ' + str(self.stars)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Order(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    date = models.DateTimeField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    people_count = models.IntegerField(validators=[MinValueValidator(1)], default=1, verbose_name='Количество гостей')
    floor = models.IntegerField(validators=[MinValueValidator(1)], default=1, verbose_name='Этаж')

    def __str__(self):
        return self.name + ' - ' + str(self.date.date().strftime('%d.%m.%Y')) + ' ' + str(self.time.strftime('%H:%M'))

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони'
