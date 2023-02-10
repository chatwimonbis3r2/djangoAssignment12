"""djangoAssignment12 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from App12 import views

urlpatterns = [
    path('showGoodsList', views.showGoodsList, name="showGoodsList"),
    path('showGoodsOne/<gid>', views.showGoodsOne, name="showGoodsOne"),
    path('showCustomerList', views.showCustomerList, name="showCustomerList"),
    path('showCustomerOne/<cid>', views.showCustomerOne, name="showCustomerOne"),
    path('newGoods', views.newGoods, name="newGoods"),
    path('newCustomer', views.newCustomer, name="newCustomer"),
    path('updateGoods/<gid>', views.updateGoods, name="updateGoods"),
    path('updateCustomer/<cid>', views.updateCustomer, name="updateCustomer"),
    path('deleteGoods/<gid>', views.deleteGoods, name='deleteGoods'),
    path('deleteCustomer/<cid>', views.deleteCustomer, name='deleteCustomer')
]
