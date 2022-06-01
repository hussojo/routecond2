from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from . import models

class RouteListView(ListView):
    model = models.Route

class RouteDetailView(DetailView):
    model = models.Route
    fields = "__all__"
    success_url = "/route/"

class RouteUpdateView(UpdateView):
    model = models.Route
    fields ='__all__'
    success_url = "/route/"

class RouteCreateView(CreateView):
    model = models.Route
    fields = "__all__"
    success_url = "/route/"

class RouteDeleteView(DeleteView):
    model = models.Route
    fields = "__all__"
    success_url = "/route/"

