from django.urls import path, include
from accounts import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'accounts'

urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='employee-list'),
    path('login/', views.LoginEmployeeView.as_view(), name='login'),
    path('logout/', views.LoginEmployeeView.as_view(), name='logout'),
    path('register/', views.RegisterEmployeeView.as_view(), name='register'),
    path('profile/<int:pk>/', include([
        path('', views.EmployeeDetailView.as_view(), name='employee-details'),
        path('update/', views.EmployeeUpdateView.as_view(), name='employee-update'),
        path('delete/', views.EmployeeDeleteView.as_view(), name='employee-delete')
    ])),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
