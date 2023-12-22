from django.urls import path
from . import views

urlpatterns = [
    path('tofiat/',views.ConvertToFiat.as_view(),name='tofiat'),
     path('tocrypto/',views.ConvertToCrypto.as_view(),name='tocrypto'),
     path('callbackurl/',views.CallBackUrl.as_view(),name='callbackurl'),
     path('donations',views.Donations.as_view(),name='donations'),
     path('donationscallback/',views.DonationsCallbackUrl.as_view(),name='donations'),
     path("results/",views.ResultUrl.as_view(),name='results'),
     path("tofiattransactions/",views.ToFiatTransactions.as_view(),name='tofiattransactions'),
     path("tocryptotransactions/", views.ToCryptoTransactions.as_view(),name='tpcryptotransactions'),
     path('timeouturl/',views.TimeOutUrl.as_view(),name='timeouturl')
]