from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ensure there is an `index` view in `views.py`.
    path('activity/', views.activity, name='activity'),
    path('Portfolio/',views.Portfolio,name='Portfolio'),

]
