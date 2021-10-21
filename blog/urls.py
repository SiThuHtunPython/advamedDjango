from django.urls import path
from django.contrib.auth import views as auth_views
from .views import MaintenanceDataListView, MaintenanceDataDetailView, MaintenanceDataCreateView, \
    MaintenanceDataUpdateView, MaintenanceDataDeleteView, UserMaintenanceDataListView, ServiceRecordDataCreateView, \
    ServiceRecordDataListView, InstallationRecordDataCreateView, InstallationServiceDataListView, \
    ServiceRecordDataDetailView, InstallationRecordDataDetailView, ServiceRecordDataUpdateView, \
    InstallationRecordDataUpdateView, UserServiceRecordDataListView, UserInstallationRecordDataListView, \
    InstallationRecordDataDeleteView, ServiceRecordDataDeleteView, maintenance2
from . import views



urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='blog/login.html'), name="login"),
    path('user/maintenance/<str:username>', UserMaintenanceDataListView.as_view(), name="user-maintenance_data"),
    path('user/service_record/<str:username>', UserServiceRecordDataListView.as_view(), name="user-service_record_data"),
    path('user/installation_record/<str:username>', UserInstallationRecordDataListView.as_view(), name="user-installation_record_data"),
    path('maintenance_data/<int:pk>/', MaintenanceDataDetailView.as_view(), name="maintenance_data-detail"),
    path('maintenance_data/add_record/', MaintenanceDataCreateView.as_view(), name="maintenance_data-create"),
    path('service_record_data/request_record/', ServiceRecordDataCreateView.as_view(), name="service-record_data-request"),
    path('installation_record_data/request_record/', InstallationRecordDataCreateView.as_view(), name="installation-record_data-request"),
    path('maintenance_data/<int:pk>/update/', MaintenanceDataUpdateView.as_view(), name="maintenance_data-update"),
    path('maintenance_data/<int:pk>/delete/', MaintenanceDataDeleteView.as_view(), name="maintenance_data-delete"),
    path('service_record/', ServiceRecordDataListView.as_view(), name="service_record"),
    path('installation_record/', InstallationServiceDataListView.as_view(), name="installation_record"),
    path('service_record_data/<int:pk>/', ServiceRecordDataDetailView.as_view(), name="service_record_data-detail"),
    path('service_record_data/<int:pk>/update/', ServiceRecordDataUpdateView.as_view(), name="service_record_data-update"),
    path('service_record_data/<int:pk>/delete/', ServiceRecordDataDeleteView.as_view(), name="service_record_data-delete"),
    path('installation_record_data/<int:pk>/update/', InstallationRecordDataUpdateView.as_view(), name="installation_record_data-update"),
    path('installation_record_data/<int:pk>/', InstallationRecordDataDetailView.as_view(), name="installation_record_data-detail"),
    path('installation_record_data/<int:pk>/delete/', InstallationRecordDataDeleteView.as_view(), name="installation_record_data-delete"),
    path('preventive_maintenance_record/', views.maintenance2, name="maintenance2"),
    path('home', views.MaintenanceDataListView, name="blog-home"),
]