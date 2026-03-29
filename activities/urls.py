from django.urls import path

from activities import views

app_name = 'activities'

urlpatterns = [
    path('', views.ActivityListView.as_view(), name='activities-list'),
    path('add', views.ActivityCreateView.as_view(), name='activity-add'),
    path('<int:pk>/update/', views.ActivityUpdateView.as_view(), name='activity-update'),
    path('<int:pk>/delete/', views.ActivityDeleteView.as_view(), name='activity-delete'),

]
