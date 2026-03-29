from django.urls import path, include
from projects import views

app_name = 'projects'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('projects/', views.ProjectListView.as_view(), name='projects-list'),
    path('create/', views.ProjectCreateView.as_view(), name='project-create'),
    path('<int:pk>/', include([
        path('details/', views.ProjectDetailView.as_view(), name='project-details'),
        path('update/', views.ProjectUpdateView.as_view(), name='project-update'),
        path('delete/', views.ProjectDeleteView.as_view(), name='project-delete'),
    ])),

]
