from django.urls import path
from accounts import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'accounts'

urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='employee-list'),
    path('login/', views.LoginEmployeeView.as_view(), name='login'),
    path('logout/', views.LoginEmployeeView.as_view(), name='logout'),
    path('register/', views.RegisterEmployeeView.as_view(), name='register'),
    path('profile/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee-details')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
