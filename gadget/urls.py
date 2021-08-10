from django.urls import path
from .import views

app_name = 'gadget'

urlpatterns = [
    path('', views.AllGadtgetsView.as_view(),name='home'),
    path('detail/<slug:slug>', views.GadgetDetailView.as_view(), name='detail')
]