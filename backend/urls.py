"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import api
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from client.views import Index 
from api.views import GetPositions, AddToCart, GetCart, ValidatePromo, RemoveFromCart, SetPositionAmount
from backend import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view()),
    path('sale', Index.as_view()),
    path('cart', Index.as_view()),
    path('api/cart.get', GetCart.as_view()),
    path('api/cart.add', AddToCart.as_view()),
    path('api/cart.remove', RemoveFromCart.as_view()),
    path('api/cart.amount', SetPositionAmount.as_view()),
    path('api/promo.check', ValidatePromo.as_view()),
    path('api/positions', GetPositions.as_view())
]


#urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#handler404 = 'client.views.NotFound'