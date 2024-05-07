from django import urls

from main import views

urlpatterns = [
    urls.path('', views.index, name='index'),
    urls.path('menu', views.menu, name='menu'),
    urls.path('about', views.about, name='about'),
    urls.path('contact', views.contact, name='contact'),
    urls.path('order_table', views.order_table, name='order'),
]
