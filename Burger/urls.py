"""
URL configuration for Burger project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path 
from burger_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('menu/', views.menu_view, name='menu'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.view_cart, name='cart'),
    path('order_now/', views.order_now, name='order_now'),
    path('clear-cart/', views.clear_cart, name='clear_cart'), 
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('update_cart/<int:item_id>/<str:action>/', views.update_cart, name='update_cart'),
    path('payment',views.payment, name='payment'),
    path('payment_success/',views.payment_success ,name='payment_success'),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
