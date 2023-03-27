from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import Newaccount, SearchResultView

urlpatterns = [
    path('main', views.main, name='main'),
    path('contact', views.contact, name='contact'),
    path('transaction', views.transaction, name='transaction'),
    # path('login', views.login_fun, name='login'),
    path('deposit', views.deposit, name='deposit'),
    path('withdraw', views.withdraw, name='withdraw'),
    # path('account-details/<str:Ac_NO>/transaction/', views.transaction, name='transaction'),
    # path('new-user', views.Newuser, name='new-user'),
    path('new-account', Newaccount.as_view(), name='new-account'),
    path('account-details', views.details, name='account_details'),
    path('change-password', views.change_password, name='change-password'),
    path('delete', views.delete_account, name='delete'),
    path('search',SearchResultView.as_view(),name='search'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)