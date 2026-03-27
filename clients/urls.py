from django.urls import path, include
from clients import views

app_name = 'clients'

urlpatterns = [
    path('', views.ClientList.as_view(), name='clients-list'),
    path('create/', views.ClientCreate.as_view(), name='client-create'),
    path('<int:pk>/', include([
        path('', views.ClientDetails.as_view(), name='client-details'),
        path('update/', views.ClientUpdate.as_view(), name='client-update'),
        path('delete/', views.ClientDelete.as_view(), name='client-delete'),
    ])),

]
