from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('providers/', views.provider_list, name='provider_list'),
    path('provider/<int:provider_id>/', views.provider_detail, name='provider_detail'),
    path('book/<int:provider_id>/', views.book_appointment, name='book'),
    path("availability/", views.edit_availability, name="edit_availability"),
    path("appointment/<int:appointment_id>/update/", views.update_status, name="update_status"),
    path("search/", views.search_providers, name="search_providers"),
    path("provider/<int:provider_id>/available-times/", views.available_times, name="available_times"),
]
