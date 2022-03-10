from django.urls import path
from .views import DrinkListView, DrinkDetailView, DrinkCreateView, DrinkUpdateView, DrinkDeleteView

urlpatterns = [
    path('', DrinkListView.as_view(), name='drink_list'),
    path('<int:pk>/', DrinkDetailView.as_view(), name='drink_detail'),
    path('create/', DrinkCreateView.as_view(), name='drink_create'),
    path('<int:pk>/update/', DrinkUpdateView.as_view(), name='drink_update'),
    path('<int:pk>/delete/', DrinkDeleteView.as_view(), name='drink_delete'),
]