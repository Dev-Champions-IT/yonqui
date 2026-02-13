from django.urls import path
from . import views

urlpatterns = [
    path('apply-membership/', views.apply_membership, name='apply_membership'),
]
