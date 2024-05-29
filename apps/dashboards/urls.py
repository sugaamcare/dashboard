from django.urls import path
from .views import DashboardsView,upload



urlpatterns = [
    path("",DashboardsView.as_view(template_name="dashboard_analytics.html"),name="index",),
    path("upload/",DashboardsView.as_view(template_name="dashboard_analytics.html"),name="index",),
    # path('upload/', upload, name="index"),

]
