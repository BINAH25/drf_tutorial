from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    #TokenRefreshView,
)

urlpatterns = [
    path('', views.api_home, name='api_home'),
    path('advocate', views.advocate_list ),
    path('advocate/<str:username>', views.advocate_detail),
    path('company', views.company_list ),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

]
