from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customers/', views.CustomerListView.as_view(), name='customers'),
    path('customer/<int:pk>', views.CustomerDetailView.as_view(), name='customer-detail'),
    path('systems/', views.SystemListView.as_view(), name='systems'),
    path('systems/<int:pk>', views.SystemDetailView.as_view(), name='system-detail'),
]