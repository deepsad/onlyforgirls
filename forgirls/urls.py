from django.conf.urls import include,url
from django.contrib import admin
'''from django.urls import path'''

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'', include('blog.urls')),
]
