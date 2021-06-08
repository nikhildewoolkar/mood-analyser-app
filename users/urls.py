from django.conf.urls import include, url
from django.contrib import admin
from users import views as user_views
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^$',views.main123,name="main123"),
 ]