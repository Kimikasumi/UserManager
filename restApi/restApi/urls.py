from django.contrib import admin
from django.urls import include, path
admin.autodiscover()
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]