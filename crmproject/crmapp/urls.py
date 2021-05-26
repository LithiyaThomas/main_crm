from . import views
from django.urls import path

urlpatterns = [
    path('',views.customer,name='customer'),
    path('items/', views.items, name='items')
]
