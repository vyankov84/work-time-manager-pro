from django.urls import path, include
from invoices import views
from invoices.api_views import InvoiceListAPIView

app_name = 'invoices'

urlpatterns = [
    path('', views.InvoiceListView.as_view(), name='invoices-list'),
    path('create/', views.InvoiceCreateView.as_view(), name='invoice-create'),
    path('<int:pk>/', include([
        path('details/', views.InvoiceDetailView.as_view(), name='invoice-details'),
        path('update/', views.InvoiceUpdateView.as_view(), name='invoice-update'),
        path('delete/', views.InvoiceDeleteView.as_view(), name='invoice-delete'),
    ])),
    path('api/list/', InvoiceListAPIView.as_view(), name='api-invoice-list'),

]
