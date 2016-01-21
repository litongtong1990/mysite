    
from django.conf.urls import url

from . import views

urlpatterns = [

	url(r'^(?P<product_name>rice[0-9]+)/$', views.generate_qrcode, name='qrcode'),
    #url(r'^(?P<product_name>rice[0-9]+)/$', views.test, name='test'),

]






