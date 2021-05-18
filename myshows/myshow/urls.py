from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "myshow"

urlpatterns = [
    # Leave as empty string for base url
    path('', views.store, name="store"),
    path('cart/<int:id>/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('signup/', views.signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='myshowcd..c/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='myshow/logout.html'), name="logout"),
    path('details/<int:id>/', views.detail, name='detail'),
    path('addreview/<int:id>/', views.add_review, name="add_review"),
    path('search/', views.search, name="searchfor"),
    path('/<slug:id>/', views.moviefilter, name="moviefilter"),
    ]


    # path('review/<pk>', views.movie_review, name='reviews'),]
    # path('addreview/<pk>', views.add_review, name='add_review'),]
    # path('movieinfo/(?P<pk>\d+)/', views.movieinfo, name='movieinfo'),]
    # path(r'^movie/<int:pk>/$', views.movie_info, name='details'),]
    # path('movieinfo/', views.movieinfo, name="movieinfo"), ]


