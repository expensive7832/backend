from django.urls import path
from .views import getUsers, signup, fetchProducts, authentication, singleproduct, deleteproduct
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("allusers/", getUsers.as_view()),
    path("signup/", signup.as_view()),
    path("products/", fetchProducts.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("user/<int:pk>", authentication.as_view()),
    path("singleproduct/<int:pk>", singleproduct.as_view()),
    path("deleteproduct/<int:pk>", deleteproduct.as_view())
]
