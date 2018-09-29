from django.conf.urls import include, url
from django.contrib import admin

from .views import who_am_i
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('users.urls')),
    url(r'^blog/', include('blogs.urls')),
    url(r'^whoami/', who_am_i, name='whoami'),
    # For jwt token testing purposes
    url(r'^api-token-auth/', obtain_jwt_token),
	url(r'^api-token-verify/', verify_jwt_token),
    
]

