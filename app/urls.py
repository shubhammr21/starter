
from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    re_path(r'^transactions/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', views.TransactionView.as_view(),
            name='transactions'),
    # path('transactions/<pk>/<action>/', views.TransactionView.as_view(), name='transactions'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
