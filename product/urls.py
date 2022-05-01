from django.urls import path

from product import views


urlpatterns = [
    path("v1/products/", views.v1.ProductsView.as_view()),
    path("v1/products/<int:pk>/", views.v1.ProductView.as_view()),
]
