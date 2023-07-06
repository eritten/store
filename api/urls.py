from .views import MyTokenObtainPairView, signup, change_email, change_password, change_username
from django.urls import path
app_name = "store buffet"

urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('change_email/', change_email, name='change_email'),
    path('change_password/', change_password, name='change_password'),
    path('change_username/', change_username, name='change_username'),
    path('signup/', signup, name='signup'),
]