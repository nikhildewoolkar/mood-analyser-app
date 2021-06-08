from django.conf.urls import include, url
from django.contrib import admin
from users import views as user_views
from django.conf.urls.static import static


urlpatterns = [
    # Examples:
    # url(r'^$', 'moodanalyzerml.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^register',user_views.register,name='register'),
    url(r'^login',user_views.login,name='login'),
    url(r'^logout',user_views.logout,name='logout'),
    url(r'^$',user_views.home,name='home'),
    url(r'^users/', include('users.urls')),
    url(r'^action/', user_views.action,name='action'),
    url(r'^moodimage/',user_views.moodimage,name='moodimage'),
    url(r'^happyres/',user_views.happyres,name='happyres'),

 ]
