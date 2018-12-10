from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^classroom$', views.viewClassroom, name='classroom'),
    url(r'^classes$', views.viewClasses, name='student'),
]