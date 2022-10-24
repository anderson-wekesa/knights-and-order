"""swordstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path #, include
from store import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home,  name="home"), #Home Page, the actual store itself
    path('product/<slug:slug>/', views.product, name = "product"),
    #path('add_to_cart/<slug:slug>', views.add_to_cart, name="add_to_cart"),

    path('cart/add/<slug:slug>/', views.cart_add, name="cart_add"),
    # path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    # path('cart/item_increment/<int:id>/',
    #      views.item_increment, name='item_increment'),
    # path('cart/item_decrement/<int:id>/',
    #      views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('checkout/',views.cart_detail,name='cart_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
