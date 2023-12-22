from django.urls import path
from . import views

urlpatterns = [
    path('tofiat/',views.ConvertToFiat.as_view(),name='tofiat'),
     path('tocrypto/',views.ConvertToCrypto.as_view(),name='tocrypto'),
     path('callbackurl/',views.CallBackUrl.as_view(),name='callbackurl'),
     path("results/",views.ResultUrl.as_view(),name='results'),
     path("tofiattransactions/",views.ToFiatTransactions.as_view(),name='tofiattransactions'),
     path('timeouturl/',views.TimeOutUrl.as_view(),name='timeouturl')
]