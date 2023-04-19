from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home import views

urlpatterns = [
path("", views.home, name="home"),
path("about/", views.about, name="about"),
path("contact/", views.contact, name="contact"),
#path("detail/<str:title>/<int:year>/<int:month>/<int:day>/", views.detail, name="detail"),
path("privacy/", views.privacy, name="privacy"),
path("terms/", views.terms, name="terms"),

    path('admin/', admin.site.urls),
]
