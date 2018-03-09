from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^predict/$', views.predict, name='emotionFtext.predict'),
    url(r'^', views.index, name= 'emotionFtext.index'),
    # url(r'^train/$', views.train, name='emotionFtext.train')

]
