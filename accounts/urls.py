from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('features/', views.features, name='features'),
    path('aboutus', views.about_us, name='aboutus'),
    path('contactus', views.contact_us, name='contactus'),
    path('healthform/', views.health_form, name='healthform'),

    path('register/', views.registerPage, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('adminuserlogs/', views.admin_user_logs, name='adminuserlogs'),

    path('adminupdateuser/<str:pk>/', views.admin_update_user, name='adminupdateuser'),
    path('admindeleteuser/<str:pk>/', views.admin_delete_user, name='admindeleteuser'),

    path('adminupdatehealthform/<str:pk>/', views.admin_update_health_form, name='adminupdatehealthform'),
    path('admindeletehealthform/<str:pk>/', views.admin_delete_health_form, name='admindeletehealthform'),

    path('adminhealthformlogs/', views.admin_health_form_logs, name='adminhealthformlogs'),
    path('adminredirect/', views.admin_redirect, name='adminredirect')

]