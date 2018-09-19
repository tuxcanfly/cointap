from django.conf.urls import url

from faucet import views

urlpatterns = [
    url(r'^balance/$', views.balance),
    url(r'^send/$', views.send),
]
