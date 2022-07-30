from django.urls import path

from .views import Home, SnacksListView, SnacksDetailView, SnackCreateView, SnackUpdateView, SnackDeleteView
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('', SnacksListView.as_view(), name="Snack_list"),
    path('<int:pk>/', SnacksDetailView.as_view(), name='Snack_detail'),
    path('create/', SnackCreateView.as_view(), name='Snack_create'),
    path("<int:pk>/update/", SnackUpdateView.as_view(), name='Snack_update'),
    path('<int:pk>/delete/', SnackDeleteView.as_view(), name="Snack_delete")
]