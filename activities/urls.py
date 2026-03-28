from django.urls import path

from activities import views

app_name = 'activities'

urlpatterns = [
    path('', views.ActivityListView.as_view(), name='activities-list'),
    path('add', views.ActivityCreateView.as_view(), name='activity-add'),

]
