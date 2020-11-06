from django.urls import include, path

urlpatterns = [
    path('', include('registration.backends.simple.urls')),
]
