from django.contrib import admin
from django.urls import path
from routecond import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('route/', views.RouteListView.as_view()),
    path('route/<int:pk>', views.RouteDetailView.as_view()),
    path('route/new', views.RouteCreateView.as_view()),
    path('route/<int:pk>/update', views.RouteUpdateView.as_view()),
    path('route/<int:pk>/delete', views.RouteDeleteView.as_view()),
]
