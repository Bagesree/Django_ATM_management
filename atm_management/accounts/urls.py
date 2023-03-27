
from django .urls import path

from .views import SignUpView,subscribe

urlpatterns =[
    path('signup/',SignUpView.as_view(),name='sign-up'),
    path('subscribe/', subscribe, name='subscribe'),

]