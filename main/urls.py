from django.urls import path
from . import views
from .views import home, about, new_index
from .views import ProductCreateView, ProductUpdateView, ProductDeleteView, ProductDetailView

urlpatterns = [
    path('', views.home, name="home"),
    path("about/", views.about, name="about"),
    path("new-index/", views.new_index, name="new"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='post-detail'),
    path('product/create/', ProductCreateView.as_view(), name="create"),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='post-update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='post-delete'),
]
