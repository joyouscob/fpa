from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.SearchCreateView.as_view(), name='search'),
    path('add/', views.SearchCreateView.as_view(), name='search_add'),
    path('predict/', views.predict, name='predict'),
    # path('<int:pk>/', views.PersonUpdateView.as_view(), name='person_change'),
    path('ajax/load-lgas/', views.load_lgas, name='ajax_load_lgas'),  # <-- this one here
]
