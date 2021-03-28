from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customers/', views.CustomerListView.as_view(), name='customers'),
    path('customer/<int:pk>', views.CustomerDetailView.as_view(), name='customer-detail'),
    path('systems/', views.SystemListView.as_view(), name='systems'),
    path('systems/<int:pk>', views.SystemDetailView.as_view(), name='system-detail'),
]

# Alter data via form
urlpatterns += [
    path('customer/<int:pk>/renew/', views.renew_customer, name='renew-customer'),
    path('systems/create/', views.SystemCreate.as_view(), name='system-create'),
    path('systems/<int:pk>/update/', views.SystemUpdate.as_view(), name='system-update'),
    path('systems/<int:pk>/delete/', views.SystemDelete.as_view(), name='system-delete'),

]