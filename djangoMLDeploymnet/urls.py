from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # path('', include('basicConcepts.urls')),
    path('', include('irisApp.urls')),
    path('admin/', admin.site.urls),  
]

