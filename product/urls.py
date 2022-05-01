from django.urls import include, path
from rest_framework_nested import routers

from product import views

v1 = routers.DefaultRouter()

v1.register(r"products", views.v1.ProductViewSet, basename="products")

urlpatterns = [
    path(r"v1/", include(v1.urls)),
]
